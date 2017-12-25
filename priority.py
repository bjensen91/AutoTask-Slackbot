import atws
import atws.monkeypatch.attributes


from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import json
at = atws.connect(username='<YOUR AUTOTASK USERNAME>',password='<YOUR AUTOTASK PASSWORD>')



@respond_to('(T\d{8}\.\d{4}) priority low', re.IGNORECASE)
def prioritylow(message, ticket_number):
	query = atws.Query('Ticket')
	query.WHERE('TicketNumber',query.Equals,ticket_number)
	ticketnumberquery = at.query(query).fetch_one()
	ticketnumberquery.Priority = 3
	ticketnumberquery.update()
	attatchments = [{
		'fallback': 'Priority Updated',
		'author_name': 'Priority updated',
		'author_link': '',
		'text': ''
		}]
	message.reply_webapi('', json.dumps(attatchments))
	
@respond_to('(T\d{8}\.\d{4}) priority medium', re.IGNORECASE)
def prioritymedium(message, ticket_number):
	query = atws.Query('Ticket')
	query.WHERE('TicketNumber',query.Equals,ticket_number)
	ticketnumberquery = at.query(query).fetch_one()
	ticketnumberquery.Priority = 2
	ticketnumberquery.update()
	attatchments = [{
		'fallback': 'Priority Updated',
		'author_name': 'Priority updated',
		'author_link': '',
		'text': ''
		}]
	message.reply_webapi('', json.dumps(attatchments))

@respond_to('(T\d{8}\.\d{4}) priority high', re.IGNORECASE)
def priorityhigh(message, ticket_number):
	query = atws.Query('Ticket')
	query.WHERE('TicketNumber',query.Equals,ticket_number)
	ticketnumberquery = at.query(query).fetch_one()
	ticketnumberquery.Priority = 1
	ticketnumberquery.update()
	attatchments = [{
		'fallback': 'Priority Updated',
		'author_name': 'Priority updated',
		'author_link': '',
		'text': ''
		}]
	message.reply_webapi('', json.dumps(attatchments))
	
@respond_to('(T\d{8}\.\d{4}) priority critical', re.IGNORECASE)
def prioritycritical(message, ticket_number):
	query = atws.Query('Ticket')
	query.WHERE('TicketNumber',query.Equals,ticket_number)
	ticketnumberquery = at.query(query).fetch_one()
	ticketnumberquery.Priority = 4
	ticketnumberquery.update()
	attatchments = [{
		'fallback': 'Priority Updated',
		'author_name': 'Priority updated',
		'author_link': '',
		'text': ''
		}]
	message.reply_webapi('', json.dumps(attatchments))

		
		
		
