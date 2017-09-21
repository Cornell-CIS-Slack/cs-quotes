from django_cron import CronJobBase, Schedule
from django.core.mail import mail_admins
from quotespage.models import Quote

class AdminApprovalEmailJob(CronJobBase):
	RUN_EVERY_MINS = 1440
	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'quotespage.approval_email_job'
	email_template = ('Hello Administrator,\n\n'
			'There are {num_quotes} quote(s) awaiting moderator approval. You can approve them here:\n'
			'\nhttps://quotes.cs.cornell.edu/admin/quotespage/quote/\n\n'
			'Sincerely,\nThe Quotes Page\n')

	def do(self):
		unapproved_quotes = Quote.objects.filter(approved=False)
		if unapproved_quotes.exists():
			mail_admins('Quotes awaiting moderation', self.email_template.format(num_quotes=len(unapproved_quotes)))
