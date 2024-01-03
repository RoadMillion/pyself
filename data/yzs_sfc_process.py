import pandas as pd

def process_excel(file_path, output_path):
    # Load the data
    df = pd.read_excel(file_path, sheet_name=0)

    # Sort and group the dataframe
    sorted_df = df.sort_values(by=['ID'], ascending=False)
    grouped_df = sorted_df.groupby(['END_POINT', 'PORT_ID', 'START_POINT'])

    # Process each group
    for _, group in grouped_df:
        if len(group) > 1:
            indices_to_update = group.index[1:]
            for i in range(len(indices_to_update)):
                current_index = indices_to_update[i]
                previous_index = indices_to_update[i - 1] if i > 0 else group.index[0]
                df.at[current_index, 'EXPIRED_TIME'] = df.at[previous_index, 'EFFECTIVE_TIME']
            df.drop(group.index[0], inplace=True)

    # Save the processed data to a new Excel file
    df.to_excel(output_path, index=False)

# Example usage
file_path = 'path_to_your_input_file.xlsx'  # Replace with your input file path
output_path = 'path_to_your_output_file.xlsx'  # Replace with your desired output file path
process_excel(file_path, output_path)
