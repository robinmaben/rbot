import sys

from repo import add_to_queue
from tasks import start_crawling

MAX_DEPTH = 4

if __name__ == "__main__":
    starting_link = sys.argv[1] if len(sys.argv) > 1 else "yclist.com"
    depth_to_crawl = int(sys.argv[2]) if len(sys.argv) > 2 else MAX_DEPTH

    add_to_queue(starting_link)
    start_crawling(depth_to_crawl)
