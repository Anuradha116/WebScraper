

import scrapy
import requests
from bs4 import BeautifulSoup
from..items import Project1Item
 
 
class  AllListSpider(scrapy.Spider):
    name = 'list1'
    
    start_urls = ['https://websites.co.in/sitemap']
 
    def parse(self, response):
        items = Project1Item()
        data=response.css("table.table a::attr(href)").extract()
    
        counter = 0
        for link in data:
            
            if counter in range(11):
                counter += 1
                url = "https:"+link
                items['url']= url
                try:
                    html = requests.get(url).content
                    soup = BeautifulSoup(html)            
                    #print(url)
                    divWhatsappGoogleMap = soup.select("div.quick-float a")
                    #print(divWhatsappGoogleMap)
                    
                    
                    for div_new in divWhatsappGoogleMap:
                        print(div_new["href"])
                        url_google_whatsapp = div_new["href"]
                        
                        if "phone=" in url_google_whatsapp:
                            
                            startPhoneIndex = url_google_whatsapp.index('phone=')
                            endPhoneIndex = url_google_whatsapp.index('&text')
                            whatsappNum =url_google_whatsapp[startPhoneIndex + 6 : endPhoneIndex]
                            #print(whatsappNum)
                            items['whatsappNum']=whatsappNum
                            

                        else:
                            startMapIndex = url_google_whatsapp.index('q=')   
                            googleLocation= url_google_whatsapp[startMapIndex + 2 : ]             
                        # print(googleLocation)
                            items['googleLocation'] =googleLocation
                            
                            yield items
                except:
                    print("link not accessible: ",url)




                




           
            
  

