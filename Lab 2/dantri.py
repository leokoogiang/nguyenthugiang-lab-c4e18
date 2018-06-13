from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "http://dantri.com.vn"
# 1 Download the webpage

# 1.1 Create a connection
conn = urlopen(url)
# 1.2. Read
data = conn.read()
#print(data)
# 1.3 Decode
html_content = data#.decode("utf-8")
# print(html_content)

# Save html _content to file
# Python 3 input output writing file
# Open a file
# f = open('workfile', 'w')

# f = open('dantri.html', 'wb')
# f.write(html_content)
# f.close()
# Python library for finding html beautifulsoup
# How to use beautifulsoup
# Phần đọc html




# 2 Extract ROI (Raw of interest)
# html, xml, xhtml
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())

ul = soup.find("ul", "ul1 ulnew") # one soup bowl
# print(ul.prettify())
# List spoon of soup bowl
li_list = ul.find_all("li")
records = []
#print(li_list.prettify())
for li in li_list:
    data ={}
    # print(li.prettify())
    # print("*"*20)
    # h4 = li.find("h4")
    # a = h4.find("a")
    # h4 = li.h4
    a = li.h4.a
    data['title'] = a.string
    data['link'] = url + a['href']
    records.append(data)
    print(records)

pyexcel.save_as(records=records, dest_file_name="news.xlsx")

    # print(url + a.string)
    # print(url + a['href'])

   
    # break


    # import pyexcel

    # a_list_of_news= [
    #     {
    #     "Title": a.string,
    #     "Link": a['href']
    #     }
    # ]
    # pyexcel.save_as(records=a_list_of_news, dest_file_name="news.xlsx")
# Gói pyexcel
    # Data type of a: 
    # Một thẻ có nhiều attribute, lưu dưới dạng dictionary
    # Nội dung của href






# Transfer html to the format that BS uses
# Find the content we want, we need to find the features of the content
# The web content has a lot of u(l)
# How to take li out
# There are many li

# 3 Extract the info

