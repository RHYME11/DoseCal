#==================================================================#
# Fill target and beam information 
# If one target is separated  as multiple layers,
# the calculation will be run separately for each indivdual layer.
# The results will be summed in the end.
#==================================================================#

from miniCodes import *



print("\nPlease fill info for multiple layer separately!")

#========================= Target ===============================#
target_isotope = get_alpha_input("Enter Target Isotope Sympol (eg, Al) = ")
target_A = get_integer_input("Enter Target A = ")
target_thick = get_float_input("Enter Target Thickness (mg/cm2) = ")


#========================= Beam== ===============================#
beam_isotope = get_alpha_input("Enter Beam Isotope Sympol (eg, Kr) = ")
beam_A = get_integer_input("Enter Beam A = ")
beam_E = get_float_input("Enter Beam E (MeV) = ")
beam_rate = get_float_input("Enter Beam Rate (pps) = ")
beam_time = get_float_input("Enter Beam Running Time (sec) = ")













