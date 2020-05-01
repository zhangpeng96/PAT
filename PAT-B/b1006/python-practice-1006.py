input_raw = int(input())
# input_raw = 990
number_str = ('{:03d}'.format(input_raw))[::-1]

output_str = ''

output_str += ''.join(['B' for _ in range(0, int(number_str[2]))])
output_str += ''.join(['S' for _ in range(0, int(number_str[1]))])
output_str += ''.join([str(i+1) for i in range(0, int(number_str[0]))])

print(output_str)
