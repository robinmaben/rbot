import requests
from BeautifulSoup import BeautifulSoup

pending_links = []
crawled_links = []


def crawl(url):
    print "Getting {}".format(url)
    response = ''
    try:
        response = requests.get(url)
        print 'Response {}'.format(response.status_code)
    except requests.ConnectionError:
        print "Failed {}".format(url)

    pending_links.remove(url)
    crawled_links.append(url)

    links = BeautifulSoup(response.content).findAll("a")

    for link in links:
        try:
            url = link['href']
            add_to_queue(url)
        except KeyError:
            continue


def add_to_queue(link):
    if link not in pending_links:
        pending_links.append(link)


def start_crawling():
    for url in pending_links:
        crawl(url)

    if len(pending_links) < 1000:
        start_crawling()


if __name__ == "__main__":
    pending_links.append('http://yclist.com/')
    start_crawling()
