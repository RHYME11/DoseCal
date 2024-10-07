
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'python'))

from miniCodes import *
from CheckFileExistence import *
from FillInfo import *
from ReadPACE4 import *
from Extract_HalfLife import *
from Calculators import *
from WriteFile import *

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


#=== Step3: Extract halflife for isotopes saved in Production_Record from HalfLife.txt
# Production_Record includes:
# [['Z', 'N', 'A', 'isotope', 'x-section(mb)', 't1/2_value', 't1/2_unit'], 
#  [49, 57, 106, 'In', 40.6, '6.2', 'm'], 
#  [49, 57, 106, 'In_isomer', 40.6, '6.2', 'm', '5.2', 'm']]
# In_isomer was added in "append_half_life_to_production()"
#=== Code: Extract_halfLife.py
half_life_data = Extract_HalfLife()
Production_Record = append_half_life_to_production(Production_Record, half_life_data)



# ==== Step4: Calculations ==== #
# =Step4.0: calculate recoil energy for isotope:
# ==for later Stopping Ratio calculation

# =Step4.1: calculate production rate (pps), need:
# ==xsec in `mb` (read from PACE4 file)
# ==target thickness in `mg/cm2` (from input in Step1)
# ==target mass in `g` (from input in Step1, will be converted in the code)
# ===mass number ~= molar mass
# ==beam rate in `pps` (from input in Step1)

# =Step4.2: Calculate production activity (Bq), need:
# ==prodx_rate in pps
# ==halflife in sec
# ==beam_tiem in sec

Production_Record[0].append("Recoil_E(MeV)")
Production_Record[0].append("Prodx_Rate(pps)")
Production_Record[0].append("Prodx_A(Bq)")
for ind in range(1, len(Production_Record)):
  xsec = Production_Record[ind][4]
  halflife = Production_Record[ind][5] * HalfLife_Unit_Factor(Production_Record[ind][6]) # convert halflife in sec
  prodx_A = Production_Record[ind][2]
  compound_A = tar_A + beam_A
  prodx_recoile =  Cal_Prodx_RecoilE(prodx_A, compound_A, Recoil_E)
  prodx_rate = Cal_Prodx_Rate(xsec, tar_th, tar_A, beam_rate)
  prodx_A = Cal_Prodx_A(prodx_rate, halflife, beam_t) 
  Production_Record[ind].append(prodx_recoile)
  Production_Record[ind].append(prodx_rate)
  Production_Record[ind].append(prodx_A)

Production_Record[0].append("Stopping_Ratio")
for ind in range(1, len(Production_Record)):
  Production_Record[ind].append(1)

#================ Write everything into txt file =====================#

write_to_txt(Production_Record, beam_iso, beam_A, tar_iso, tar_A, beam_E, tar_th, beam_rate, beam_t)










