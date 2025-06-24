import pandas as pd
import json
import sys
import os

# Create outputs directory
os.makedirs("outputs", exist_ok=True)

# Get input file from command line
input_file = sys.argv[1] if len(sys.argv) > 1 else "metadata_sample.xlsx"
df = pd.read_excel(input_file)

# Clean column names
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# RACI Matrix Export
raci_cols = ['object', 'owner', 'accountable', 'consulted', 'informed']
raci_df = df[raci_cols].drop_duplicates()
raci_df.to_csv("outputs/raci_matrix.csv", index=False)

# Data Dictionary Export
dict_cols = ['object', 'field_name', 'data_type', 'owner']
dict_data = df[dict_cols].drop_duplicates().to_dict(orient='records')
with open("outputs/data_dictionary.json", "w") as f:
    json.dump(dict_data, f, indent=2)

# Lineage Export
lineage_cols = ['object', 'field_name', 'source_system', 'target_system']
lineage_data = df[lineage_cols].dropna().drop_duplicates().to_dict(orient='records')
with open("outputs/lineage_mapping.json", "w") as f:
    json.dump(lineage_data, f, indent=2)

print("✅ Outputs generated in /outputs folder")
