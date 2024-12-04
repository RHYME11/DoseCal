import numpy as np
import pdfplumber
import os
import re
from pathlib import Path
#=========================================================================#
#============= Following mini codes are called in main.py ============#
#=========================================================================#

#=======================================#
# Check if input contains letters only 
#=======================================#
def get_alpha_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isalpha():
            return user_input
        else:
            print("Warning: Please enter letters only (no numbers or special characters).")

#=======================================#
# Function to validate integer input
#=======================================#
def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Warning: Please enter a valid number!")

#=======================================#
# Function to validate float input
#=======================================#
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

#=======================================#
# Check input exists or not
# Check input is .pdf file
#=======================================#
def get_pdf_file_input(prompt):
    while True:
        pdf_path = input(prompt)
        
        # Check if the file exists
        if not os.path.exists(pdf_path):
            print(f"Warning: {prompt} does not exist. Please enter a valid file path.")
            continue
        
        # Check if the file is a PDF by checking its extension
        if not pdf_path.lower().endswith('.pdf'):
            print(f"Warning: {prompt} is not a PDF. Please enter a valid PDF file.")
            continue
        
        # If both checks pass, return the file path
        return pdf_path


#=======================================#
# Check is input is an existing isotope
# Separate A and Name for two inputs
#=======================================#
def check_isotope_exists(beam_A, beam_isotope, file_path='HalfLife/HalfLife.dat'):
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


#=============================================================#
#============= convert all half-lives to seconds =============#
#=============================================================#
def HalfLife_Unit_Factor(unit):
    fac = 0
    if unit == "s":
        fac = 1;
    if unit == "m":
        fac = 60;
    if unit == "h":
        fac = 60*60;
    if unit == "d":
        fac = 24*60*60;
    if unit == "y":
        fac = 365*24*60*60;
    return fac

#=============================================================#
#============= convert seconds to different time unit =============#
#=============================================================#
def Time_Seconds_Unit(seconds):
    if seconds >= 31536000:
      unit = 'y'
      if seconds%3153600 == 0:
        time = int(seconds%3153600)
      else:
        time = round(float(seconds/3153600),1)
    elif seconds >= 86400:
      unit = 'd'
      if seconds%86400 == 0:
        time = int(seconds/86400)
      else:  
        time = round(float(seconds/86400),1)
    elif seconds >= 3600:
      unit = 'h'
      if seconds%3600 == 0:
        time = int(seconds/3600)
      else:
        time = round(float(seconds/3600),1)
    elif seconds >= 60:
      unit = 'm'
      if seconds%60 == 0:
        time = int(seconds/60)
      else:
        time = round(float(seconds/60),1)
    else:
      unit = 's'
      time = int(seconds)
    return time, unit
