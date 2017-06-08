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

# finding the graphics cards, item-container is the name of the class
containers = soup.findAll("div", {"class":"inner-article"})

# print(containers[0])
available_list = []

# Item object
class Item:
    def __init__(self, name, link):
      self.name = name
      self.link = link

    def displayItem(self):
      print ("Name : " + self.name + " Link: " + self.link)

item1 = Item("Fuck", "google.com")
item1.displayItem()

# it just go through the html tree
# for container in containers:
#     item = container.a
#
#     # item_url = item["href"]
#
#     temp = item.div #this will detect the sold out
#
#     # if the division is not present then it will add it to the availble item list
#     if temp == None:
#         if item["href"] not in available_list:
#             available_list.append(item["href"])
#             available_url = item["href"] #variables of only available
#             available_item = "http://supremenewyork.com" + available_url
#             # print(available_item)


print("done")
