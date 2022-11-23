import requests
from bs4 import BeautifulSoup
import csv


def write_to_csv(data):

    with open('enter_nout.csv', 'a') as file:
    
        writer = csv.writer(file)
    
        writer.writerow([data['title'], data['price'], data['img']])


def get_html(url):
    
    response = requests.get(url)
    
    return response.text


def get_total_pages(html):
    
    soup = BeautifulSoup(html,'lxml')
    
    pages = int(soup.find('span', class_ = 'vm-page-counter').text.split()[-1])
    
    return pages

def get_data(html):
    
    soup = BeautifulSoup(html, 'lxml')
    
    product_list = soup.find_all('div', class_='row')
    
    for product in product_list:
    
        title = product.find('span', class_='prouct_name').text
    
        price = product.find('span', class_='price').text
    
        img = 'https://enter.kg/' + product.find('img').get('src')
    
        data = {
            'title': title, 
            'price': price, 
            'img': img
            }
        write_to_csv(data)
def main():
    
    notebooks_url = 'https://enter.kg/computers/noutbuki_bishkek'
    
    html = get_html(notebooks_url)
    
    number = int(get_total_pages(html))
    
    for i in range(1,number+1):
    
        print(i)
     
        if i == 1:
            url = 'https://enter.kg/computers/noutbuki_bishkek'
        else:
            url = 'https://enter.kg/computers/noutbuki_bishkek' +f'/results,{(i-1)*100+1}-{(i-1)*100}'
        get_html(url)       
        get_data(html)
with open('enter_nout.csv', 'w') as file:

    writer = csv.writer(file)

    writer.writerow(['title', 'price', 'img'])

main()