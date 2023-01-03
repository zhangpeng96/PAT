





### 犯过的错误

#### 多次提交部分结果失败

返回结果不对，`Your password needs shu zi`缺少一个半角句号。

```python
		if count['digit'] == 0 and count['alpha']:
			return 'Your password needs shu zi'
		if count['digit'] and count['alpha'] == 0:
```
