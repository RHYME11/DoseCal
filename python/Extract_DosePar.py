import os
# ======== This code is used in summarize.py ======== #
# Input all dose par files needed for the future calculation
# Give the does parameter path with given number
  
def Does_Path(path_num):
  # Map input numbers to corresponding dose file paths
  dose_file_mapping = {
    '1': "DoseParFiles/Body_unshield.dat",
    '2': "DoseParFiles/Body_shield.dat",
    '3': "DoseParFiles/Skin_unshield.dat",
    '4': "DoseParFiles/Skin_shield.dat",
    '5': "DoseParFiles/Breath_Par.dat"
  }
  # Return the dose file path or an empty string if invalid input
  return dose_file_mapping.get(path_num, '')

def get_dose_input():
  # Function to handle input and validation
  
  while True:
    dose_input = input("Please choose a Dose type (1-5): ").strip()
    if dose_input.isdigit() and Does_Path(dose_input):  # Check if valid number and valid dose file
      return dose_input
    print("Invalid input. Please fill a number between 1 and 5")

def calculate_doses():
  dose_files = []
  print("1: DoseParFiles/Body_unshield.dat")
  print("2: DoseParFiles/Body_shield.dat")
  print("3: DoseParFiles/Skin_unshield.dat")
  print("4: DoseParFiles/Skin_shield.dat")
  print("5: DoseParFiles/Breath_Par.dat")


  # First dose calculation input
  print("Please choose which type of Dose you want to calculate:")
  dose_input = get_dose_input()
  dose_files.append(Does_Path(dose_input))

  # Additional dose calculations (optional)
  while True:
    dose_input = input("Do you want to calculate another Dose type? (1-5 for more, 'n' or Enter to finish): ").strip().lower()
    if dose_input == '' or dose_input == 'n':  # Exit if 'n' or Enter
      break
    elif dose_input.isdigit() and Does_Path(dose_input):  # Check if valid number
      dose_file = Does_Path(dose_input)
      # Check if the file is already in the list
      if dose_file in dose_files:
        print(f"{dose_file} has already been added. Please choose another dose type.")
      else:
        dose_files.append(dose_file)
    else:
      print("Invalid input. Please fill a number between 1 and 5.")

  # Define the preferred order of files
  preferred_order = [
    "DoseParFiles/Body_unshield.dat",
    "DoseParFiles/Body_shield.dat",
    "DoseParFiles/Skin_unshield.dat",
    "DoseParFiles/Skin_shield.dat",
    "DoseParFiles/Breath_Par.dat"
  ]

  # Sort dose_files based on the preferred order
  dose_files = sorted(dose_files, key=lambda x: preferred_order.index(x))

  return dose_files


# ==== Read Parameters from dose par files ==== #
# Function to read parameters from dose files
def read_dose_parameters(file_path):
  dose_params = {}
  with open(file_path, 'r') as file:
    for line in file:
      line = line.strip()
      # Skip comments or empty lines
      if not line or line.startswith('#'):
        continue
      # Extract relevant data
      parts = line.split()
      isotope = parts[1]
      par = float(parts[2])
      dose_params[isotope] = par
  return dose_params



