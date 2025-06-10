import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url ="https://quotes.toscrape.com/"
    response =requests.get(url)
    soup =BeautifulSoup(response.content,'html.parser')
    quotes =[]
    for quote in soup.find_all('div',class_='quote'):
        text=quote.find('span',class_='text').text
        author=quote.find('small',class_='author').text
        quotes.append({'text':text,'author':author})
       
    return quotes

def save_to_file(quotes,filename="quotes.txt"):
      with open(filename,"w",encoding='utf-8') as file:
            for quote in quotes:
                file.write(str(quote)+"\n")


quotes =scrape_quotes()
print (quotes)
save_to_file(quotes,"newquotes.txt")

    
 
