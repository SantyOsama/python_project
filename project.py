import bs4
import requests
import csv

title = []
time = []
link = []
desc = []

for i in range(1, 500, 1):
    url = "https://getintopc.com/page/" + str(i) + "/"
    page = requests.get(url)
    # print(page.content)
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    # print(soup)
    title.insert(len(title), soup.find_all("h2", {"class": "title"}))
    time.insert(len(time), soup.find_all("span", {"class": "ext"}))
    link.insert(len(link), soup.find_all("div", {"class": "post-info"}))
    desc.insert(len(desc), soup.find_all("div", {"class": "post-content clear-block"}))

# print(soup.find_all("div"))
# print(title[0][1].get_text())
# print(time[0][1].get_text())
# print(link[0][1].get_text())
# print(desc[0][1].get_text())

rows = []
for i in range(0, 499, 1):
    for j in range(1, 6, 1):
        rows.insert(len(rows), [title[i][j].get_text(), time[i][j].get_text(),
                                link[i][j].get_text(), desc[i][j].get_text()])
        dic1 = {"title": title[i][j].get_text(), "time": time[i][j].get_text(), "link": link[i][j].get_text(),
                "describtion": desc[i][j].get_text()}
        print(dic1)
fields = ["title", "time", "link", "desc"]
filename = "abc.text"
# writing to csv file
with open("abc.text", 'w', encoding="utf-16") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerows(rows)