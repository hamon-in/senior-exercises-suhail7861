import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote

def download_image(url, directory):
    response = requests.get(url)
    if response.status_code == 200:
        # Extract filename from the URL
        parsed_url = urlparse(url)
        filename = os.path.basename(unquote(parsed_url.path))
        filepath = os.path.join(directory, filename)
        
        # Save the image
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {url}")

def scrape_images(url, directory):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        image_elements = soup.find_all('img', class_='gallery-asset__thumb')

        if not os.path.exists(directory):
            os.makedirs(directory)

        for image_element in image_elements:
            image_url = image_element['src']
            download_image(image_url, directory)
    else:
        print(f"Failed to fetch images from: {url}")

if __name__ == "__main__":
    url = "https://www.gettyimages.in/photos/aamir-khan-actor"
    download_directory = "images"
    
    scrape_images(url, download_directory)
