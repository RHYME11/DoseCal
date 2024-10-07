#============== Summarize  ===============#
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'python'))
from miniCodes import *
from FillInfo import *
from ReadFile import *


# === Read all files created from main.py
files_path = []
while True:
  file_input = input("Do you want to add a new file, y(default)/n: ").strip().lower()
  if 'n' in file_input:
    break
  while True: 
    file_path = input("Add file path: ").strip()
    if os.path.exists(file_path):
      if file_path in files_path:
        print("This file is already added.")
        continue
      else:
        files_path.append(file_path)
        break
    else:
      print("Please fill a valid path")
  
# === extract info from each file === #
# prodx_A read from parse_parameters_from_txt(file)
# is multiplied stopping_ratio already!
# =================================== #
summ = []
for file in files_path:
  # Extract parameters from the current file
  target_A, target_isotope, beam_A, beam_isotope, beam_E, beam_rate, beam_t, production = parse_parameters_from_txt(file)
  
  # Check if summ already contains elements
  if summ:
    # Extract reference info from the first element of summ
    ref_target_A, ref_target_isotope, ref_beam_A, ref_beam_isotope, _, _, ref_beam_t, _ = summ[0]
    
    # Check if the current file's parameters match the reference values
    if (target_A != ref_target_A or
        target_isotope != ref_target_isotope or
        beam_A != ref_beam_A or
        beam_isotope != ref_beam_isotope or
        beam_t != ref_beam_t):
      
      # Print the file name and exit if there's a mismatch
      print(f"Inconsistent data in file: {file}")
      sys.exit(1)  # Exit the program with an error code

  # Append the data to the summ list if consistent
  summ.append([target_A, target_isotope, beam_A, beam_isotope, beam_E, beam_rate, beam_t, production])

# Sort the summ list in place based on beam_E (index 4) in descending order
summ.sort(key=lambda x: x[4], reverse=True)



print(summ)















