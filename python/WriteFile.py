import os
import re

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



# =========== Run in the end of summarize.py =========#
# Write dose into individual txt files based on cd time
def write_dose_lists_to_files(dose_lists):
  for dose_list in dose_lists:
    # Extract the 'Prodx_A(Bq)' header to create the filename
    header = dose_list[0]
    cd_value = header[4]  # Extract the 'Prodx_A(Bq)@cd=X' part

    # Extract only the part after 'cd=' using a regular expression
    cd_value_cleaned = re.search(r'cd=.*', cd_value).group()  # Get only 'cd=X'
    
    # Format the filename to include only underscores as special characters
    cd_value_cleaned = re.sub(r'[^\w\s]', '_', cd_value_cleaned)  # Replace non-alphanumeric characters with '_'
    filename = f"{cd_value_cleaned}.txt"

    # Write the content to the file
    with open(filename, 'w') as file:
      for row in dose_list:
        # Round numeric values under 'Prodx_A(Bq)' and dose columns to 2 decimal places
        rounded_row = [
          f"{x:.2f}" if isinstance(x, (float, int)) and idx >= 4 else str(x)
          for idx, x in enumerate(row)
        ]
        # Convert each row into a string of tab-separated values and write to the file
        file.write('\t'.join(map(str, rounded_row)) + '\n')

# =========== Run in the end of summarize.py =========#
# Write all sum values in "summary.txt"
def write_summary_file(dose_lists):
  # Initialize summary content
  summary_rows = []

  # Build summary header dynamically based on dose_list[0]
  first_dose_list = dose_lists[0][0]  # Header of the first dose_list
  summary_header = ['cd'] + first_dose_list[5:]  # Collect all headers starting from column 5

  for dose_list in dose_lists:
    # Extract the 'Prodx_A(Bq)@cd=X' part to determine the cd value
    header = dose_list[0]
    cd_value = header[4]  # 'Prodx_A(Bq)@cd=X'

    # Extract the part after 'cd=' to get the actual cd value (e.g., '1.5m')
    cd_value_cleaned = cd_value.split('cd=')[-1]  # Extract part after 'cd='

    # Initialize a row for the summary
    summary_row = [cd_value_cleaned]
    dose_sums = [0] * (len(header) - 5)  # To store sums for each dose type, starting from column 6

    # Iterate through the dose_list and find the 'sum' row
    for row in dose_list:
      # If the row is the 'sum' row, collect the dose values for summary
      if row[0] == 'sum':
        for i in range(len(dose_sums)):
          dose_sums[i] = round(row[i + 5], 2)  # Collect sum values for each dose

    # Append the dose sums to the summary row
    summary_row.extend([str(dose) for dose in dose_sums])
    summary_rows.append(summary_row)

  # Write the summary file
  with open("summary.txt", 'w') as summary_file:
    # Write the header
    summary_file.write('  '.join(summary_header) + '\n')

    # Write each summary row
    for summary_row in summary_rows:
      summary_file.write('  '.join(summary_row) + '\n')







