# chattR

Small web-application for subreddit-analysis

Hosted @ www.patstocklin.webfactional.com

This website allows a user to observe what trending topics are currently being discussed and shared on a particular subreddit. After entering a subreddit in mind, the website peeks and reports back with several items: 
	 What is most frequently being talked about (all words are run through a filter of the English language's most common words),
		The average Flesch-Kincaid Grade Level of all recently-commented redditors, and finally,
		The subreddit's averaged 'sentiment', including the subjectivity and polarity of discussions.
	


The Flesch-Kincaid Grade Level is a metric used to gauge an individual's aptitude for writing. The F-K score takes into account a document's total number of words, sentences, and syllables. While it is worth noting that not everybody on Reddit comments under the assumption someone will examine their writing, it is interesting to note the observable discrepencies of writing levels across different communities and their respective subject matters. More can be read on the Flesch-Kincaid Formula here.



For grabbing comments and submissions on Reddit, I used PRAW, the Python Reddit API Wrapper. For language processing and parsing, I used python's Natural Language Toolkit, NLTK. For sentiment analysis, I used python's TextBlob library. A subreddit's sentiment includes both its Polarity, how positive/negative a community's attitude is, and its Subjectivity, how objective/subjective the content of a thread is. For comparison visualization across Reddit's most popular subreddits, I used Bokeh. The website was built using Django 1.8 (Flask probably would have been more well-suited for this exercise) and uses Bootstrap for stylistic purposes.
