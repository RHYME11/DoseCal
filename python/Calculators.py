# =========== Here includes all calcualtors ========== #


# ======= Calculate production rate (pps) for each isotope ======= #
# Need:
# 1. xsec for isotopes in mb
# 2. target thickness for the current layer in mg/cm2
# 3. target mass (needs to be converted in 'g')
# 3.* mass number ~= molar mass
# 4. beam rate in pps
def Cal_Prodx_Rate(xec, target_thick, target_A, beam_rate):
  # Eqn: prodx_rate = xsec(m2) * unit_thick(g/m2) / mass(g) *rate (atom/s)
  # 1 mb = 1e-3 barn = 1e-3 * 1e-28 m2
  # 1 mg/cm2 = 10 g/m2
  # mass = A/N_A gram
  # N_A (iAvogadro constant) = 6.02e23
  mass = A/6.02e23
  production_rate = (xsec/1e3/1e28)*(thick_tot*10)/mass*rate
  return prodx_rate
