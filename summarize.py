#============== Summarize  ===============#
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'python'))
from miniCodes import *
from FillInfo import *
from ReadFile import *
from Summary import *
from Calculators import *
from Extract_DosePar import *
from WriteFile import *

# === Read all files created from main.py === #
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
# =========================================== #
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

# =========================================== #
# === combine productions among files === #
# === add production activities together === #
# sum_prodx = [['A', 'Isotope', 't1/2', 'unit', 'Prodx_A(Bq)']]
# The last element 'Prodx_A(Bq)' is when beam stops (cd = 0 sec)

sum_prodx = combine_productions(summ)


# =============== Activity after cd ====================== #
# === 1. Input cd time === #
print("Warning: Empty input will skip waiting time input!")
cd = []
while True:
  cd_input = input("How long will you wait after stopping beam (in sec): ")
  # if there is empty input, quit this loop
  if cd_input == '':
    break 
  # if there is a number input, save it in cd.list for future calculation
  else:
    cd.append(float(cd_input))
    cd_t, cd_unit = Time_Seconds_Unit(cd[-1])
    sum_prodx[0].append(f'Prodx_A(Bq)@cd={cd_t}{cd_unit}')
            

# === 2. Calculate Prodx_A with cd time === #
for iso in sum_prodx[1:]:
  halflife = iso[2]*HalfLife_Unit_Factor(iso[3]) # convert halflife into seconds
  prodx_A = iso[4]
  for t in cd:
    iso.append(Cal_A_cd(prodx_A, halflife, t))


# =============== Calculate Does ======================== #
# 1. Read Does Parameters:

dose_files = calculate_doses()

# 2.regroup sum_prodx based on cd times: e.g. there 4 cd times, len(dose_lists) = 4
# in dose_lists: 
# A = 0 has been removed
# For isotope and isotope_isomer case: only keep the one with higher A
# now, len(dose_lists) = the number of cd inputs
# dose_lists[0] = ['A', 'Isotope', 't1/2', 'unit', 'A(Bq)@cd=?']
dose_lists = split_sum_prodx(sum_prodx) 
  
# 3. loop dose_lists
# read dose par out and calculate dose under different dose cases 
# calculate dose types under different cd time
# If there are 5 types input in 'dose_files'
# Here will be 5 elements added in each row
dose_lists = calculate_dose(dose_lists, dose_files)


# 4. sum dose
dose_lists = add_sum_row(dose_lists)

# 5. Write each dose_list in a file
# And write all sum into a summay.txt
write_dose_lists_to_files(dose_lists)
write_summary_file(dose_lists)

#print(dose_lists)















