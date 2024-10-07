# DoesCa
---


## Python Libraries Required

The following Python libraries are required to run the current code:

- `numpy`
- `pdfplumber`
- `os` (part of Python's standard library, no need to install)
- `re` (part of Python's standard library, no need to install)
- `pathlib` (part of Python's standard library, no need to install) 


## Files Preparation: 

### HalfLife.txt
1. Include all isotopes (and isomers) with half-life > 1 second;
2. Values from NNDC (Gamma Search);
3. If a new .txt file is required, you can follow steps:
   1. Go to Nuclear Levels and Gammas Search;
   2. Give the range for Z or A or N to search the result (I usually set half-life range > 1 sec);
   3. Save the result page as PDF (Right click -> choose print -> Save as PDF);
   4. Run code "HalfLife_File_Convert.py"
   
   * No space in any path
   
4. If extra info needs to be added in the existing file or a new txt file needs to be generated, please keep the format:

   |  Isotope   | Level  | $J^{\pi}$  | $t_{1/2}$ value | $t_{1/2}$ unit | error (optional) |
   |------------|--------|----------|---------------|--------------|------------------|
   | 108In      | 0      | 7+       | 39.6          | m            | 7                |

### PACE4 Calculation Results
1. Save the result page as PDF (Right click -> choose print -> Save as PDF);
2. Save PACE4 results in PACE4 folder with name formate: {beam_isotope}{beam_A}_{target_isotope}{target_A}_{beam_E}MeV. E.g. "Kr84_Al27_400MeV.pdf"

### Folder DoesParFiles:
* Contain 5 txt files for "Body Unshield", "Body Shield", "Skin Unshield", "Skin Shield" and "Breath". <\br>
* Value source from 2 PDF files also contained in this folder. <\br>
* Specific values for parameters (such as, distance and unit) marked at top in each file.
* If extra parameters values needed, please generate txt file with same format "A" "Isotope" "DoesPar"

---

## Run main.py

### Step1: Fill target and beam information
* Target thickness can be calculated in LISE++ with physics calculator.

### Step2: Read the associated PACE4 PDF file

### Step3: Extract halflife for isotopes from HalfLife.txt

### Step4: Calculations: 
#### Production rate (pps) for each isotope
- Need:
  - xsec in `mb` (read from PACE4 file)
  - target thickness in `mg/cm2` (from input in Step1)
  - target mass in `g` (from input in Step1, will be converted in the code)
    - mass number ~= molar mass
  - beam rate in `pps` (from input in Step1)

#### Activity (Bq) for each isotope

### Step5: Write information into txt file
---


## \*Generate Stopping ratios:
Now, there is no convenient way to generate stopping ratios for all production isotopes, except SRIM which needs to calculate one by one.</br>
Now assume all production will be stopped in the target (stopping_ratio = 1), returning higher radiation dose.</br>
The stopping ratio is not considered in calculations in main.py, but will be generated in txt file which is returned after running main.py</br>
* You can edited it manually in the file, which will effect the future calcualtions in summary.py

---



## Run summarize.py











