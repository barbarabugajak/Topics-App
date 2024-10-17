import requests
from bs4 import BeautifulSoup
from .models import Category, Topic

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
        urls = []
        for title in titles:
            # Get the href of the title
            data.append(title.get_text().strip())
            href = title.get('href')
            urls.append(f"{url}{href}")

        return data, urls
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None


def scrape():
    data_cnn = scrape_cnn()[0]
    urls_cnn = scrape_cnn()[1]
    try:
        news, created = Category.objects.get_or_create(pk=1)
        print(news)
    except Exception as e:
        print(f"Failed to create a category: {e}")
    for i in range(len(data_cnn)):
        try:
            topic, created = Topic.objects.get_or_create(name=data_cnn[i], link=urls_cnn[i], category=news, language="English")
            if created:
                topic.save()
        # Exceptin as e
        except Exception as e:
            print(f"Failed to create a topic: {e}")
    print(Topic.objects.all())
    return True

scrape()