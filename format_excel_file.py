import pandas as pd
import json

# Load the Excel file
df = pd.read_excel("apidelaylogs.xlsx")

# print(df.columns.tolist())
# ['traceId', 'name', '@timestamp', 'service', 'environment', 'statusCode', 'responseTimeSec', 'clientIp', 'spanId', '@message']


# Function to extract only 'url.full' key
def extract_url_full(json_str):
    try:
        data = json.loads(json_str)
        url = data.get("attributes", {}).get("url.full")
        if not url:
            url = data.get("resource", {}).get("attributes", {}).get("url.full")
        if not url:
            url = data.get("attributes", {}).get("http.url")
        return {"url.full": url} if url else {}
    except Exception:
        print("Error parsing:", json_str)
        return {}


# Apply the function to '@message' column
df["@message"] = df["@message"].apply(lambda x: json.dumps(extract_url_full(x)))

df.to_excel("cleaned_file.xlsx", index=False)

print("Done! File saved as 'cleaned_file.xlsx'")
