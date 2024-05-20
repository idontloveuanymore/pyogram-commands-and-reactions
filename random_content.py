from bs4 import BeautifulSoup
import requests
import json

def get_funny_cat():
    response = requests.get('https://api.thecatapi.com/v1/images/search?category_ids=6')
    data = json.loads(response.text)
    cat_url = data[0]['url']
    return cat_url

def get_funny_dog():
    response = requests.get('https://api.thedogapi.com/v1/images/search?')
    data = json.loads(response.text)
    dog_url = data[0]['url']
    return dog_url

def get_random_image():
    response = requests.get('https://www.anekdot.ru/random/mem/')
    soup = BeautifulSoup(response.text, 'html.parser')
    image_element = soup.select_one('.topicbox img')
    image_url = image_element['src'] if image_element else None
    return image_url

def get_random_joke():
    response = requests.get('https://www.anekdot.ru/random/anekdot/')
    soup = BeautifulSoup(response.text, 'html.parser')
    joke = soup.select_one('.text').text.strip()
    return joke

if __name__ == '__main__':
    print(get_funny_cat())
    print(get_funny_dog())
    print(get_random_image())
    print(get_random_joke())