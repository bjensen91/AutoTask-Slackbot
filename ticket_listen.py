from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import json


import atws
import atws.monkeypatch.attributes

at = atws.connect(username='<YOUR AUTOTASK USERNAME',password='<YOUR AUTOTASK PASSWORD>')

priority_list = [0, '#ffa500', '#008000', '#59afe1', '#ff4500'] 

#list1 = [0] * 7
#list2 = ['Jeopardy', 0, 0, 0, 0,'Time and Materials', 'Residential', 'Jeopardy', 'MSP Gold', 'Residential MSP', 'Tier 1 MSP']
#list3 = [0] * 182
#list4 = ['Community Partner', ' no longer a client', 'inactive business client', 'Vendor', 'DO NOT PROVIDE SERVICE UNTIL PAY', 'inactive residential']
#list5 = list1 + list2 + list3 + list4

@listen_to('(T\d{8}\.\d{4})')
def autotask(message, ticket_number):
    query = atws.Query('Ticket')
    query.WHERE('TicketNumber',query.Equals,ticket_number)
    ticketnumberquery = at.query(query).fetch_one()
    try: 
        query = atws.Query('Resource')
        query.WHERE('id',query.Equals,ticketnumberquery.AssignedResourceID)
        assignedto = at.query(query).fetch_one()
    except AttributeError:
        query = atws.Query('Account')
        query.WHERE('id',query.Equals,ticketnumberquery.AccountID)
        accountidquery = at.query(query).fetch_one()
        attachments = [{
	        'pretext': f'<https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenTicketDetail&TicketNumber={ticketnumberquery.TicketNumber}|{ticketnumberquery.Title}>',
            'fallback': 'Ticket Found',
            'author_name': accountidquery.AccountName,
            'author_link': f"https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&AccountID={ticketnumberquery.AccountID}",
            'text': ticketnumberquery.Description,
            'fields': [
			    {
			    'title': 'Assigned to',
			    'value': 'Ticket not assigned'
			    },
			    {
			    'title': f'Support level',
			    'value': 'edit the lists to make this work for you' #list5[accountidquery.KeyAccountIcon]
			    }
			],
            'color': priority_list[ticketnumberquery.Priority]
		    }]
        message.reply_webapi('', json.dumps(attachments))
    else:
        query = atws.Query('Account')
        query.WHERE('id',query.Equals,ticketnumberquery.AccountID)
        accountidquery = at.query(query).fetch_one()
        attachments = [{
		    'pretext': f'<https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenTicketDetail&TicketNumber={ticketnumberquery.TicketNumber}|{ticketnumberquery.Title}>',
            'fallback': 'Ticket Found',
            'author_name': accountidquery.AccountName,
            'author_link': f"https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&AccountID={ticketnumberquery.AccountID}",
            'text': ticketnumberquery.Description,
            'fields': [
			    {
			    'title': 'Assigned to',
			    'value': f'{assignedto.FirstName} {assignedto.LastName}'
			    },
			    {
			    'title': 'Support Level',
			    'value': 'edit the lists to make this work for you' #list5[accountidquery.KeyAccountIcon],
			    }
			],
            'color': priority_list[ticketnumberquery.Priority]
		    }]
        message.reply_webapi('', json.dumps(attachments))
