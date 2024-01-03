import pandas as pd

# Load the data
df = pd.read_excel("../files/a2.xlsx")

# Identify duplicates based on specific columns
duplicate_columns = ["DOOR_AREA_ID", "PRICING_PORT_DISTRICT_ID", "mobilization_wharf_id", "CONTAINER_SIZE_ID", "BOUND_TYPE", "priceType"]

# Keep all duplicates
df_duplicates = df[df.duplicated(subset=duplicate_columns, keep=False)]

# Create a new column 'mark', and set its value to True if the row is not the one with the max id in its group
df_duplicates['max_id'] = df_duplicates.groupby(duplicate_columns)['ID'].transform(max)
df_duplicates['mark'] = df_duplicates['ID'] != df_duplicates['max_id']

# Create a new column 'next_effective_time' and set its value to the 'effective_time' of the next row
df_duplicates['next_effective_time'] = df_duplicates['EFFECTIVE_TIME'].shift(-1)

# In each group, set 'expired_time' of the current row to 'next_effective_time' of the same row, but only for rows where 'mark' is True
df_duplicates['EXPIRED_TIME'] = df_duplicates.loc[df_duplicates['mark'], 'next_effective_time']



# Write the final DataFrame back to an Excel file
df_duplicates.to_excel("../files/a2_result.xlsx", index=False)
