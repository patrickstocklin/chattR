#This should be our Script for Calculations
from collections import OrderedDict
from textblob import TextBlob
import nltk
import praw
import time
import pprint
import sys

def calculateSentiment(sentence):
	try:
		sentenceToParse = TextBlob(sentence)
		print sentence
		polarity = sentenceToParse.sentiment.polarity
		print "Polarity: ", polarity
		subjectivity = sentenceToParse.sentiment.subjectivity
		print "Subjectivity: ", subjectivity
		return (1.5*polarity, 1.5*subjectivity)
	except UnicodeDecodeError as e:
		print "+++++++++++++++++++"
		print "UnicodeDecodeError"
		print "+++++++++++++++++++"
		return (0,0)

def countSyllables(buzzwordDict, word): 
    count = 0
    common_words = ['the','be','to','of','and','a','in','that','have','I','it','for','not','on','with','he',
'as','you','do','at','this','but','his','by','from','they','we','say','her','she','or','an','will','my','one',
'all','would','there','their','what','so','up','out','if','about','who','get','which','go','me','when','make',
'can','like','time','no','just','him','know','take','person','into','year','your','good','some','could','them',
'see','other','than','then','now','look','only','come','its','over','think','also','back','after','use','two',
'how','our','work','first','well','way','even','new','want','because','any','these','give','day','most','us',
'i','is',"it's",'was','are',"don't",'has','been',"he's","she's",'were',"didn't","am","doesn't", "that's",
'should','could','would',"should've","could've","would've",'more','did','everyone','really','too',"i've","i'm",
'much','though','had','why','very',"isn't", "i'd",]
    
    vowels = 'aeiouy'
    #Find out what words are being stripped of all below
    initialWord = word
    word = word.lower().strip(".:;?!,/<>\-*")
        
    if len(word) == 0:
        return 0
    if "http" in word:
        print "+++++++++++++++++++"
        print "Link"
       	print word
        print "+++++++++++++++++++"
        return 1
    #If first letter is a vowel
    if word[0] in vowels:
        count += 1

    for index in range(1, len(word)):
            #Handles compound-vowel syllables
        if word[index] in vowels and word[index-1] not in vowels:
            count += 1
        #handles words like 'scene'
    if word.endswith('e'):
        count -= 1
        #handles words like 'rustle'
    if word.endswith('le'):
        count += 1
        #every word we miss must make a sound
    if count == 0:
        count +=1
    #print word, count
    if word not in common_words and len(word) != 1:
    	if word in buzzwordDict:
    		buzzwordDict[word] += 1
    	else:
    		buzzwordDict[word] = 1
    return count

    #Given a excerpt of text, returns the writing level
def calculateScore(buzzwordDict, writingText):
    #Flesch Grade Level:
    #Calculate the average number of words used per sentence
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    data = writingText
    sample = tokenizer.tokenize(data.decode("utf8"), data)
    totalSentences = len(sample)
    totalWords = 0
    totalSyllables = 0
    for i in range(0, totalSentences):
        sentence = sample[i].split()
        # print "What we want to analyze: "
        # print sample[i]
       	

        numOfWords = len(sentence)
        for j in range(0, numOfWords):
            totalSyllables = totalSyllables + countSyllables(buzzwordDict, sentence[j])
            #Add To Dictionary of Words
        totalWords = totalWords + numOfWords
    try:
    #Flesch Kincaid Grade Level
        score = 0.39*(float(totalWords) / float(totalSentences))+11.8*(float(totalSyllables) / float(totalWords))
        score = score - 15.59
   
    #Flesch Reading Ease:
        Fscore = 206.835 - 1.015*(float(totalWords) / float(totalSentences))
        Fscore = Fscore - 84.6*(float(totalSyllables) / float(totalWords))
    except ZeroDivisionError:
    	print "ZeroDivisionError"
        score = 0
        Fscore = 100
    #206.835 - 1.015(total words / total sentences)
    # - 84.6(total syllables/total words) = Score
    #90-100 - easily understood by 11y/o
    #60-70 - easily understood by 13 - 15 y/o
    #0-30 - best understood by university graduates
    return score

def main(desiredSubreddit):
	r = praw.Reddit("A Scraper Script "
	                "by u/DontKillTheMedic, v 1.0.")
	r.login('WritingLevelBot', '')

	subreddits = [desiredSubreddit]              
	commentList = []
	sub_values = {}
	subredditScore = 0

	buzz_wordsDict = {}
	buzz_words = ""

	alreadyDone = []

	pol=0
	sub=0
	n=0

	for subreddit in subreddits:
	    sr = r.get_subreddit(subreddit)
	    writingscore = 0
	    n = 0
	    try:
	        for submission in sr.get_hot(limit=5):
	            print "Thread: ", submission.title
	            thread = submission.comments
	            for comment in thread:
	                if isinstance(comment, praw.objects.MoreComments):
	                    pass
	                else:
	                    if comment.body == "[deleted]":
	                        #print "DELETED"
	                        pass
	                    elif comment not in commentList and comment.body.encode('utf8') not in alreadyDone:
	                        commentList.append(comment)
	                        writingscore = writingscore + calculateScore(buzz_wordsDict, comment.body.encode('utf8'))
	                        sentimentTup = calculateSentiment(comment.body.encode('utf8'))
	                        pol += sentimentTup[0]
	                        sub += sentimentTup[1]
	                        n+=1
	                        alreadyDone.append(comment.body.encode('utf8'))
	                        print "Appended Comment ", comment.body.encode('utf8')
	                        for leaf in comment.replies:
	                            if isinstance(leaf, praw.objects.MoreComments):
	                                pass
	                            elif leaf not in commentList and leaf.body.encode('utf8') not in alreadyDone:
	                            	commentList.append(leaf)
	                                writingscore = writingscore + calculateScore(buzz_wordsDict, leaf.body.encode('utf8'))
	                                sentimentTup = calculateSentiment(comment.body.encode('utf8'))
	                                pol += sentimentTup[0]
	                                sub += sentimentTup[1]
	                                n+=1
	                                alreadyDone.append(leaf.body.encode('utf8'))
	                                print "Appended Leaf ", leaf.body.encode('utf8')
	                            else:
	                            	print "REPEAT"
	        #print writingscore, n
	        subScore = writingscore / n
	        print subScore
	        print pol, sub
	        print n

	        pol = pol / n
	        sub = sub / n

	        print pol, sub

	        sub_values[subreddit] = subScore
	        subredditScore = subScore
	    except IOError as e:
	        print "IOError"
	        time.sleep(5)
	    except praw.errors.HTTPException as e:
	        print "HTTPException" 
	        time.sleep(5)
	                
	buzz_wordsDict = OrderedDict(sorted(buzz_wordsDict.items(), key=lambda t: t[1], reverse=True))                
	print buzz_wordsDict
	counter = 0

	for item, val in buzz_wordsDict.iteritems():
		try:
			buzz_words = buzz_words + str(item) + " (" + str(val) + "), "
			counter += 1
			if counter == 30:
				break
		except UnicodeEncodeError as e:
			print "Unicode Encode Error"
			pass
	return round(subredditScore, 2), buzz_words, round(pol, 2), round(sub, 2), n
