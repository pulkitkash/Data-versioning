import pandas as pd
import os

# create a sample Dataframe with columns names
data = {'Name': ['Pulkit','adi','Disa'],
        'Age': [25,22,13],
        'City': ['Delhi','nangloi','unnao']}

df = pd.DataFrame(data)


# Adding new rows to df for v2
new_row_loc = {'Name': 'GF1','Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc

# Adding new rows to df for v3
#new_row_loc2 = {'Name': 'V3', 'Age': 30, 'City': 'City1'}
#df.loc[len(df.index)] = new_row_loc2

#Ensure the "data" directory exists at the root level


data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the data frame to as csv file, including columns names
df.to_csv(file_path, index=False)

print(f"CSv file save to {file_path}")