import datetime

def get_date(record, today):
	name, date_str = record.split()
	date = datetime.datetime.strptime(date_str, '%Y/%m/%d').date()
	if date > today:
		return False
	elif date < datetime.date(today.year - 200, today.month, today.day):
		return False
	else:
		# or comparing object directly
		return {name: today.__sub__(date).days}

def main():	
	date_dict = {}
	today = datetime.date(2014, 9, 6)
	count = int(input())
	for i in range(0, count):
		date = get_date(input(), today)
		if date:
			date_dict.update(date)

	date_dict = sorted(date_dict.items(), key = lambda d: d[1], reverse = True)
	print(date_dict)
	
	print(len(date_dict), date_dict[0][0], date_dict[-1][0])

if __name__ == '__main__':
	main()


# Note
	# oss = {'a': today}
	# print(test < today)

	# days = today.__sub__(test).days
	# today = datetime.date.today()