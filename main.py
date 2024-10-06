
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'python'))

from miniCodes import *
from CheckFileExistence import *
from FillInfo import *
from ReadPACE4 import *
from Extract_HalfLife import *

#==================================================================#
#=== Step0: Prepare and Check files
#=== Code: CheckFileExistence.py
Prepare()


#=== Step1: Fill Beam and Target Information
#=== Code: FillInfo.py
# return order:
# target_isotope, target_A, target_thick
# beam_isotope, beam_A, beam_E, beam_rate, beam_time 
tar_iso, tar_A, tar_th, beam_iso, beam_A, beam_E, beam_rate, beam_t = FillInfo()
info_txt = f"{beam_iso}{beam_A}_{tar_iso}{tar_A}_{int(beam_E)}MeV.txt"


#=== Step2: Read the associated PACE4 output
#=== Code: ReadPACE4.py
print("")
print("# ==================================== #")
print("# ===== Step2: Read PACE4 Result====== #")
print("# ==================================== #")
print("Default PACE4 Path: PACE4/{beam_isotope}{beam_A}_{target_isotope}{target_A}_{beam_E}MeV")
print("E.g. PACE4/Kr84_Al27_400MeV.pdf")
print("If it is saved in a different path, please type bwelow. Or hit 'Enter'")
pace4 = input("Please fill PACE4 pdf path: ")
if not '' in pace4:
   pdf_path = pace4
else:
  pdf_path = f"PACE4/{beam_iso}{beam_A}_{tar_iso}{tar_A}_{int(beam_E)}MeV.pdf" 

Beam_E, Recoil_E, Total, Production_Record = ReadPACE4(pdf_path)

if abs(Beam_E - beam_E) > 2:
  print("Beam energy in PACE4 file doesn't match your input. Please check!")
  exit()
else:
  total_xec = Total[-1]
  print(Production_Record)


#=== Step3: Extract halflife for isotopes saved in Production_Record from HalfLife.txt
#=== Code: Extract_halfLife.py
half_life_data = Extract_HalfLife()
Production_Record = append_half_life_to_production(Production_Record, half_life_data)
print(f"# of rows: {len(Production_Record)}")
print("after extracting halflife:")
print(Production_Record)












