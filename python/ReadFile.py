import re
import os

# =========== Run at the beginnig of summarize.py =========#
# Read information from WriteFile.py
def parse_parameters_from_txt(file_path):
  with open(file_path, 'r') as file:
    lines = file.readlines()

    # Extract relevant parameters from the first few lines
    target_line = lines[0].strip()
    beam_line = lines[3].strip()
    energy_line = lines[4].strip()
    rate_line = lines[5].strip()
    time_line = lines[6].strip()

    # Use regex to extract the values from each line
    target_match = re.match(r"Target:\s*(\d+)([A-Za-z]+)", target_line)
    beam_match = re.match(r"Beam:\s*(\d+)([A-Za-z]+)", beam_line)
    energy_match = re.match(r"Energy:\s*([\d.]+)\s*MeV", energy_line)
    rate_match = re.match(r"Rate:\s*([\d.eE+-]+)\s*pps", rate_line)
    time_match = re.match(r"Running Time:\s*([\d.]+)\s*sec", time_line)

    # Extract parameters
    target_A = int(target_match.group(1))
    target_isotope = target_match.group(2)
    beam_A = int(beam_match.group(1))
    beam_isotope = beam_match.group(2)
    beam_E = float(energy_match.group(1))
    beam_rate = float(rate_match.group(1))
    beam_t = float(time_match.group(1))

    # Search for header line#
    header_index = next(i for i, line in enumerate(lines) if line.startswith("#"))  
    #production = [['A',"Isotope",'t1/2', 'unit', 'Prodx_A(Bq)']]
    production = []
    for line in lines[header_index+1:]:
      # Skip empty lines
      if not line.strip():
        continue
      # Split the line into columns and process the values
      row = line.strip().split()
      prodx_A = float(row[7])*float(row[8])
      production.append([int(row[0]),row[1],float(row[3]),row[4],prodx_A]) 
  
  return target_A, target_isotope, beam_A, beam_isotope, beam_E, beam_rate, beam_t, production











