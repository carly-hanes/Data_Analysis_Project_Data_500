import pandas as pd

# Load the CSV file
df = pd.read_csv('sample_data.csv')
print("Data loaded successfully!")

# Calculate average session duration by conversion status
average_duration = (
    df.groupby('is_conversion')['session_duration_minutes']
    .mean()
    .reset_index()
)

# Replace numeric 0/1 with descriptive labels
average_duration['is_conversion'] = average_duration['is_conversion'].replace({
    0: 'No Conversion',
    1: 'Converted'
})

print("\nAverage session duration by conversion status:")
print(average_duration)