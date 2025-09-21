import scipy.io
import pandas as pd
import numpy as np

# Load the MAT file
mat_file = r'C:\Users\patri\OneDrive - Universiti Teknologi PETRONAS\Project\dataset\0Nm_Normal.mat'
mat = scipy.io.loadmat(mat_file)

# Extract 'Signal'
signal_data = mat['Signal']

try:
    # Access structured fields within the 'Signal' data
    start_value = float(signal_data[0][0][0]['start_value'][0][0])
    increment = float(signal_data[0][0][0]['increment'][0][0])
    num_values = int(signal_data[0][0][0]['number_of_values'][0][0])

    # Extract the Pascal values
    pascal_values = signal_data[0][0][1]['values'][0][0].flatten()

    # Generate time series
    time_series = np.linspace(start_value, start_value + increment * (num_values - 1), num_values)

    # Create a DataFrame
    df = pd.DataFrame({
        'TimeStamp': time_series,
        'Pascal_Pa': pascal_values
    })

    # Save to CSV
    csv_file = "0Nm_Normal.csv"
    df.to_csv(csv_file, index=False)

    print(f"CSV export successful: {csv_file}")
    print(f"Number of rows exported: {len(df)}")
    print("Sample data:\n", df.head())

except Exception as e:
    print(f"An error occurred: {e}")
    print("Signal data structure:\n", signal_data)
