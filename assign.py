import atws
import atws.monkeypatch.attributes


from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import json
at = atws.connect(username='<YOUR AUTOTASK USERNAME>',password='<YOUR AUTOTASK PASSWORD>')


@respond_to('(T\d{8}\.\d{4}) assign ([A-Z][a-zA-Z]*) ([A-Z][a-zA-Z]*)')
def assignticket(message, ticket_number, first_name, last_name):
	query = atws.Query('Ticket')
	query.WHERE('TicketNumber',query.Equals,ticket_number)
	ticketnumberquery = at.query(query).fetch_one()
	
	query = atws.Query('Resource')
	query.WHERE('FirstName',query.Equals,first_name)
	
	query.WHERE('LastName',query.Equals,last_name)
	
	personquery = at.query(query).fetch_one()
	
	ticketnumberquery.AssignedResourceID = f'{personquery.id}'
	ticketnumberquery.AssignedResourceRoleID = '29683465'
	ticketnumberquery.update()
	
	attatchments = [{
		'fallback': 'Ticket Assigned',
		'author_name': 'Ticket Assigned',
		'author_link': '',
		'text': ''
		}]
	message.reply_webapi('', json.dumps(attatchments))
	

