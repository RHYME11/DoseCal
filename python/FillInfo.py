#======================== Step 1 ==================================#
# Fill target and beam information 
# If one target is separated  as multiple layers,
# the calculation will be run separately for each indivdual layer.
# The results will be summed in the end.
#==================================================================#

from miniCodes import *

#===================== Fill Information =========================#
def FillInfo():
  print("# ==================================== #")
  print("# ===== Step1: Fill Information ====== #")                                                                                            
  print("# ==================================== #")
  
  print("Warning: A thick target may attenuate the beam as it penetrates deeper.")
  print("It's recommended to split thick targets into multiple layers.")
  print("For each layer, the beam energy can be treated as uniform.")
  print("Please enter information for one layer only.")
  print("To account for multiple layers, run the code multiple times\n")
  # ===== Target ===== #
  while True:
    target_isotope = get_alpha_input("Enter Target Isotope Sympol (eg, Al) = ")
    target_A = get_integer_input("Enter Target A = ")
    target_thick = get_float_input("Enter Target Thickness (mg/cm2) = ")
    if check_isotope_exists(target_A, target_isotope):
      break
    else:
      print(f"{target_A}{target_isotope} doesn't exist. Please fill valid info!")
    
  # ===== Beam ===== #
  # When the beam pass the target, the energy will be attenuated 
  # But the beam rate is same 
  while True:
    beam_isotope = get_alpha_input("Enter Beam Isotope Sympol (eg, Kr) = ")
    beam_A = get_integer_input("Enter Beam A = ")
    beam_E = get_float_input("Enter Beam E (MeV) = ")
    beam_rate = get_float_input("Enter Beam Rate (pps) = ")
    beam_time = get_float_input("Enter Beam Running Time (sec) = ")
    if check_isotope_exists(target_A, target_isotope):
      break
    else:
      print(f"{beam_A}{beam_isotope} doesn't exist. Please fill valid info!")
    
  return target_isotope, target_A, target_thick, beam_isotope, beam_A, beam_E, beam_rate, beam_time












