import os

#=========================================================================#
#============= Following mini codes are called in FillInfo.py ============#
#=========================================================================#
def get_alpha_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isalpha():
            return user_input
        else:
            print("Warning: Please enter letters only (no numbers or special characters).")
# Function to validate integer input
def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Warning: Please enter a valid number!")

# Function to validate float input
def get_float_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Warning: Please enter a valid number!")


#=========================================================================#
#==================== Mini Codes related to Half-Life=====================#
#=========================================================================#
def get_pdf_file_input(prompt):
    while True:
        pdf_path = input(prompt)
        
        # Check if the file exists
        if not os.path.exists(pdf_path):
            print("Warning: The file does not exist. Please enter a valid file path.")
            continue
        
        # Check if the file is a PDF by checking its extension
        if not pdf_path.lower().endswith('.pdf'):
            print("Warning: The file is not a PDF. Please enter a valid PDF file.")
            continue
        
        # If both checks pass, return the file path
        return pdf_path



def check_isotope_exists(beam_A, beam_isotope, file_path='../HalfLife/HalfLife.txt'):
    # Combine the values to create the desired isotope string
    isotope_to_check = f"{beam_A}{beam_isotope.lower()}"

    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Check for the existence of the isotope in the first column
    for line in lines:
        # Split the line into columns based on whitespace
        columns = line.split()
        if columns and columns[0].lower() == isotope_to_check:
            return True  # Found the isotope

    return False  # Isotope not found





