
import re
import requests
from bs4 import BeautifulSoup
site = 'https://www.codespeedy.com/'
response = requests.get(site)
soup = BeautifulSoup(response.text, 'html.parser')
image_tags = soup.find_all('img')
urls = [img['src'] for img in image_tags]
for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
         print("Regular expression didn't match with the url: {}".format(url))
         continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)
print("Download complete, downloaded images can be found in current directory!")
from bs4 import *
import requests
import os
def folder_create(images):
    folder_name = input("Enter name of folder: ")
    os.mkdir(folder_name)
    download_images(images, folder_name)
def download_images(images, folder_name):
    count = 0
    print(f"Found {len(images)} images")
    if len(images) != 0:
        for i, image in enumerate(images):
            image_link = image["src"]
            r = requests.get(image_link).content
            with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
                f.write(r)
                count += 1
        if count == len(images):
            print("All the images have been downloaded!")
        else:
            print(f" {count} images have been downloaded out of {len(images)}")
def main(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.findAll('img')
    folder_create(images)
url = input("Enter site URL:")
main(url)