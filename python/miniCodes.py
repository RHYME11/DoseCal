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








