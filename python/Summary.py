# === This is code for summarize.py === #

# =========================================== #
# === combine productions among files === #
# === add production activities together === #
def combine_productions(summ):
  sum_prodx_dict = {}
  # Iterate over each element in summ
  for entry in summ:
    production = entry[7]  # The production is the 8th element in each entry of summ

    # Iterate over each row in production
    for row in production:
      A = row[0]           # 'A' value
      isotope = row[1]      # 'Isotope' value
      t_half_value = row[2] # 't1/2_value'
      t_half_unit = row[3]  # 't1/2_unit'
      prodx_A = row[4]      # 'prodx_A'

      # Use (A, isotope) as the key to combine prodx_A values
      key = (A, isotope)
      
      if key in sum_prodx_dict:
        # If the key already exists, sum the prodx_A values
        sum_prodx_dict[key][2] += prodx_A
      else:
        # If the key doesn't exist, create a new entry
        sum_prodx_dict[key] = [t_half_value, t_half_unit, prodx_A]

  # Convert the dictionary back to a list of lists
  sum_prodx = [[A, isotope, values[0], values[1], values[2]] for (A, isotope), values in sum_prodx_dict.items()]
  # Add the header as the first element
  header = ['A', 'Isotope', 't1/2', 'unit', 'Prodx_A(Bq)']
  sum_prodx.insert(0, header)
  
  return sum_prodx



# =========================================== #
# === 1. Separate sum_prodx based on the amount of cd time put in === #
# === 2. Moreover, in each sub new_lists:
# ===== compare A between isotope and its isomer (if it exists)
# ===== remove the one with lower A
# === 3. Remove lines with A = 0
def split_sum_prodx(sum_prodx):
  # Determine how many extra elements exist after the first 5 in sum_prodx[0]
  N = len(sum_prodx[0]) - 5
  
  # Create N lists, each will store the appropriate elements
  new_lists = [[sum_prodx[0][:4] + [sum_prodx[0][5 + i]]] for i in range(N)]
  
  # Loop through each row in sum_prodx (starting from index 1 to skip header)
  for row in sum_prodx[1:]:
    # First 4 elements are common
    common_elements = row[:4]
    
    # Iterate over the new_lists and fill them with the common elements + 1 extra element
    for i in range(N):
      # Copy the first 4 elements
      new_row = common_elements[:]
      # Add the i-th element after the 5th element to the respective list (skip the 5th element)
      new_row.append(row[5 + i])
      # If the Prodx_A(Bq) value is 0, skip adding this row
      if new_row[-1] == 0:
        continue 
      for existing_row in new_lists[i]:
        if existing_row[0] == new_row[0] and existing_row[1].replace('_m', '') == new_row[1].replace('_m', ''):
          # Compare Prodx_A(Bq) values and keep the one with the higher value
          if new_row[-1] > existing_row[-1]:
            existing_row[:] = new_row  # Replace existing row with new_row if new_row has higher value
          break
      else:
        # If no matching isotope is found, append the new row to the list
        new_lists[i].append(new_row)


  return new_lists
