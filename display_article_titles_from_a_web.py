import requests

from bs4 import BeautifulSoup

def scrape_blog(url):

    # catch any errors while retrieving 
    try:

        response = requests.get(url)

        response.raise_for_status()

    except requests.exceptions.RequestException as e:

        print(f"Failed to retrieve the page: {e}")

        return

    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('h2')  # Assuming article titles you want are in <h2> tags

    if articles:

        for article in articles:

            print(article.get_text())

    else:

        print("No article titles found on the page.")

if __name__ == "__main__":

    url = input("Enter URL of the blog: ")

    scrape_blog(url)
