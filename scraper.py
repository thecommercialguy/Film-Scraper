from bs4 import BeautifulSoup
import requests 
import re  # Regular expression module



# A method for ensuring each movie title returns a properly formatted link that the 
# scraper can access to retrieve data
def page_obtain(title: str):
    # title = 'The Dark Knight'
    # title_1 = 'The GodFather'

    search = f'https://www.themoviedb.org/search?query={title}&language=en-US'

    search_result = requests.get(search).text
    
    doc = BeautifulSoup(search_result, "html.parser")

    link_rel = doc.find("a", class_="result")['href']

    if link_rel:
        link = f"https://www.themoviedb.org{link_rel}"
        print(link)
        return link
        
    
    else:
        return ValueError
   

# Return the properly formatted link from the first wikipedia search term
def get_film_page(doc: BeautifulSoup):

    result = doc.find("div", class_="mw-search-results-container")

    link = result.find("a")['href']

    if link:
        return f"https://en.wikipedia.org{link}"
    
    else:
        return TypeError




def scrape_data(url):
    # url = 'https://en.wikipedia.org/wiki/Spider-Man_(2002_film)'
    # url = 'https://en.wikipedia.org/wiki/The_English_Patient_(film)'
    result = requests.get(url)
    text = result.text

    movie = {
        'title': None,
        'director': None,
        'release': None,
        'genre': None
    }



    # Psycho (1960)

    doc = BeautifulSoup(text, "html.parser")

    primary_content = doc.find("section", class_="header poster")

    title = primary_content.find("div", class_="title").a.text
    if title:
        movie['title'] = title

    release_raw = primary_content.find("span", class_="release").text
    if release_raw:
        release_formatted = release_raw.strip()[:10]
        movie['release'] = release_formatted

    genres = primary_content.find("span", class_="genres").find_all("a")
    if genres:
        genres_list = []
        for genre in genres:
            genres_list.append(genre.text)
        
        movie['genre'] = genres_list

    profiles = primary_content.find_all("li", class_="profile") 
    for profile in profiles:
        children = profile.find_all("p")
        sibling = False
        for i in range(len(children)):
            if 'Director' in children[i].text:
                # print(children[i].text)
                sibling = True
        
        if sibling:
            director = children[0].a.text
            if director:
                movie['director'] = director
                break
        

    # print(movie)


    return movie

db_link = ''
            
movies = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Blink Twice",
    "The Hunger Games",
    "The Substance",
    "Killers of the Flower Moon",
    "Barbie",
    "Forrest Gump",
    "Fight Club",
    "Inception",
    "The Matrix",
    "The Empire Strikes Back",
    "Twisters",
    "We Live In Time",
    "Challengers",
    # "City of God",
    "It's What's Inside",
    "Joker: Folie à Deux",
    "Spirited Away" 
]

movies_list = []

title = 'The Dark Knight'
title_1 = 'The GodFather'
title_2 = 'Barbie Movie'
title_3 = 'Zootopia'
title_4 = 'Pearl'

for movie in movies:
    link = page_obtain(movie)
    mObj = scrape_data(link)
    print(mObj)
    movies_list.append(mObj)



# for m in movies_list:
#     print(m)

# url = 'http://localhost:5200/api/Movie'
# res = requests.get('http://localhost:5200/api/Movie')

# print(requests.get('https://www.themoviedb.org/movie/933260-the-substance?language=en-US').status_code)
# to_Update = res.json()

u = page_obtain('Blink Twice')

scrape_data(u)

toUpdateArr = []

# for update in to_Update:
#     toUpdateArr.append(update['title'])


# for movie in toUpdateArr:
#     link = page_obtain(movie)
#     mObj = scrape_data(link)
#     movies_list.append(mObj)



# for m in movies_list:
#     print(m)



# link = page_obtain(title_4) 
# print(link)
# scrape_data(link)

# Genres

# print(title)




# tbody = doc.tbody
# trs = tbody.contents

# prices = {}

# for tr in trs:
#     name, price = tr.contents[2:4]
#     if price.span:
#         prices[name.p.string] = price.span.string





# print(list(trs[0].children))  # initailly return an iterable generator object


 
# .find()
# .find_all()

# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")

# tag = doc.find("option")


# Finding text containing "$"
# Find what the text is following the "$"

# tags = doc.find_all("input", type="text")
# for tag in tags:
#     tag['placeholder'] = "I CHANGE YOU" # Reassiging placeholder attribute value

# with open("changed.html", "w") as file:
#     file.write(str(doc))

# print(tags)  # Printing the modified HTML result

# [print(f"{i}: {t}\n") for i, t in enumerate(tags)]

# url ="https://www.areenpc.com/product-page/asus-nvidia-geforce-rtx-4080-super-tuf-gaming"
# result = requests.get(url)

# doc = BeautifulSoup(result.text, "html.parser")

# prices = doc.find_all(string="$")
# parent = prices[0].parent


# print(parent.find_all("span")[0].text)

# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")

# tags = doc.find_all
# print(tags[1])    