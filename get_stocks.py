import os
from selenium import webdriver


class Scraper:
    def __init__(self):
        dir_path = os.path.dirname(os.getcwd())
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--start-maximized')
        prefs = {"download.default_directory": os.path.join(dir_path, 'temp')}
        options.add_experimental_option("prefs", prefs)
        chromedriver = os.path.join(os.getcwd(), 'chromedriver')
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(options=options, executable_path=chromedriver)


stocks = []
scraper = Scraper().driver

while len(stocks) < 1000:
    scraper.get('https://raybb.github.io/random-stock-picker/')
    stock = (scraper.find_element_by_xpath('//*[@id="ticker"]')).text
    if stock not in stocks:
        stocks.append(stock.upper())

scraper.close()

stock_str = '\n'.join(stocks)

with open('stocks.txt', 'w') as f:
    f.write(stock_str)
