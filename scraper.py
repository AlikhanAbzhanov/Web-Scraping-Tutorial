from bs4 import BeautifulSoup
import re

with open("index.html", errors="ignore") as file:
    src = file.read()

# print(src)

soup = BeautifulSoup(src, "lxml")

# title = soup.title

# print(title)
# print(title.text)
# print(title.string)

# page_h1 = soup.find("h1")

# print(page_h1)

# page_all_h1 = soup.find_all("h1")

# print(page_all_h1)

# for i in page_all_h1:
    # print(i.text)

# user_name = soup.find("div", class_="user__name")

# print(user_name.text.strip())

# user_name = soup.find("div", class_="user__name").find("span").text

# print(user_name)

# user_name = soup.find("div", {"class": "user__name", "id": "aaa"}).find("span").text

# print(user_name)

# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")

# print(find_all_spans_in_user_info)
# print(find_all_spans_in_user_info[0])
# print(find_all_spans_in_user_info[1].text)

# for i in find_all_spans_in_user_info:
#     print(i.text)

# social_links = soup.find(class_="social__networks").find("ul").find_all("a")

# print(social_links)

# all_a = soup.find_all("a")

# print(all_a)

# for i in all_a:
#     text = i.text
#     url = i.get("href")

#     print(f"{text}: {url}")

# post_div = soup.find(class_="post__text").find_parent()

# print(post_div)

# post_div = soup.find(class_="post__text").find_parent("div", "user__post")

# print(post_div)

# post_divs = soup.find(class_="post__text").find_parents("div", "user__post")

# print(post_divs)

# next_el = soup.find(class_="post__title").next_element.next_element.text

# print(next_el)

# next_el = soup.find(class_="post__title").find_next().text

# print(next_el)

# next_sib = soup.find(class_="post__title").find_next_sibling()

# print(next_sib)

# prev_sib = soup.find(class_="post__date").find_previous_sibling()

# print(prev_sib)

# post_title = soup.find(class_="post__date").find_previous_sibling().find_next().text

# print(post_title)

links = soup.find(class_="some__links").find_all("a")

# print(links)

# for link in links:
#     link_href_attr = link.get("href")
#     link_href_attr1 = link["href"]

#     link_data_attr = link.get("data-attr")
#     link_data_attr1 = link["data-attr"]

#     print(link_href_attr)
#     print(link_data_attr)

#     print(link_href_attr1)
#     print(link_data_attr1)

# find_a_by_text = soup.find("a", text="Shop")

# print(find_a_by_text)

# find_all_shops = soup.find_all(text=re.compile("([Ss]hop)"))

# print(find_all_shops)
