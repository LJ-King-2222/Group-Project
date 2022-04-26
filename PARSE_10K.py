# %% https://sec-api.io/docs/sec-filings-item-extraction-api
# Very Important: Register and get an api code/key
import numpy as np
import contextlib
from sec_api import ExtractorApi
# %% Very important: Register and get an api key!!!

# extractorApi = ExtractorApi("Your-API-Code/Key")

extractorApi = ExtractorApi ('dbe7f7eaba6c4d7dcdf59689dc060d96b9fbc2c71428f7681ac0dfbfed1e03b1')

filing_urls = "https://www.sec.gov/ix?doc=/Archives/edgar/data/0001318605/000095017022000796/tsla-20211231.htm"



# %% get the standardized and cleaned text of section 1A "Risk Factors"
section_text = extractorApi.get_section(filing_urls, "7", "text")


print(section_text)

with open('C:\\Users\\LJone\\Fin510\\EDGAR\\10k_txt', 'w') as f:
    f.writelines(section_text)
    




