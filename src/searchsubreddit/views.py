from django.shortcuts import render

from .models import SearchBox
from .forms import SearchBoxForm
#import json as simplejson
#import Scraper Script
import scraper


# Create your views here.
def home(request):
	title = "Title Goes Here"
	Search = SearchBoxForm(request.POST or None)
	score = None
	polarity = None
	subjectivity = None
	buzzwords = None
	queried = False
	numberOfComments = 0
	
	if Search.is_valid():
		print "CALCULATE SUBREDDIT SCORE"
		title = Search.cleaned_data.get('Peek')
		score, buzzwords, polarity, subjectivity, numberOfComments = scraper.main(title)
		title = "/r/" + title
		print score
		queried = True
		Search.save()

	context = {
		"title": title,
		"searchBar": Search,
		"results": score,
		"polarity": polarity,
		"subjectivity": subjectivity,
		"queried": queried,
		"buzzwords": buzzwords,
		"numberOfComments": numberOfComments
	}

	return render(request, "home.html", context)

	#About View
def about(request):
	return render(request, "about.html", {})

def compare(request):
	return render(request, "results.html", {})