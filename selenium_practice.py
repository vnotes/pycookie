from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.baidu.com/')
    driver.close()
