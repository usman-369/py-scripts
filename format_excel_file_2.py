import pandas as pd

# Load the Excel file
df = pd.read_excel("cleaned_file.xlsx")

# Drop duplicates based on '@message' column
df_unique = df.drop_duplicates(subset="@message", keep="first")

df_unique.to_excel("unique_cleaned_file.xlsx", index=False)

print("Done! File saved as 'unique_cleaned_file.xlsx'")
