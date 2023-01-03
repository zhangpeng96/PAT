







### Python3解题思路与相关问题

#### 数据输入部分

由于这道题是根据输入的数值来循环输入的，因此在用样例测试时不推荐将`input()`替换为指定的字符串，直接将输入完成后列表的赋值写出来更方便：

```python
def main():
	# ins = input()
	ins = '6 6 7'
	divi = list(map(int, ins.split(' ')))
	gp = ['01234 880','a1903 199','ydjh2 200','wehu8 300','dx86w 220','missing 400']
	gmid = ['ydhfu77 99','wehu8 55','ydjh2 98','dx86w 88','a1903 86','01234 39']
	gfinal = ['ydhfu77 88','a1903 66','01234 58','wehu8 84','ydjh2 82','missing 99','dx86w 81']
```

