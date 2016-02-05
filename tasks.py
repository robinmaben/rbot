import requests
from repo import *
import slack_client
from BeautifulSoup import BeautifulSoup


def crawl(url):
    print "Getting {}".format(url)
    response = ''
    pending_links.remove(url)
    try:
        if url not in crawled_links:
            response = requests.get(url)
            # TODO: Use RobotsTxtAwareSession https://pypi.python.org/pypi/requests-robotstxt

            print 'Response {}'.format(response.status_code)
    except:
        print "Failed {}".format(url)

    crawled_links.append({'url': url,
                          'page': response.content if response else ''})

    if response:
        extract_urls_from_response(url, response)


# Job
def extract_urls_from_response(url, response):
    links = BeautifulSoup(response.content).findAll("a")
    for link in links:
        try:
            href = link['href']
            url_to_add = "{}{}".format(url, href) if len(href) > 0 and href[0] == '/' else href
            add_to_queue(url_to_add)
        except KeyError:
            continue


# Job
def analyze_pages():
    for url, page in crawled_links:
        print "Analyzing - ", url, len(page)
        matches = BeautifulSoup(page).findAll("a", text=["hiring", "career", "join us", "work at", "work with"])
        if len(matches) > 0:
            print "Found possible career page", matches
            possible_career_pages.append(page)


# Job
def analyze_career_pages():
    pass
    # Check if url content has email or mailto link


# Job
def report_findings():
    slack_client.send_message()


# Job
def start_crawling(depth):
    print "Starting Crawl to depth of ", depth
    for level in range(0, depth):
        while len(pending_links) > 0:
            crawl(pending_links[0])
