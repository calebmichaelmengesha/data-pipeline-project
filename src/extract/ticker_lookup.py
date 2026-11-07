import requests



HEADERS={
    "User-Agent":"DataPipelineProject mengeshacalu123@gmail.com"
}
def get_company_cik(ticker):
    url="https://www.sec.gov/files/company_tickers.json"

    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        companies=response.json()
    except requests.exceptions.Timeout:
        print("Error: SEC ticker lookup timed out.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the SEC.")
        return None
    except requests.exceptions.RequestException as error:
        print("Error fetching ticker directory:",error)
        return None
    except ValueError:
        print("Error: Invaldi JSON response from SEC")
        return None



    companies = response.json()

    
    ticker=ticker.strip().upper()

    #Search for the company
    for company in companies.values():
        if company["ticker"] == ticker:
            return str(company["cik_str"]).zfill(10)
    
    return None



