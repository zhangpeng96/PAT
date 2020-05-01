
input_str = '3 4 -5 2 6 1 0 0 1 -1'
# input_str = input()

input_list = list(map(int, input_str.split()))

base_list, exp_list = input_list[::2], input_list[1::2]

result_list = []

for i in range(0, len(base_list)):
    if not exp_list[i]:
        if base_list[i] == 0:
            result_list.extend([0, 0])
        continue
    result_list.extend([base_list[i] * exp_list[i], exp_list[i] - 1])

result_str = ' '.join(map(str, result_list))
print(result_str)
