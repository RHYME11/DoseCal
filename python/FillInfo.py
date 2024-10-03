#==================================================================#
# Fill target and beam information 
# If one target is separated  as multiple layers,
# the calculation will be run separately for each indivdual layer.
# The results will be summed in the end.
#==================================================================#

from miniCodes import *

print("\nPlease fill info for multiple layer separately!")

#========================= Target ===============================#
While True:
  target_isotope = get_alpha_input("Enter Target Isotope Sympol (eg, Al) = ")
  target_A = get_integer_input("Enter Target A = ")
  print("Please enter the thickness for individual layer, if target is separated to multiple layers!")
  target_thick = get_float_input("Enter Target Thickness (mg/cm2) = ")
  if check_isotope_exists(target_A, target_isotope):
    break
  else:
    print(f"{target_A}{target_isotope} doesn't exist. Please fill valid info!")
#========================== Beam =================================#
# When the beam pass the target, the energy will be attenuated 
# But the beam rate is same 
While True:
  beam_isotope = get_alpha_input("Enter Beam Isotope Sympol (eg, Kr) = ")
  beam_A = get_integer_input("Enter Beam A = ")
  print("Please enter the energy when the beam dlivery to the current target layer!")
  beam_E = get_float_input("Enter Beam E (MeV) = ")
  beam_rate = get_float_input("Enter Beam Rate (pps) = ")
  beam_time = get_float_input("Enter Beam Running Time (sec) = ")
  if check_isotope_exists(target_A, target_isotope):
    break
  else:
    print(f"{beam_A}{beam_isotope} doesn't exist. Please fill valid info!")












