from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

def soup_sort():
    with open("capitoltrades_content_with_js.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")

    rows = soup.find_all("tr", class_="border-b transition-colors hover:bg-neutral-100/50 data-[state=selected]:bg-neutral-100 dark:hover:bg-neutral-800/50 dark:data-[state=selected]:bg-neutral-800 h-14 border-primary-15")
    
    # Loop through each row and extract relevant details
    for row in rows:
        # Politician's Name
        name_tag = row.find("h2", class_="politician-name")
        politician_name = name_tag.get_text(strip=True) if name_tag else None
        
        # Politician's Info (party, chamber, state)
        info_tag = row.find("div", class_="politician-info")
        party = info_tag.find("span", class_="party").get_text(strip=True) if info_tag.find("span", class_="party") else None
        chamber = info_tag.find("span", class_="chamber").get_text(strip=True) if info_tag.find("span", class_="chamber") else None
        state = info_tag.find("span", class_="us-state-compact").get_text(strip=True) if info_tag.find("span", class_="us-state-compact") else None
        
        # Traded Issuer
        issuer_tag = row.find("div", class_="q-fieldset issuer-info")
        traded_issuer = issuer_tag.find("h3", class_="issuer-name").get_text(strip=True) if issuer_tag.find("h3", class_="issuer-name") else None
        
        # Transaction Date
        trade_date_tag = row.find_all("td")[2].find("div", class_="text-size-3 font-medium")
        trade_date = trade_date_tag.get_text(strip=True) if trade_date_tag else None
        trade_year_tag = row.find_all("td")[2].find("div", class_="text-size-2 text-txt-dimmer")
        trade_year = trade_year_tag.get_text(strip=True) if trade_year_tag else None
        transaction_date = f"{trade_date} {trade_year}" if trade_date and trade_year else None
        
        # Transaction Type
        tx_type_tag = row.find("span", class_="tx-type")
        transaction_type = tx_type_tag.get_text(strip=True) if tx_type_tag else None

        # Transaction Amount
        #<span class="mt-1 text-size-2 text-txt-dimmer hover:text-foreground">
        tx_amount_tag = row.find("span", class_="mt-1 text-size-2 text-txt-dimmer hover:text-foreground")
        transaction_amount = tx_amount_tag.get_text(strip=True) if tx_amount_tag else None

        # Display the extracted information
        print(f"Politician Name: {politician_name}")
        print(f"Party: {party}")
        print(f"Chamber: {chamber}")
        print(f"State: {state}")
        print(f"Traded Issuer: {traded_issuer}")
        print(f"Transaction Date:   {transaction_date}")
        print(f"Transaction Type:   {transaction_type}")
        print(f"Transaction Amount: {transaction_amount}")
        print("\n" + "-"*40 + "\n")
    return rows

def get_webpage_content_with_js(url, wait_time=10, use_brave=False):
   
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to the URL
        driver.get(url)

        # Wait for a specific element to be present, indicating the page has loaded
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
        )
        time.sleep(5)

        # Get the page source after JavaScript execution
        content = driver.page_source

        # Print the first 1000 characters of the content
        # print("\nFirst 1000 characters of the webpage content:")
        # print(content[:1000])

        with open('capitoltrades_content_with_js.html', 'w', encoding='utf-8') as f:
            f.write(content)
        # print("\nFull content has been saved to 'capitoltrades_content_with_js.html'")

    finally:
        driver.quit()

# URL of the webpage
url = "https://www.capitoltrades.com/trades?chamber=senate&pageSize=24"
## TODO this is kinda slow i want to find a better option
get_webpage_content_with_js(url, use_brave=False)
trades = soup_sort()
print(f"{rows[1]}")