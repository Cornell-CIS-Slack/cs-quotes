from django.core.management.base import BaseCommand, CommandError
from quotespage.models import Quote
import datetime
import json

class Command(BaseCommand):
	args = '<file>'
	help = 'Loads quotes from a file containing one JSON object per line'
	option_list = BaseCommand.option_list = (
					make_option('--debug',
							action="store_true",
							dest="debug",
							default=False,
							help="Display extra printouts for debugging."
					)

	def handle(self, *args, **options):
		filename = args[0]
		try:
			with open(filename) as file:
				newquotes = []
				for line in file:
					jsobj = json.loads(line)
					try:
						dateparse = datetime.datetime.strptime(jsobj["date"], "%Y-%m-%d")
					except ValueError as err:
						if options['debug']:
							self.stderr.write("Invalid date on this line: " + line)
						raise err
					quote = Quote(date=dateparse,
							speaker=jsobj["speaker"],
							speaker_class=jsobj["speaker_class"],
							quotation=jsobj["quotation"],
							context=jsobj["context"],
							approved=True)
					newquotes.append(quote)
				#if that completed without errors, save them
				for quote in newquotes:
					quote.save()
		except EnvironmentError:
			raise CommandError('Could not open file "' + filename + '"')
		except Exception as ex:
				raise CommandError('Error occurred while loading quotes: ' + str(ex) + '. New quotes not saved.')
