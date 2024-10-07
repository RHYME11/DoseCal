import numpy as np

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


# ======= Calculate production rate (pps) for each isotope ======= #
# Need:
# 1. prodx_rate in pps
# 2. halflife in sec
# 3. beam_time in sec
def Cal_Prodx_A(prodx_rate, halflife, beam_time):
  # Eqn: prodx_A = prodx_rate * (1-exp(-0.693/halflife*beam_time))
  return prodx_rate * (1-np.exp(-0.693/halflife*beam_time))
