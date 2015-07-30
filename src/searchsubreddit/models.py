from django.db import models

# Create your models here.
class SearchBox(models.Model):
	Peek = models.CharField(blank=True, default="e.g. '/r/funny' or 'funny'", max_length=120)

	def __unicode__(self):
		return self.Peek