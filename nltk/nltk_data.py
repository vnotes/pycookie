import requests
from lxml import etree

if __name__ == '__main__':
    url = 'http://www.nltk.org/nltk_data/'
    rs = requests.get(url).content
    selector = etree.HTML(rs)
    packages = selector.xpath('//packages/package/@url')
    with open('nltk_data.txt', 'a+') as data:
        for package in packages:
            print(package)
            data.write(package + '\n')
