import atws
import atws.monkeypatch.attributes


from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import json
at = atws.connect(username='<YOUR AUTOTASK USERNAME>',password='<YOUT AUTOTASK PASSWORD>')

#You will likely need to change the status values for your specific company, these values may be determined from the autotask info script.

@respond_to('(T\d{8}\.\d{4}) status escalated', re.IGNORECASE)
def statusescalated(message, ticket_number):
        query = atws.Query('Ticket')
        query.WHERE('TicketNumber',query.Equals,ticket_number)
        ticketnumberquery = at.query(query).fetch_one()
        ticketnumberquery.Status = 39
        ticketnumberquery.update()
        attatchments = [{
                'fallback': 'Status Update',
                'author_name': 'Status updated',
                'author_link': '',
                'text': ''
                }]
        message.reply_webapi('', json.dumps(attatchments))

@respond_to('(T\d{8}\.\d{4}) status scheduled', re.IGNORECASE)
def statusscheduled(message, ticket_number):
        query = atws.Query('Ticket')
        query.WHERE('TicketNumber',query.Equals,ticket_number)
        ticketnumberquery = at.query(query).fetch_one()
        ticketnumberquery.Status = 38
        ticketnumberquery.update()
        attatchments = [{
                'fallback': 'Status Update',
                'author_name': 'Status updated',
                'author_link': '',
                'text': ''
                }]
        message.reply_webapi('', json.dumps(attatchments))

@respond_to('(T\d{8}\.\d{4}) status to be scheduled', re.IGNORECASE)
def statustobescheduled(message, ticket_number):
        query = atws.Query('Ticket')
        query.WHERE('TicketNumber',query.Equals,ticket_number)
        ticketnumberquery = at.query(query).fetch_one()
        ticketnumberquery.Status = 40
        ticketnumberquery.update()
        attatchments = [{
                'fallback': 'Status Update',
                'author_name': 'Status updated',
                'author_link': '',
                'text': ''
                }]
        message.reply_webapi('', json.dumps(attatchments))

@respond_to('(T\d{8}\.\d{4}) status complete', re.IGNORECASE)
def statuscomplete(message, ticket_number):
	query = atws.Query('Ticket')
	query.WHERE('TicketNumber',query.Equals,ticket_number)
	ticketnumberquery = at.query(query).fetch_one()
	ticketnumberquery.Status = 5
	ticketnumberquery.update()
	attatchments = [{
		'fallback': 'Status Update',
		'author_name': 'Status updated',
		'author_link': '',
		'text': ''
		}]
	message.reply_webapi('', json.dumps(attatchments))

@respond_to('(T\d{8}\.\d{4}) status new', re.IGNORECASE)
def statusnew(message, ticket_number):
	query = atws.Query('Ticket')
	query.WHERE('TicketNumber',query.Equals,ticket_number)
	ticketnumberquery = at.query(query).fetch_one()
	ticketnumberquery.Status = 1
	ticketnumberquery.update()
	attatchments = [{
		'fallback': 'Status Update',
		'author_name': 'Status updated',
		'author_link': '',
		'text': ''
		}]
	message.reply_webapi('', json.dumps(attatchments))

@respond_to('(T\d{8}\.\d{4}) status Waiting Customer', re.IGNORECASE)
def statuswaiting(message, ticket_number):
	query = atws.Query('Ticket')
	query.WHERE('TicketNumber',query.Equals,ticket_number)
	ticketnumberquery = at.query(query).fetch_one()
	ticketnumberquery.Status = 7
	ticketnumberquery.update()
	attatchments = [{
		'fallback': 'Status Update',
		'author_name': 'Status updated',
		'author_link': '',
		'text': ''
			}]
	message.reply_webapi('', json.dumps(attatchments))

@respond_to('(T\d{8}\.\d{4}) status In Progress', re.IGNORECASE)
def statusprogress(message, ticket_number):
	query = atws.Query('Ticket')
	query.WHERE('TicketNumber',query.Equals,ticket_number)
	ticketnumberquery = at.query(query).fetch_one()
	ticketnumberquery.Status = 8
	ticketnumberquery.update()
	attatchments = [{
		'fallback': 'Status Update',
		'author_name': 'Status updated',
		'author_link': '',
		'text': ''
		}]
	message.reply_webapi('', json.dumps(attatchments))

#status 1 is new
#status 5 is complete
#status 7 is Waiting Customer
#status 8 is In Progress
