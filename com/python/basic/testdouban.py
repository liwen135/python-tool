import requests
from bs4 import BeautifulSoup

session = requests.session()


def main():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    url = 'https://book.douban.com/top250'
    html = requests.get(url,headers=header).content
    return html

if __name__ == '__main__':
   html = main()
   soup = BeautifulSoup(html, 'html.parser')
   book_list = soup.find('div', attrs={'class': 'article'})
   name = []
   for i in book_list.find_all('table'):
       book_name = i.find('div', attrs={'class': 'pl2'})
       m = list(book_name.find('a').stripped_strings)
       if len(m) > 1:
           x = m[0] + m[1]
       else:
           x = m[0]
       # print(x)
       name.append(x)
   print(name)
   content = session.get('https://book.douban.com/top250').content;
   print(content)