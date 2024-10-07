import numpy as np
from Extract_DosePar import *
# =========== Here includes all calcualtors ========== #

# ======= Calculate recoil energy (MeV) for productions ===== #
# As a reference for future Stopping ratio
# Need:
# 1. Recoil Energy of compound nucleus
# 2. A of compound nucleus
# 3. A of productions
def Cal_Prodx_RecoilE(prodx_A, compound_A, Total_RecoilE):
  # Eqn: prodx_recoile = Total_RecoilE / compound_A * prodx_A
  return Total_RecoilE / compound_A * prodx_A


# ======= Calculate production rate (pps) for each isotope ======= #
# Need:
# 1. xsec for isotopes in mb
# 2. target thickness for the current layer in mg/cm2
# 3. target mass (needs to be converted in 'g')
# 3.* mass number ~= molar mass
# 4. beam rate in pps
def Cal_Prodx_Rate(xsec, target_thick, target_A, beam_rate):
  # Eqn: prodx_rate = xsec(m2) * unit_thick(g/m2) / mass(g) *rate (atom/s)
  # 1 mb = 1e-3 barn = 1e-3 * 1e-28 m2
  # 1 mg/cm2 = 10 g/m2
  # mass = A/N_A gram
  # N_A (iAvogadro constant) = 6.02e23
  mass = target_A/6.02e23
  prodx_rate = (xsec/1e3/1e28)*(target_thick*10)/mass*beam_rate
  return prodx_rate


# ======= Calculate production A (Bq) for each isotope ======= #
# Need:
# 1. prodx_rate in pps
# 2. halflife in sec
# 3. beam_time in sec
def Cal_Prodx_A(prodx_rate, halflife, beam_time):
  # Eqn: prodx_A = prodx_rate * (1-exp(-0.693/halflife*beam_time))
  return prodx_rate * (1-np.exp(-0.693/halflife*beam_time))

# ======= Code used in summarize.py ========= #
# ======= Calculate production A(Bq) after cd ======= #
# Need:                                                    
# 1. prodx_A in Bq                                     
# 2. halflife in sec                                       
# 3. cd time in sec 
def Cal_A_cd(prodx_A, halflife, t):
  # Eqn: prodx_A = prodx_A * exp(-0.693/halflife * t)
  return prodx_A * np.exp(-0.693/halflife * t)

# ======= Caculate Prodution Dose(uSv/h) ========== #
# Function to match isotopes and calculate dose
# dose_files = # of dose file input (e.g. dose_files = ['Body_unshield.txt', 'Skin_shield.txt'])
# dose_lists is grouped by cd times (e.g. cd = 0s, 15min, 1h, 1d. Then len(dose_lists) = 4)
# before calculation dose_list = ['A', 'Isotope', 't1/2', 'unit', 'prodx_A(Bq)@cd=?']
# after calculation dose_list = ['A', 'Isotope', 't1/2', 'unit', 'prodx_A(Bq)@cd=?', 'Body_unshield(uSv/h)', 'Skin_shield(uSv/h)']
def calculate_dose(dose_lists, dose_files): 
  # Read dose parameters from all files     
  dose_params_list = [read_dose_parameters(dose_file) for dose_file in dose_files]
                                   
  for dose_list in dose_lists:     
    header = dose_list[0]  # The first row is the header
    # Add a new column for each dose file to the header
    for dose_file in dose_files:   
      file_name_without_ext = os.path.basename(dose_file).split(".")[0]
      header.append(f"{file_name_without_ext}(uSv/h)")
                                   
    # Iterate through the rows in the dose_list   
    for row in dose_list[1:]:      
      A, isotope, t_half, unit, prodx_A = row[:5] 
                                   
      # Correct "isotope_m" to "isotope_isomer"   
      if isotope.endswith("_m"):   
        isotope = isotope.replace("_m", "_isomer")
                                   
      # Calculate dose for each dose file   
      for dose_params in dose_params_list:  
        dose = 0                   
        if isotope in dose_params: 
          par = dose_params[isotope]  # Get the parameter from the dose file
          dose = prodx_A/1e9 * par  # Calculate the dose
                                   
        # Append the dose to the row        
        row.append(dose)           
                                   
  return dose_lists

# ====== Calculate sum of Dose in dose_lists ===== #
# Function to add sum of dose
def add_sum_row(dose_lists):
  for dose_list in dose_lists:
    # Initialize the sum row, starting with ['sum', '', '', '', ''] for the first five elements
    sum_row = ['sum', '', '', '', '']
    
    # Sum the values in each column from the 6th to the 10th column
    for col_index in range(5, len(dose_list[0])):  # Start summing from the 6th column
      column_sum = 0
      for row in dose_list[1:]:  # Skip the header (index 0)
        column_sum += row[col_index] if isinstance(row[col_index], (int, float)) else 0
      
      # Append the column sum to the sum_row
      sum_row.append(column_sum)
    
    # Append the sum_row to the dose_list
    dose_list.append(sum_row)
 
  return dose_lists



