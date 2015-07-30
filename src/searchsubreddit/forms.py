from django import forms
from .models import SearchBox

class SearchBoxForm(forms.ModelForm):
	class Meta:
		model = SearchBox
		fields = ['Peek']

		#Must be named after a field of our Model
	def clean_Peek(self):
		print self.cleaned_data
		print self.cleaned_data.get('Peek')
		searchterm = self.cleaned_data.get('Peek')
		if searchterm[:3] == '/r/':
			print "/r/ Format"
			subreddit = searchterm[3:]
			print subreddit
		elif searchterm[:2] == 'r/':	
			subreddit = searchterm[2:]
			print "Another Format"
			print subreddit
		elif searchterm[:1] == '/':
			print "A Third Format"
			subreddit = searchterm[1:]
			print subreddit
		elif '/' not in searchterm:
			print "A Fourth Format"
			subreddit = searchterm
			print subreddit
		else:
			raise forms.ValidationError("Please enter the subreddit correctly")

		return subreddit