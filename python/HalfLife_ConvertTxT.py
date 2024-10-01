#=============================================#
# Convert Halflife pdf file to txt file
#=============================================#

from miniCodes import *

pdf_path = get_pdf_file_input("Enter half-life pdf file path: ")

def Convert_PDF_to_TXT(pdf_path, flag_overwrite = False):
    # Get the base name of the PDF file (without the extension) using string operations
    base_name = pdf_path.split('/')[-1].replace('.pdf', '')
    # Create the output TXT file name
    txt_path = pdf_path.replace('.pdf', '.txt')
    
    # if txt file exists and don't need to be replaced, return empty
    if os.path.exists(txt_path) and flag_overwrite:
        return
    # if txt file doesn't exist or you want to overwrite it
    else:
        # Open the PDF file
        with pdfplumber.open(pdf_path) as pdf:
            text_to_write = []
            capture_text = False # will be "True" when detect "Nucleus E level(keV) Jπ T 1/2" where start extracting info
            # Iterate through each page
            for page in pdf.pages:
                # Extract the text from the page
                text = page.extract_text() 
                # Split the text into lines
                lines = text.split('\n')
                for line in lines:
                    # Skip the unwanted header and footer lines
                    #if "page" in line.lower() and "," in line and ("AM" in line or "PM" in line):
                    if "AM" in line or "PM" in line:
                        continue
                    if "https://www.nndc.bnl.gov" in line:
                        continue     
                    # Start capturing text after the target start line
                    if "Nucleus E level(keV) Jπ T 1/2" in line:
                        capture_text = True
                        continue
                    # Stop capturing text after the target end line
                    if "Gamma Information" in line:
                        capture_text = False
                        continue
                    if "≥" in line or ">" in line:
                        continue
                    if "eV" in line:
                        continue
                    # Capture the text
                    if capture_text:
                        text_to_write.append(line)
        # Write the captured text to the dynamically named txt file
        with open(txt_path, "w") as output_file:
            output_file.write("\n".join(text_to_write))

#===========================================================================================================#









