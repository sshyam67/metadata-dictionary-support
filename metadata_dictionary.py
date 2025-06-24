import pandas as pd

# Load metadata file
df = pd.read_excel("sample_metadata.xlsx")

# Print structure
print("Loaded columns:", df.columns.tolist())

# Show RACI matrix simulation
print("\n--- RACI Simulation ---")
for index, row in df.iterrows():
    print(f"{row['Object']} | Owner: {row['Owner']} | Accountable: {row['Accountable']} | Consulted: {row['Consulted']} | Informed: {row['Informed']}")

# Example: generate a dictionary output for export
metadata_dict = df.to_dict(orient="records")
