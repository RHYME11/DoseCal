import os

#== miniCode: 
# change al or AL =>Al
# change c => C
def format_isotope(isotope):
  # Format the isotope to be upper or upper-lower
  if len(isotope) == 1:
    return isotope.upper()
  elif len(isotope) == 2:
    return isotope[0].upper() + isotope[1].lower()
  return isotope  # Default, return as is if more than 2 characters

def get_valid_filename(file_name):
  # If the file exists, ask the user if they want to replace it
  if os.path.exists(file_name):
    replace = input(f"'{file_name}' already exists. Do you want to replace it? y(default)/n: ").lower()
    if 'n' in replace:
      # If not replacing, add "_copy" to the file name
      file_name = file_name.replace(".txt", "_copy.txt")
  return file_name


# =========== Run in the end of main.py =========#
# Write production information of one layer 
def write_to_txt(production_record, beam_isotope, beam_A, target_isotope, target_A, beam_E, target_thickness, beam_rate, beam_t):
  # Format the isotopes and ensure beam_A, target_A, beam_E are integers
  beam_isotope = format_isotope(beam_isotope)
  target_isotope = format_isotope(target_isotope)
  beam_A = int(beam_A)
  target_A = int(target_A)
  beam_E = int(beam_E)
  
  # Define the base file name
  base_name = f"{beam_isotope}{beam_A}_{target_isotope}{target_A}_{beam_E}MeV.txt"
  
  # Get a valid file name (either original or with "_copy" if required)
  file_name = get_valid_filename(base_name)

  # Define the header you want to write
  header = ["#A", "Isotope", "xsec(mb)", "t1/2_value", "t1/2_unit", "Recoil_E(MeV)", 
            "Prodx_Rate(pps)", "Prodx_A(Bq)", "Stopping_Ratio"]

  # Open the file for writing
  with open(file_name, 'w') as file:
    # Add additional info lines before the header
    file.write(f"Target: {target_A}{target_isotope}\n")
    file.write(f"Thickness: {target_thickness} mg/cm2\n")
    file.write("\n")  # Empty line
    file.write(f"Beam: {beam_A}{beam_isotope}\n")
    file.write(f"Energy: {beam_E} MeV\n")
    file.write(f"Rate: {beam_rate:.2e} pps\n")
    file.write(f"Running Time: {beam_t} sec\n")
    file.write("\n")  # Another empty line before header

    # Write the header
    file.write("\t".join(header) + "\n")

    # Write the required information for each isotope in production_record
    for row in production_record[1:]:  # Skip the header row in production_record
      A = int(row[2])
      isotope = str(row[3])
      xsec_mb = round(float(row[4]), 2)
      t1_2_value = round(float(row[5]), 2)
      t1_2_unit = str(row[6])
      recoil_E = round(float(row[7]), 2)
      prodx_rate = round(float(row[8]), 2)
      prodx_A = round(float(row[9]), 2)
      stopping_ratio = round(float(row[10]), 2)

      # Format the row and write it into the file
      file.write(f"{A}\t{isotope}\t{xsec_mb}\t{t1_2_value}\t{t1_2_unit}\t{recoil_E}\t{prodx_rate}\t{prodx_A}\t{stopping_ratio}\n")

  print(f"Data written to {file_name}")















