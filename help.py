
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import json

@respond_to('help')
def help(message):
	attachments = [{
		'I can help you': 'I have found a Ticket sire...',
		'author_name': '*AUTOBOT COMMAND LIST*',
		'author_link': '',
		'text': 'Below is a list of commands AUTOBOT can recieve',
		'mrkdwn_in': ['author_name','fields'],
		'fields': [
			{
			'title': 'Ticket Search',
			'value': '@AUTOBOT _ticketnumber_',
			'mrkdwn': "true"
			},
			{
			'title': 'Phonenumber Search',
			'value': '@AUTOBOT 5556667777 (no special characters)'
			},
			{
			'title': 'Update Notes',
			'value': '@AUTOBOT _ticketnumber_ "notes in quotes"',
			'mrkdwn': "true"
			},
			{
			'title': 'Update Status',
			'value': '@AUTOBOT _ticketnumber_ status _status_',
			'mrkdwn': "true"
			},
			{
			'title': 'Update Queue',
			'value': '@AUTOBOT _ticketnumber_ queue _queue_',
			'mrkdwn': "true"
			},
			{
			'title': 'Update Priority',
			'value': '@AUTOBOT _ticketnumber_ priority _priority_',
			'mrkdwn': "true"
			}
			],
		'color': '#59afe1'
		}]
	message.reply_webapi('', json.dumps(attachments))

		
		
		
