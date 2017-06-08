from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq

my_url = "http://www.supremenewyork.com/shop/all"

# this is just urlopen we just renamed it

# opens the connection
uClient = uReq(my_url)
html = uClient.read()
uClient.close()

#soup is just BeautifulSoup

#html parsing
soup = BeautifulSoup(html, "html.parser")
# print(page_soup.body.span)

# finding the clothing piece, item-container is the name of the class
containers = soup.findAll("div", {"class":"inner-article"})

# print(containers[0])
# available_list = []



# Item object
class Item:
    def __init__(self, name, link):
      self.name = name
      self.link = link

    def displayItem(self):
      print (self.name + ":  " + self.link)

# Stores all the items
all_items = [];

# it just go through the html tree
for container in containers:
    item = container.a


    temp = item.div #this will detect the sold out

    # if the division is not present then it will add it to the availble item list
    if temp == None:
        available_url = item["href"] #variables of only available
        available_item_url = "http://supremenewyork.com" + available_url

        # opens the connection
        uClient2 = uReq(available_item_url)
        html2 = uClient2.read()
        uClient2.close()

        #html parsing
        soup2= BeautifulSoup(html2, "html.parser")

        # find the div with name
        containers2 = soup2.find("div", {"id":"details"})
        available_item_name = containers2.h1.get_text()
        available_item_color = containers2.p.get_text();

        if(available_item_color != None):
            available_item_name = containers2.h1.get_text() + "(" + available_item_color + ")"

        all_items.append(Item(available_item_name, available_item_url))

for i in all_items:
    i.displayItem()


print("done")
