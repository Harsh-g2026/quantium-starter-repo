import pandas as pd
import glob

# Step 1: Load all CSV files from data folder
csv_files = glob.glob("data/*.csv")
df_list = [pd.read_csv(f) for f in csv_files]
df = pd.concat(df_list, ignore_index=True)

# Step 2: Filter only Pink Morsel rows
df = df[df["product"] == "pink morsel"]

# Step 3: Create Sales = quantity * price
# (strip $ sign from price if present, convert to float)
df["price"] = df["price"].astype(str).str.replace("$", "", regex=False).astype(float)
df["Sales"] = df["quantity"] * df["price"]

# Step 4: Keep only required columns, rename to match output spec
output_df = df[["Sales", "date", "region"]].rename(
    columns={"date": "Date", "region": "Region"}
)

# Step 5: Save to output CSV
output_df.to_csv("output.csv", index=False)

print("Done. Output saved to output.csv")