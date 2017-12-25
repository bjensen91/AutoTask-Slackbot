# AutoTask-Slackbot
A SlackBot that integrates with AutoTask. 

Use these scripts as plugins for https://github.com/lins05/slackbot to add AutoTask integration
Python 3.6 is required as well as the atws python module available via pip. I HIGHLY reccommend you read the lins05/slackbot README to get the bot up and running FIRST, then add these plugins for AutoTask integration.

To install...

install python 3.6.x

FOR WINDOWS -- https://www.python.org/downloads/ choose any version above 3.6

FOR macOS -- https://www.python.org/downloads/mac-osx/ ^^

For LINUX -- compile from source -- https://www.python.org/downloads/source/ or follow your distro specific guidelines

open a terminal or administrative command prompt...

pip install atws

pip install slackbot


drag your desired scripts into the slackbot/slackbot/plugin folder located where python installs you modules. Alternatively you may clone or download https://github.com/lins05/slackbot and put them into your plugins folder there.
(optional) replace the default "dispatcher.py" with the one provided to allow each slackbot reply to be placed in its own thread as opposed to a general message. I find it to be much better.
If you have any questions DO NOT HESITATE TO EMAIL ME, this is an EXCELLENT first coding project, or fisrt python project. I will do my absolute best to anwser ANY question, related to this project or otherwise.

These plugins (once configured) will do a variety of AutoTask related funcitons...
They may need to be modified slightly to work for your company, see info.py on how to do this.



1) ticket_listen.py
  Listens for any mention of an AutoTask ticket, then replies in slack with an attatchment containing..
    
    A) The title of the ticket that links to the ticket within autotask
    
    B) The name of the company the ticket is for, and a link to the company within autotask
    
    C) A summary of the ticket
    
    D) Who the ticket is assigned to
    
    E) The support level the client is paying for (this will need to be modified for your specific company to work)
    
    F) The color of the attatchment corresponds to the priority of the ticket: Blue = low, Green = medium, Orange = high,       Red = Critical

2) priority.py 
Change the priority of a ticket form slack. to use, call your bot, type priority, followed by what level of priority. @'yourbotsname' priotiry low or medium or high or critical
  
3) assign.py
Assign a ticket to an autotask resource via First and Last name. to use, call your bot, type assign, folled by the first and last name of the autotask resource. @'yourbotsname' assign Fisrtname Lastname

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------The scripts below will need more modification to work for you, all information needed to allow these scripts to funciton will be clearly documented in the script its self.

4)notation.py
add notes to a ticket from slack. To use, call your bot, enter the ticketnumber, then whatever you enter in quotes after that will be added to a note on that ticket. @'yourbotsname' TicketNumber "Whatever in quotes goes in the notes"
  
5)phone_search.py
Search AutoTask for Companies or Contacts via phone-number. To use, call your bot, type search, then enter a 10 digit phone number (do not use special characters). @'yourbotsname' search 11122233333
  
6)queue.py
change a ticket to another Autotask Queue. To use, call your bot, type queue, then type the desired queue. @'yourbotsname' queue yourautotaskqueue

7)status.py
change the status of a ticket via slack. To use, call your bot, type status, then type the desired status. @'yourbotsname' status desired-autotask-status
  
8)help.py
define what your bot can do and how to call its functions.
