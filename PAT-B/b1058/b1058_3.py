import re

def key_map(record):
	temp = record.split()
	return {
		'score': int(temp[0]),
		'keys': set(temp[3:])
	}

def main():
	# answer_count, ins_count = list(map(int, input().split()))
	answer_count, ins_count = [3,4]
	key_list = []
	error_dict = dict(zip(range(0, ins_count), [0]*ins_count))

	for ins in range(0, ins_count):
		key_list.append(key_map(input()))

	ins_list = []

	for i in range(0, answer_count):
		ins_list.append(input())

	score_list = [0] * len(ins_list)
	for n, ins in enumerate(ins_list):
		answer_list = re.findall(r'\((.*?)\)', ins)
		for i, answer in enumerate(answer_list):
			if key_list[i]['keys'] == set(answer.split()[1:]):
				score_list[n] += key_list[i]['score']
			else:
				error_dict[i] += 1

	for i in score_list:
		print(i)

	error_dict = sorted(error_dict.items(), key = lambda x:(-x[1], x[0]))
	error_count_max = error_dict[0][1]
	if error_count_max:
		error_str = str(error_dict[0][0] + 1)
		for i in error_dict:
			if i[1] == error_count_max:
				error_str += ' ' + str(i[0] + 1)
		print(error_str)
	else:
		print('Too simple')


if __name__ == '__main__':
	main()