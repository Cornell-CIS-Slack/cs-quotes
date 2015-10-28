from django.contrib import admin
from .models import Quote, ApiUser
from .widgets import ApiKeyWidget

admin.site.site_header="CS Quotes Administration"
admin.site.site_title="CS Quotes Admin"
admin.site.index_title="Data Management"


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
	fields=['approved', 'quotation', 'speaker', 'speaker_class', 'context', 'date', 'votes']
	list_display = ('quotation', 'speaker', 'date', 'approved')
	list_filter = ['approved', 'date']
	search_fields = ['quotation', 'speaker']
	actions = ['approve_quotes']

	def approve_quotes(self, request, queryset):
		rows_updated = queryset.update(approved=True)
		if rows_updated == 1:
			prefix = "1 quote was"
		else:
			prefix = "{!s} quotes were".format(rows_updated)
		self.message_user(request, "{!s} successfully approved.".format(prefix))
	approve_quotes.short_description = "Approve selected quotes"	

@admin.register(ApiUser)
class ApiUserAdmin(admin.ModelAdmin):
	fields = ['name','api_key','key_expires']
	list_display = ('name','api_key','key_expires')
	search_fields = ['name']

	def get_form(self, request, obj=None, **kwargs):
		#kwargs is the arguments to be passed to modelform_factory()
		if 'widgets' in kwargs:
			kwargs['widgets']['api_key'] = ApiKeyWidget()
		else:
			kwargs['widgets'] = { 'api_key' : ApiKeyWidget() }
		return super(ApiUserAdmin, self).get_form(request, obj, **kwargs)

