# value = input('Enter a value (# to end input): ')
# items = []
# total = 0

# while value != '#':
# 	items.append(value)
# 	total += int(value)
# 	value = input('Enter a value (# to end input): ')

# print('Average = ', total / len(items))


items = ['39217', '37769', '37493', '37429', '37382', '37084', '36773', '35936', '33679', '33476', '33185', '33068', '32781', '32721', '32304', '32299', '32256', '31916', '31810', '31764', '31460', '31458', '31394', '31221', '31185', '30855', '30830', '30691', '30668', '30630', '30627', '30546', '30531', '30529', '30446', '30228', '30175', '28717', '28575', '28452', '28411', '28383', '28363', '28208', '28118', '28008', '27751', '27652', '27397', '27100', '27073', '27007', '26507', '26292', '26003', '25744', '25677', '25548', '25535', '25520', '25389', '25306', '25212', '24862', '24804', '24645', '24314', '24310', '24147', '24093', '24082', '23870', '23659', '23545', '23528', '23515', '23429', '23306', '23305', '23048', '22931', '22728', '22677', '22631', '22507', '22435', '22279', '22047', '21903', '21770', '21562', '21479', '21464', '21444', '21437', '21314', '20988', '20746', '20703', '20625', '20549', '20317', '19995', '19783', '19401', '19054', '19053', '18855', '18714', '18618', '18425', '18244', '17986', '17722', '16509']
total = 0

for i in items:
	total += int(i)

print('Average = ', total / len(items))