import requests
from ticker_lookup import get_company_cik
import json
from pathlib import Path

#get cik ourselves from the input our user give
ticker=input("Enter a ticker symbol: ")

cik=get_company_cik(ticker)

if cik is None:
    print("Ticker not found")
    raise SystemExit

#Construct SEC API URL
url=f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

#Identify our application to the SEC
headers={
    "User-Agent": "DataPipelineProject mengeshacalu123@gmail.com"
}

#Request the data
response=requests.get(url,headers=headers, timeout=30)

#Check the response
print("status code:", response.status_code)

if response.status_code == 200:
    data=response.json()

    print("Company:",data["entityName"])
    print("CIK",data["cik"])
    print("US GAAP concepts:", len(data.get("facts",{}).get("us-gaap",{})))

    
    # Find the main project directory
    project_dir = Path(__file__).resolve().parents[2]

    # Define where to save the raw data
    raw_dir = project_dir / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    # Create the output filename
    filename = raw_dir / f"{ticker.strip().upper()}_companyfacts.json"

    # Save the SEC response
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    print("Financial data saved to:", filename)


else:
    print("Request failed:", response.status_code)
