# r-bot
Simple, low-ceremony crawler to find pages of interest based on provided keywords and starting points - and report them to a Slack message / channel.


### Algorithm -
	
	CrawlList = []
	InterestingList = []
	
	StartingPoints = []
	
	Launch(depth):
	
	    for level in depth:
	        Crawl()
	
	    Collect():
	
	Reset():
	    # Add/Update StartingPoints to CrawlList
	    # Reset all crawled pages metadata
	
	Crawl():
	    for page in CrawlList:
	        Save page content and metadata
	
	        urls = Fetch URLs()
	        for url in urls:
	            if not in CrawlList:
	            CrawlList.append(url)
	
	
	Collect():
	    for page in CrawlList
	        analysis = Analyze(page)
	        if analysis.is_interesting:
	            Add or update InterestingList
	
	
	Analyze(page):
	    # Conditions
	    # key words
	
	
	Relaunch():
	    #
