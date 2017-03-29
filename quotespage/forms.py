from django import forms
from django.forms import extras
from .models import Quote 
import datetime

class NewQuoteForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(NewQuoteForm, self).__init__(*args, **kwargs)
		self.initial['date'] = datetime.date.today()

	class Meta:
		model = Quote
		fields = ['quotation', 'speaker', 'speaker_class', 'context', 'date']
		labels = {
				'quotation' : 'What was said?',
				'speaker' : 'Who said it?',
				'speaker_class' : 'Type of speaker'
		}
		help_texts = {
				'context' : 'Any explanatory context. Start with a lowercase letter, since this will appear after a comma.',
				'quotation' : 'Limited HTML allowed. Possible tags: &lt;p&gt;, &lt;b&gt;, &lt;i&gt;, &lt;u&gt;, &lt;em&gt;, &lt;strong&gt;, &lt;sup&gt;, &lt;sub&gt;, &lt;span&gt;. Newlines will be converted to &lt;br&gt; automatically.' 
		}
		widgets = {
				'date' : extras.widgets.SelectDateWidget(years=range(2000,2020)),
		}

class SearchForm(forms.Form):

	q = forms.CharField(label='Search by Quote or Context', max_length=500)

