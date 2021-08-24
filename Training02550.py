from bs4 import BeautifulSoup
import requests
import re
import csv



bbc = requests.get('https://www.bbc.com/news').text##getting the html from source site

Scrap = BeautifulSoup(bbc, 'lxml')

csv_file = open('WebScraper1.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Titles_list', 'URL_list', 'category_list'])



Titles_list = []
URL_list = []
category_list = []

for block in Scrap.find_all('div',class_='nw-c-top-stories'):
      
    #getting articles titles
    for title in block.find_all('h3', class_='gs-c-promo-heading__title'):
      #display article title
        NewsTitle = title.contents[0]
        Titles_list.append(NewsTitle)
    
      
      
      
    
    #getting articles URLs
    for link in block.find_all('a', class_= 'gs-c-promo-heading'):
      # display article urls
      #if 'sport' not in link.get('href') and 'twitter' not in link.get('href') and 'facebook' not in link.get('href') and 'instagram' not in link.get('href'):
        URL = link['href']
        URL_list.append(URL)
    print(URL_list)
        
        
    
    
    #getting article category
    for category in block.find_all('a', class_ = 'gs-c-section-link'):
        Ccategory = category.span.text
        category_list.append(Ccategory)
    
    for i in range(0,17):
        csv_writer.writerow([Titles_list[i], URL_list[i],category_list[i]])
    
     


#print(Titles_list)
#print(URL_list)
#print(category_list)

 



#AuthorList = []
ArticleList = [] 
for URL in URL_list:
   #ArticleList = [] 
    Article = requests.get('https://www.bbc.com'+URL).text
    scrap2 = BeautifulSoup(Article, 'lxml')
    TextList = []
    
    
    for Text1 in scrap2.find_all('div', class_= 'ssrcss-18snukc-RichTextContainer e5tfeyi1'):
        TextList.append(Text1.text)  
    ArticleList.append(TextList)
print(ArticleList[5])





#AuthorList = []  
    #for author in scrap2.find_all('p', class_ = 'ssrcss-1gg9z89-Contributor'): 
  
   #print(author.strong.text)
  
     #   try:
      #      AuthorList.append(author.strong.text)
  
       # except Exception as e:
        #    AuthorList.append("Not Mentioned")
  
#dprint(AuthorList)
#print(URL_list)
csv_file.close()