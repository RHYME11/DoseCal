from miniCodes import *  
from tqdm import tqdm

#==================== Step 0 =========================#  
def Prepare():
  
  print("# ==================================== #")
  print("# ===== Step0: Check Preparetion ===== #")
  print("# ==================================== #")
  # List of files to check
  files_to_check = [
      "HalfLife/HalfLife.txt",
      "DoesParFiles/Body_unshield.txt",
      "DoesParFiles/Body_shield.txt",
      "DoesParFiles/Skin_unshield.txt",
      "DoesParFiles/Skin_shield.txt",
      "DoesParFiles/Breath_Par.txt"
  ]

  # List to store missing files
  missing_files = []

  # Progress bar for file checking
  for file_path in tqdm(files_to_check, desc="Checking files", unit="file"):
      if not os.path.exists(file_path):
          missing_files.append(file_path)

  # If there are missing files, print them and exit
  if missing_files:
      print("\nThe following files are missing:")
      for missing_file in missing_files:
          print(missing_file)
      print("\nPlease check and add the missing files. Exiting...")
      exit()  

  # Final message to ask for PACE4 preparation
  print("\nPlease make sure the associated PACE4 calculation results are ready and saved in the PACE4 folder.")
  print("Default name format: {beam_name}{beam_A}_{target_name}{target_A}_{beam_energy}MeV.pdf")
  print("For example: Kr84_27Al_400MeV.pdf\n") 




