import atws
import atws.monkeypatch.attributes


from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import json
at = atws.connect(username='<YOUR AUTOTASK USERNAME>',password='<YOUR AUTOTASK PASSWORD>')

#You will need to modify the list below to allow this phone search example to work. You must use the autotask info script to discover what values correspond to what service level, you may simply remove all references to this list as well, replace with ''
#OR delete this list and replace all instances of list5[accountnumberquery.KeyAccountIcon] with '' or 'some information'

list1 = [0] * 7
list2 = ['Jeopardy', 0, 0, 0, 0,'Time and Materials', 'Residential', 'Jeopardy', 'MSP Gold', 'Residential MSP', 'Tier One MSP']
list3 = [0] * 182
list4 = ['Community Partner', ' no longer a client', 'inactive business client', 'Vendor', 'DO NOT PROVIDE SERVICE UNTIL PAY', 'inactive residential', 'Non Profit']
list5 = list1 + list2 + list3 + list4

@respond_to('search (\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
def autotask(message, rawphonenumber):
	string = "rawphonenumber"
	''.join(e for e in string if e.isalnum())
	#convention (555) 111 2222
	def main():
		phoneNumber=int(rawphonenumber)
		tempNumber = []
		phoneNumber = str(phoneNumber)
		length = len(phoneNumber)
		index=0

		for num in phoneNumber:     # string to list conversion by iteration
			tempNumber.append(num)

		tempNumber.insert(0,"(")
		tempNumber.insert(4,")")
		tempNumber.insert(5," ")
		tempNumber.insert(9," ")
		phoneNumber = ''.join(tempNumber)

		query = atws.Query('Account')
		query.WHERE('Phone',query.Equals,phoneNumber)
		accountnumberquery = at.query(query).fetch_one()
		if accountnumberquery == None:
			#convention (555)-111-2222
			def main2():
				phoneNumber=int(rawphonenumber)
				tempNumber = []
				phoneNumber = str(phoneNumber)
				length = len(phoneNumber)
				index=0

				for num in phoneNumber:     # string to list conversion by iteration
					tempNumber.append(num)

				tempNumber.insert(0,"(")
				tempNumber.insert(4,")")
				tempNumber.insert(5,"-")
				tempNumber.insert(9,"-")
				phoneNumber = ''.join(tempNumber)

				query = atws.Query('Account')
				query.WHERE('Phone',query.Equals,phoneNumber)
				accountnumberquery = at.query(query).fetch_one()
				if accountnumberquery == None:
					#convention (555) 111-2222
					def main3():
						phoneNumber=int(rawphonenumber)
						tempNumber = []
						phoneNumber = str(phoneNumber)
						length = len(phoneNumber)
						index=0
	
						for num in phoneNumber:     # string to list conversion by iteration
							tempNumber.append(num)

						tempNumber.insert(0,"(")
						tempNumber.insert(4,")")
						tempNumber.insert(5," ")
						tempNumber.insert(9,"-")
						phoneNumber = ''.join(tempNumber)

						query = atws.Query('Account')
						query.WHERE('Phone',query.Equals,phoneNumber)
						accountnumberquery = at.query(query).fetch_one()
						if accountnumberquery == None:
							#conventin 555-111-2222
							def main4():
								phoneNumber=int(rawphonenumber)
								tempNumber = []
								phoneNumber = str(phoneNumber)
								length = len(phoneNumber)
								index=0
	
								for num in phoneNumber:     # string to list conversion by iteration
									tempNumber.append(num)

								tempNumber.insert(3,"-")
								tempNumber.insert(7,"-")
								phoneNumber = ''.join(tempNumber)

								query = atws.Query('Account')
								query.WHERE('Phone',query.Equals,phoneNumber)
								accountnumberquery = at.query(query).fetch_one()
								if accountnumberquery == None:
									##convention (555)111-2222
									def main5():
										phoneNumber=int(rawphonenumber)
										tempNumber = []
										phoneNumber = str(phoneNumber)
										length = len(phoneNumber)
										index=0
	
										for num in phoneNumber:     # string to list conversion by iteration
											tempNumber.append(num)

										tempNumber.insert(0,"(")
										tempNumber.insert(4,")")
										tempNumber.insert(8,"-")
										phoneNumber = ''.join(tempNumber)

										query = atws.Query('Account')
										query.WHERE('Phone',query.Equals,phoneNumber)
										accountnumberquery = at.query(query).fetch_one()
										if accountnumberquery == None:
											##convention (555)-111 2222
											def main6():
												phoneNumber=int(rawphonenumber)
												tempNumber = []
												phoneNumber = str(phoneNumber)
												length = len(phoneNumber)
												index=0
	
												for num in phoneNumber:     # string to list conversion by iteration
													tempNumber.append(num)

												tempNumber.insert(0,"(")
												tempNumber.insert(4,")")
												tempNumber.insert(5,"-")
												tempNumber.insert(9," ")
												phoneNumber = ''.join(tempNumber)

												query = atws.Query('Account')
												query.WHERE('Phone',query.Equals,phoneNumber)
												accountnumberquery = at.query(query).fetch_one()
												if accountnumberquery == None:
													##convention 555 111 22222
													def main7():
														phoneNumber=int(rawphonenumber)
														tempNumber = []
														phoneNumber = str(phoneNumber)
														length = len(phoneNumber)
														index=0
	
														for num in phoneNumber:     # string to list conversion by iteration
															tempNumber.append(num)

														tempNumber.insert(3," ")
														tempNumber.insert(7," ")
														phoneNumber = ''.join(tempNumber)

														query = atws.Query('Account')
														query.WHERE('Phone',query.Equals,phoneNumber)
														accountnumberquery = at.query(query).fetch_one()
														if accountnumberquery == None:
															##convention 555 111-2222
															def main8():
																phoneNumber=int(rawphonenumber)
																tempNumber = []
																phoneNumber = str(phoneNumber)
																length = len(phoneNumber)
																index=0
	
																for num in phoneNumber:     # string to list conversion by iteration
																	tempNumber.append(num)

																tempNumber.insert(3," ")
																tempNumber.insert(7,"-")
																phoneNumber = ''.join(tempNumber)

																query = atws.Query('Account')
																query.WHERE('Phone',query.Equals,phoneNumber)
																accountnumberquery = at.query(query).fetch_one()
																if accountnumberquery == None:
																	#convention 5551112222
																	def main9():
																		query = atws.Query('Account')
																		query.WHERE('Phone',query.Equals,rawphonenumber)
																		accountnumberquery = at.query(query).fetch_one()
																		if accountnumberquery == None:
																			#convention 555111 2222
																			def main10():
																				phoneNumber=int(rawphonenumber)
																				tempNumber = []
																				phoneNumber = str(phoneNumber)
																				length = len(phoneNumber)
																				index=0
	
																				for num in phoneNumber:     # string to list conversion by iteration
																					tempNumber.append(num)

																			
																				tempNumber.insert(6," ")
																				phoneNumber = ''.join(tempNumber)

																				query = atws.Query('Account')
																				query.WHERE('Phone',query.Equals,phoneNumber)
																				accountnumberquery = at.query(query).fetch_one()
																				if accountnumberquery == None:
																					#convention 555 1112222
																					def main11():
																						phoneNumber=int(rawphonenumber)
																						tempNumber = []
																						phoneNumber = str(phoneNumber)
																						length = len(phoneNumber)
																						index=0
	
																						for num in phoneNumber:     # string to list conversion by iteration
																							tempNumber.append(num)

																			
																						tempNumber.insert(3," ")
																						phoneNumber = ''.join(tempNumber)

																						query = atws.Query('Account')
																						query.WHERE('Phone',query.Equals,phoneNumber)
																						accountnumberquery = at.query(query).fetch_one()
																						if accountnumberquery == None:
																							#convention (555)1112222
																							def main12():
																								phoneNumber=int(rawphonenumber)
																								tempNumber = []
																								phoneNumber = str(phoneNumber)
																								length = len(phoneNumber)
																								index=0
	
																								for num in phoneNumber:     # string to list conversion by iteration
																									tempNumber.append(num)

																			
																								tempNumber.insert(0,"(")
																								tempNumber.insert(4,")")
																								phoneNumber = ''.join(tempNumber)

																								query = atws.Query('Account')
																								query.WHERE('Phone',query.Equals,phoneNumber)
																								accountnumberquery = at.query(query).fetch_one()
																								if accountnumberquery == None:
																									#convention (555)111 2222
																									def main13():
																										phoneNumber=int(rawphonenumber)
																										tempNumber = []
																										phoneNumber = str(phoneNumber)
																										length = len(phoneNumber)
																										index=0
	
																										for num in phoneNumber:     # string to list conversion by iteration
																											tempNumber.append(num)

																			
																										tempNumber.insert(0,"(")
																										tempNumber.insert(4,")")
																										tempNumber.insert(8," ")
																										phoneNumber = ''.join(tempNumber)
	
																										query = atws.Query('Account')
																										query.WHERE('Phone',query.Equals,phoneNumber)
																										accountnumberquery = at.query(query).fetch_one()
																										if accountnumberquery == None:
																											#convention (555) 1112222
																											def main14():
																												phoneNumber=int(rawphonenumber)
																												tempNumber = []
																												phoneNumber = str(phoneNumber)
																												length = len(phoneNumber)
																												index=0
	
																												for num in phoneNumber:     # string to list conversion by iteration
																													tempNumber.append(num)

																			
																												tempNumber.insert(0,"(")
																												tempNumber.insert(4,")")
																												tempNumber.insert(5," ")
																												phoneNumber = ''.join(tempNumber)
	
																												query = atws.Query('Account')
																												query.WHERE('Phone',query.Equals,phoneNumber)
																												accountnumberquery = at.query(query).fetch_one()
																												if accountnumberquery == None:
																													#convention 555-1112222
																													def main15():
																														phoneNumber=int(rawphonenumber)
																														tempNumber = []
																														phoneNumber = str(phoneNumber)
																														length = len(phoneNumber)
																														index=0
	
																														for num in phoneNumber:     # string to list conversion by iteration
																															tempNumber.append(num)

																			
																														tempNumber.insert(3,"-")
																														phoneNumber = ''.join(tempNumber)
	
																														query = atws.Query('Account')
																														query.WHERE('Phone',query.Equals,phoneNumber)
																														accountnumberquery = at.query(query).fetch_one()
																														if accountnumberquery == None:
																															#convention 555111-2222
																															def main16():
																																phoneNumber=int(rawphonenumber)
																																tempNumber = []
																																phoneNumber = str(phoneNumber)
																																length = len(phoneNumber)
																																index=0
	
																																for num in phoneNumber:     # string to list conversion by iteration
																																	tempNumber.append(num)

																			
																																tempNumber.insert(6,"-")
																																phoneNumber = ''.join(tempNumber)
	
																																query = atws.Query('Account')
																																query.WHERE('Phone',query.Equals,phoneNumber)
																																accountnumberquery = at.query(query).fetch_one()
																																if accountnumberquery == None:
																																	#convention 555-1112222
																																	def main17():
																																		phoneNumber=int(rawphonenumber)
																																		tempNumber = []
																																		phoneNumber = str(phoneNumber)
																																		length = len(phoneNumber)
																																		index=0
	
																																		for num in phoneNumber:     # string to list conversion by iteration
																																			tempNumber.append(num)

																			
																																		tempNumber.insert(3,"-")
																																		phoneNumber = ''.join(tempNumber)
	
																																		query = atws.Query('Account')
																																		query.WHERE('Phone',query.Equals,phoneNumber)
																																		accountnumberquery = at.query(query).fetch_one()
																																		if accountnumberquery == None:
																																			#convention 555-111 2222
																																			def main18():
																																				phoneNumber=int(rawphonenumber)
																																				tempNumber = []
																																				phoneNumber = str(phoneNumber)
																																				length = len(phoneNumber)
																																				index=0
	
																																				for num in phoneNumber:     # string to list conversion by iteration
																																					tempNumber.append(num)

																			
																																				tempNumber.insert(3,"-")
																																				tempNumber.insert(7," ")
																																				phoneNumber = ''.join(tempNumber)
	
																																				query = atws.Query('Account')
																																				query.WHERE('Phone',query.Equals,phoneNumber)
																																				accountnumberquery = at.query(query).fetch_one()
																																				if accountnumberquery == None:
																																					#convention (555)-1112222
																																					def main19():
																																						phoneNumber=int(rawphonenumber)
																																						tempNumber = []
																																						phoneNumber = str(phoneNumber)
																																						length = len(phoneNumber)
																																						index=0
	
																																						for num in phoneNumber:     # string to list conversion by iteration
																																							tempNumber.append(num)

																			
																																						tempNumber.insert(0,"(")
																																						tempNumber.insert(4,")")
																																						tempNumber.insert(5,"-")
																																						phoneNumber = ''.join(tempNumber)
	
																																						query = atws.Query('Account')
																																						query.WHERE('Phone',query.Equals,phoneNumber)
																																						accountnumberquery = at.query(query).fetch_one()
																																						if accountnumberquery == None:
																																							message.reply("This phone number is not in AutoTask", in_thread=True)
																																						else:
																																							attatchments = [{
																																								'fallback': 'I have found a Phone Number...',
																																								'author_name': accountnumberquery.AccountName,
																																								'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
																																								'text': list5[accountnumberquery.KeyAccountIcon],
																																								'color': '#59afe1'
																																								}]
																																							message.reply_webapi('', json.dumps(attatchments))
																																					main19()
																																				else:
																																					attatchments = [{
																																						'fallback': 'I have found a Phone Number...',
																																						'author_name': accountnumberquery.AccountName,
																																						'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
																																						'text': list5[accountnumberquery.KeyAccountIcon],
																																						'color': '#59afe1'
																																						}]
																																					message.reply_webapi('', json.dumps(attatchments))
																																			main18()
																																		else:
																																			attatchments = [{
																																				'fallback': 'I have found a Phone Number...',
																																				'author_name': accountnumberquery.AccountName,
																																				'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
																																				'text': list5[accountnumberquery.KeyAccountIcon],
																																				'color': '#59afe1'
																																				}]
																																			message.reply_webapi('', json.dumps(attatchments))
																																	main17()
																																else:
																																	attatchments = [{
																																		'fallback': 'I have found a Phone Number...',
																																		'author_name': accountnumberquery.AccountName,
																																		'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
																																		'text': list5[accountnumberquery.KeyAccountIcon],
																																		'color': '#59afe1'
																																		}]
																																	message.reply_webapi('', json.dumps(attatchments))
																															main16()
																														else:
																															attatchments = [{
																																'fallback': 'I have found a Phone Number...',
																																'author_name': accountnumberquery.AccountName,
																																'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
																																'text': list5[accountnumberquery.KeyAccountIcon],
																																'color': '#59afe1'
																																}]
																															message.reply_webapi('', json.dumps(attatchments))
																													main15()
																												else:
																													attatchments = [{
																														'fallback': 'I have found a Phone Number...',
																														'author_name': accountnumberquery.AccountName,
																														'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
																														'text': list5[accountnumberquery.KeyAccountIcon],
																														'color': '#59afe1'
																														}]
																													message.reply_webapi('', json.dumps(attatchments))
																											main14()
																										else:
																											attatchments = [{
																												'fallback': 'I have found a Phone Number...',
																												'author_name': accountnumberquery.AccountName,
																												'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
																												'text': list5[accountnumberquery.KeyAccountIcon],
																												'color': '#59afe1'
																												}]
																											message.reply_webapi('', json.dumps(attatchments))
																									main13()
																								else:
																									attatchments = [{
																										'fallback': 'I have found a Phone Number...',
																										'author_name': accountnumberquery.AccountName,
																										'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
																										'text': list5[accountnumberquery.KeyAccountIcon],
																										'color': '#59afe1'
																										}]
																									message.reply_webapi('', json.dumps(attatchments))
																							main12()
																						else:
																							attatchments = [{
																								'fallback': 'I have found a Phone Number...',
																								'author_name': accountnumberquery.AccountName,
																								'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
																								'text': list5[accountnumberquery.KeyAccountIcon],
																								'color': '#59afe1'
																								}]
																							message.reply_webapi('', json.dumps(attatchments))
																					main11()
																				else:
																					attatchments = [{
																						'fallback': 'I have found a Phone Number...',
																						'author_name': accountnumberquery.AccountName,
																						'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
																						'text': list5[accountnumberquery.KeyAccountIcon],
																						'color': '#59afe1'
																						}]
																					message.reply_webapi('', json.dumps(attatchments))
																			main10()
																		else:
																			attatchments = [{
																				'fallback': 'I have found a Phone Number...',
																				'author_name': accountnumberquery.AccountName,
																				'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
																				'text': list5[accountnumberquery.KeyAccountIcon],
																				'color': '#59afe1'
																				}]
																			message.reply_webapi('', json.dumps(attatchments))
																	main9()
																else:
																	attatchments = [{
																		'fallback': 'I have found a Phone Number...',
																		'author_name': accountnumberquery.AccountName,
																		'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
																		'text': list5[accountnumberquery.KeyAccountIcon],
																		'color': '#59afe1'
																		}]
																	message.reply_webapi('', json.dumps(attatchments))
															main8()
														else:
															attatchments = [{
																'fallback': 'I have found a Phone Number...',
																'author_name': accountnumberquery.AccountName,
																'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
																'text': list5[accountnumberquery.KeyAccountIcon],
																'color': '#59afe1'
																}]
															message.reply_webapi('', json.dumps(attatchments))
													main7()
												else:
													attatchments = [{
														'fallback': 'I have found a Phone Number...',
														'author_name': accountnumberquery.AccountName,
														'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
														'text': list5[accountnumberquery.KeyAccountIcon],
														'color': '#59afe1'
														}]
													message.reply_webapi('', json.dumps(attatchments))
											main6()
										else:
											attatchments = [{
												'fallback': 'I have found a Phone Number...',
												'author_name': accountnumberquery.AccountName,
												'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
												'text': list5[accountnumberquery.KeyAccountIcon],
												'color': '#59afe1'
												}]
											message.reply_webapi('', json.dumps(attatchments))
									main5()
								else:
									attatchments = [{
										'fallback': 'I have found a Phone Number...',
										'author_name': accountnumberquery.AccountName,
										'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
										'text': list5[accountnumberquery.KeyAccountIcon],
										'color': '#59afe1'
										}]
									message.reply_webapi('', json.dumps(attatchments))
							main4()
						else:
							attatchments = [{
								'fallback': 'I have found a Phone Number...',
								'author_name': accountnumberquery.AccountName,
								'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
								'text': list5[accountnumberquery.KeyAccountIcon],
								'color': '#59afe1'
								}]
							message.reply_webapi('', json.dumps(attatchments))
					main3()
				else:
					attatchments = [{
						'fallback': 'I have found a Phone Number...',
						'author_name': accountnumberquery.AccountName,
						'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
						'text': list5[accountnumberquery.KeyAccountIcon],
						'color': '#59afe1'
						}]
					message.reply_webapi('', json.dumps(attatchments))
			main2()
		else:
			attatchments = [{
				'fallback': 'I have found a Phone Number...',
				'author_name': accountnumberquery.AccountName,
				'author_link': f'https://ww5.autotask.net/Autotask/AutotaskExtend/ExecuteCommand.aspx?Code=OpenAccount&Phone={accountnumberquery.Phone}',
				'text': list5[accountnumberquery.KeyAccountIcon],
				'color': '#59afe1'
				}]
			message.reply_webapi('', json.dumps(attatchments))
	main()
