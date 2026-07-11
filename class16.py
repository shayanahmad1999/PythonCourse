csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# print(','.join(csv.split(';')))
# print(','.join(csv.split(';')).split(':'))
# print(','.join(','.join(csv.split(';')).split(':')))
# print(','.join(','.join(csv.split(';')).split(':')).split(','))

friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)

print("==========OR==========")

print(csv.replace(';', ',').replace(':', ',').split(','))
