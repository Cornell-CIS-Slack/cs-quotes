from django import forms
from django.template.loader import render_to_string
from django.utils.html import mark_safe

class ApiKeyWidget(forms.widgets.TextInput):
	template_name = "quotespage/api_key_widget.html"

	def render(self, name, value, attrs=None):
		if attrs is None:
			attrs = {}
		attrs['id']="api_key_input"
		attrs['size']="88"
		text_input_html = super(ApiKeyWidget, self).render(name, value, attrs)
		context = {
				'text_input_html' : text_input_html,
		}
		return mark_safe(render_to_string(self.template_name, context))

	class Media:
		js = (
				'quotespage/api_key_button.js',
		)

