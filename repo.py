# Move these to use Firebase (or MySQL on dev account)
pending_links = []
crawled_links = []

possible_career_pages = []
qualifying_career_pages = []


def add_to_queue(link):
    if link not in pending_links \
            and link not in crawled_links:
        pending_links.append(link)
