# DoesCal

## HalfLife.txt
1. Include all isotopes (and isomers) with half-life > 1 second;
2. Values from NNDC (Gamma Search);
3. If a new .txt file is required, please follow the steps:
   1. Go to Nuclear Levels and Gammas Search;
   2. Give the range for Z or A or N to search the result (I usually set half-life range > 1 sec);
   3. Save the result page as PDF (Right click -> choose print -> Save as PDF);
   4. Run code "HalfLife_File_Convert.py"
   
   * No space in any path
   
4. If extra info needs to be added in the existing file or a new txt file needs to be generated, please keep the format:

   |  Isotope   | Level  | $J^{\pi}$  | $t_{1/2}$ value | $t_{1/2}$ unit | error (optional) |
   |------------|--------|----------|---------------|--------------|------------------|
   | 108In      | 0      | 7+       | 39.6          | m            | 7                |




## Folder DoesParFiles:
* Contain 5 txt files for "Body Unshield", "Body Shield", "Skin Unshield", "Skin Shield" and "Breath". <\br>
* Value source from 2 PDF files also contained in this folder. <\br>
* Specific values for parameters (such as, distance and unit) marked at top in each file.
* If extra parameters values needed, please generate txt file with same format "A" "Isotope" "DoesPar"
