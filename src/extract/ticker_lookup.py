import requests



HEADERS={
    "User-Agent":"DataPipelineProject mengeshacalu123@gmail.com"
}
def get_company_cik(ticker):
    url="https://www.sec.gov/files/company_tickers.json"

    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()

    companies = response.json()

    
    ticker=ticker.strip().upper()

    #Search for the company
    for company in companies.values():
        if company["ticker"] == ticker:
            return str(company["cik_str"]).zfill(10)
    
    return None



