#=================== Step 2 =====================#
# Read PACE4 output 
# Extract Total_xec, Recoil_Energy(Compound)
# Generate List for all productions with isotope, A and x-sec
#================================================#

from miniCodes import *

#=== extract Compound Info from PDF
def Extract_CompoundInf(text):
  # Return Values:
  Coulomb_Barrier = -1
  Center_Mass = -1
  Recoil_Energy = -1
  Beam_Energy = -1
  Compound_A = -1
  
  lines = text.split('\n')
  # loop all lines in this text(page)
  for i, line in enumerate(lines):
      if "Bass fusion xsection for E = " in line:
          match = re.search(r'Bass fusion xsection for E = (\d+(\.\d+)?)\s*MeV', line)
          if match:
              Beam_Energy = float(match.group(1))
              continue
      if "Barrier height" in line:
          match = re.search(r'Barrier height is (\d+(\.\d+)?)\s*MeV', line)
          if match:
              Coulomb_Barrier = float(match.group(1))
              continue
      if "Center of mass energy (MeV)" in line:
          match = re.search(r'Center of mass energy \(MeV\)\s*(\d+(\.\d+)?)', line)
          if match:
              Center_Mass = float(match.group(1))
              continue
      if "Compound nucleus recoil energy (MeV)" in line:
          match = re.search(r'Compound nucleus recoil energy \(MeV\)\s*(\d+(\.\d+)?)', line)
          if match:
              Recoil_Energy = float(match.group(1))
              break
      if "Compound nucleus " in line and Compound_A < 0:
          columns = line.split()
          Compound_A = float(columns[-1])

  if Beam_Energy<0:
      print("Beam energy NOT Found")
  if Coulomb_Barrier<0:
      print("Barrier height NOT Found")
  if Center_Mass<0:
      print("Center of mass energy NOT Found")
  if Recoil_Energy<0:
      print("Compound nucleus recoil energy NOT Found")
  if Compound_A<0:
      print("Compound nucleus info NOT Found")
 
  return Beam_Energy, Coulomb_Barrier, Center_Mass, Recoil_Energy, Compound_A


#=== extract Production Info from PDF
def Extract_ProductInf(pdf):
  start_flag = False 
  end_flag = False
  Production_Inf = []
  for page_num, page in enumerate(pdf.pages[1:]):
      if start_flag and end_flag: break
      text = page.extract_text()
      if text:
          lines = text.split('\n')
          for i, line in enumerate(lines):
              if "Yields of residual nuclei" in line: 
                  start_flag = True
                  continue
              if "Angular distribution results" in line: 
                  end_flag = True
                  break
              if start_flag and not end_flag:
                  Production_Inf.append(line.split())
  if not Production_Inf:
      print("Yields of residual nuclei NOT Found")
  return Production_Inf

#=== filter Production Info
def Filter_Inf(Production):
  # If production cross pages, there will be line written in "Production" with one element which returns page number
  # So we need to delete it first
  Production = [row for row in Production if len(row) > 1]

  # Take out the last line which contains total information for the reaction
  # Then delete it from "Production"
  Total = Production[-1]
  Production = Production[:-1]

  # Add "isotop for the Column name"
  Production[0].insert(3, "isotope")
  
  # Only Record Z, N, A, isotope, xsection information into Excel
  # And convert all values to int or float
  Production_Record = [[row[0], row[1], row[2], row[3], row[6]] for row in Production]
  for row in Production_Record[1:]:
      row[0] = int(row[0])  # Convert Z to int
      row[1] = int(row[1])  # Convert N to int
      row[2] = int(row[2])  # Convert A to int
      row[4] = float(row[4])  # Convert x-section(mb) to float
  
  return Total, Production_Record

#=== Read PACE4 pdf file
def ReadPACE4(pdf_path):
  with pdfplumber.open(pdf_path) as pdf:
      # Extract basic information for this reaction
      page = pdf.pages[0]
      text = page.extract_text()
      Beam_Energy, Coulomb_Barrier, Center_Mass, Recoil_Energy, Compound_A = Extract_CompoundInf(text)
      # Extract info for productions from the reaction
      Production = Extract_ProductInf(pdf)

  # Filter Production info to write them into Spreadsheet
  Total, Production_Record = Filter_Inf(Production)
  return Beam_Energy,Recoil_Energy, Total, Production_Record












