from bs4 import BeautifulSoup
import requests

def parse():
    html_text = requests.get('https://www.olx.ua/d/list/?search%5Bfilter_enum_price%5D%5B0%5D=free').text
    soup = BeautifulSoup(html_text, 'lxml')
    sale = soup.find_all('div', class_="css-19ucd76")
    print(len(sale))
    print(sale)
    cats = ['кот', 'котёнок', 'кошка', 'котята', 'мес', 'собака', 'щенок', "Пёсик"]
    for i in sale:
        title = i.find('h6', class_="css-v3vynn-Text eu5v0x0").text
        #if all(not x in cats for x in title):
            date_city = i.find('p', class_='css-p6wsjo-Text eu5v0x0').text
            link = i.a['href']
    #link_text = link.get('href')


            print(f'Post: {title}\nDate and city: {date_city}\nLink: https://olx.ua{link}\n')





if __name__ == '__main__':
    parse()
