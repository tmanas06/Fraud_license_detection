import pandas as pd

# Load your dataset
df = pd.read_csv('licenses.csv')

# Data Preprocessing
# ...

# Define fraud criteria
df['IsFraud'] = (pd.to_datetime(df['Expiration Date']) < pd.to_datetime('today')) & (df['Current Status'] == 'CUR')

# Function to check fraud status based on user input
def check_fraud():
    # Get user input
    license_number = input("Enter License Number: ")


    # Find the corresponding entry in the dataset
    entry = df[df['License Number'] == license_number]

    # Check if the entry exists and if it's flagged as fraudulent
    if not entry.empty:
        if entry['IsFraud'].values[0]:
            print("This taxi service is flagged as potentially fraudulent.")
        else:
            print("This taxi service is not flagged as fraudulent.")
    else:
        print("No entry found for the provided license number.")

# Call the function to check fraud status
check_fraud()
