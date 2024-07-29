import requests
from bs4 import BeautifulSoup
from myapp.models import Topic

def scrape_cnn():
    # URL of the website to scrape
    url = 'https://edition.cnn.com'

    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        #container__link container__link--type-article container_ribbon__link container_ribbon__left container_ribbon__light 
        # Find all headlines
        titles = soup.find_all(class_="container__link container__link--type-article container_ribbon__link container_ribbon__left container_ribbon__light")
        # Print the titles
        data = []
        for title in titles:
            data.append(title.get_text().strip())
        return data
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None


def scrape():
    data_cnn = scrape_cnn()
    try:
        news_category = Category.objects.get(name="News")
    except:
        raise Exception("Category 'News' does not exist")
    for topic in data_cnn:
        try:
            user = Topic.objects.get_or_create(name=topic, link="#", category=news_category, language="English")
        except:
            pass
    return True
    