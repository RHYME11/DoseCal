#=================== Step 3 =====================#                                                                                             
# Read HalfLife.dat
# Extract t1/2 value and unit
# If HalfLife.dat does not exist, please follow README
#================================================#

import re

# ============= Function to parse the t_half value into t_value + t_unit ==============#
# the input "t_half" should have one character (no-digit) part
def parse_t_half(t_half):
  # if t1/2 = stable, will return the age of the universe
  if t_half.upper() == "STABLE":
    return 1.4e10, "y"
  matches = re.findall(r'(\d+(?:\.\d+)?(?:e[-+]?\d+)?)\s*([a-zA-Z]+)', t_half)
  # Initialize variables for the extracted values
  t_value = -1
  t_unit = None
  # If matches are found, assign the number and unit
  if matches:
    t_value = float(matches[0][0])  # First number found
    t_unit = matches[0][1]    # Corresponding unit
  return t_value, t_unit


# ============= Function to extract t1/2 from dat ==============#
# extracted_data = [A,"nucleus_name", t1/2, "unit"]
def Extract_HalfLife(dat_path="HalfLife/HalfLife.dat"):
  # Open the existing TXT file and process it
  with open(dat_path, "r") as input_file:
    extracted_data = []
    # Skip the first line (header)
    next(input_file)
    for line in input_file:
      # Skip any empty lines
      if not line.strip():
        continue
      # Split the line into columns
      columns = line.split()
      # Extract Nucleus (separated into number and letters, like "1H" to "1" and "H")
      nucleus_full = columns[0]
      nucleus_number = ''.join([char for char in nucleus_full if char.isdigit()])
      nucleus_letters = ''.join([char for char in nucleus_full if char.isalpha()])
      # Extract and parse T 1/2
      t_half = ' '.join(columns[3:])
      value, unit = parse_t_half(t_half)
      if value > 0:
        # Append the extracted data as a tuple
        extracted_data.append((float(nucleus_number), nucleus_letters, value, unit))
  return extracted_data



# ========= Function to append t1/2 information to Production_Record
def append_half_life_to_production(production_record, half_life_data):
  # Add headers for t1/2 values
  production_record[0].append("t1/2_value")
  production_record[0].append("t1/2_unit")
  
  i = 1
  while i < len(production_record):
    A = production_record[i][2]  # Extract A (mass number)
    isotope = production_record[i][3]  # Extract isotope symbol
    matching_half_lives = [data for data in half_life_data if int(data[0]) == A and data[1].lower() == isotope.lower()]

    if len(matching_half_lives) == 1:
      # If there is only one match, append it to the production record
      production_record[i].append(float(matching_half_lives[0][2]))  # t1/2 value as float
      production_record[i].append(f"{matching_half_lives[0][3]}")  # t1/2 unit (as string)

    elif len(matching_half_lives) > 1:
      # If there are multiple matches (isomer case)
      # Append the first match to the current row
      production_record[i].append(float(matching_half_lives[0][2]))  # t1/2 value as float
      production_record[i].append(f"{matching_half_lives[0][3]}")  # t1/2 unit (as string)

      # Create a copy of the current row for the isomer and append the second half-life
      isomer_row = production_record[i][:]  # Copy the row
      isomer_row[3] = f"{isotope}_m"  # Change isotope to "isotope_isomer"
      
      # Remove the first t1/2 value and unit (we are modifying the last two elements)
      isomer_row[-2] = float(matching_half_lives[1][2])  # 2nd t1/2 value as float
      isomer_row[-1] = f"{matching_half_lives[1][3]}"  # 2nd t1/2 unit (as string)

      # Insert the isomer row into the production record
      production_record.insert(i + 1, isomer_row)

      # Move the index to skip the newly inserted isomer row
      i += 1

    else:
      # If no match found, append "N/A"
      production_record[i].append("N/A")
      production_record[i].append("N/A")

    i += 1

  return production_record










