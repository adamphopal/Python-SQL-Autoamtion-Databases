import requests
import csv
from bs4 import BeautifulSoup
from ebay_scraper import *




def main():
    csv_file = open('output1.csv', 'w')
    writer = csv.writer(csv_file)
    writer.writerow(['title', 'price', 'currency', 'total sold', 'link'])
    csv_file.close()

    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=mens+watches&_pgn=1'

    products = get_index_data(get_page(url))

    for link in products:
        data = get_detail_data(get_page(link))
        write_csv(data, link)


if __name__ == '__main__':
    main()
