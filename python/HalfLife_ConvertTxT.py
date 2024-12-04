#=============================================#
# Convert Halflife pdf file to dat file
# It won't over write on the existing dat file
#=============================================#

from miniCodes import *
from tqdm import tqdm

def Convert_PDF_to_TXT(pdf_path, flag_overwrite = False):
    # Get the base name of the PDF file (without the extension) using string operations
    base_name = pdf_path.split('/')[-1].replace('.pdf', '')
    # Create the output TXT file name
    dat_path = pdf_path.replace('.pdf', '.dat')
    
    # if dat file exists and don't need to be replaced, return empty
    if os.path.exists(dat_path) and not flag_overwrite:
      print("Keep the old HalfLife.dat. Bye ~")  
      return
    # if dat file doesn't exist or you want to overwrite it
    else:
        # Open the PDF file
        with pdfplumber.open(pdf_path) as pdf:
            text_to_write = []
            capture_text = False # will be "True" when detect "Nucleus E level(keV) Jπ T 1/2" where start extracting info
            # Iterate through each page
            for page in tqdm(pdf.pages, desc="Processing pages", unit="page"):
                # Extract the text from the page
                text = page.extract_text() 
                # Split the text into lines
                lines = text.split('\n')
                for line in lines:
                    # Skip the unwanted header and footer lines
                    #if "page" in line.lower() and "," in line and ("AM" in line or "PM" in line):
                    if "AM" in line or "PM" in line:
                        continue
                    if "https://www.nndc.bnl.gov" in line:
                        continue     
                    # Start capturing text after the target start line
                    if "Nucleus E level(keV) Jπ T 1/2" in line:
                        capture_text = True
                        continue
                    # Stop capturing text after the target end line
                    if "Gamma Information" in line:
                        capture_text = False
                        continue
                    if "≥" in line or ">" in line:
                        continue
                    if "eV" in line:
                        continue
                    # Capture the text
                    if capture_text:
                        text_to_write.append(line)
        # Write the captured text to the dynamically named dat file
        with open(dat_path, "w") as output_file:
          output_file.write("#Nucleus E_level Jpi t1/2\n")  
          output_file.write("\n".join(text_to_write))

#================================ mian code =======================================#


pdf_path = get_pdf_file_input("Enter half-life pdf file path: ")
dat_path = pdf_path.replace('.pdf', '.dat')
if os.path.exists(dat_path):
  overwrite =input(f"{dat_path} exists. Do you want to overwrite it, y/n(default): ")
  if 'y' in overwrite.lower():
    flag = True
  elif 'n' or '' in overwrite.lower():
    flag = False

Convert_PDF_to_TXT(pdf_path, flag)











