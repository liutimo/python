# Python Json

## dumps
将python对象编码成JSON字符串。

### 语法
```python
json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, 
            indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)
```

### Python对象和json的对应关系
| Python           | JSON   |
| :--------------- | :----- |
| dict             | object |
| list, tuple      | array  |
| str, unicode     | string |
| int, long, float | number |
| True             | true   |
| False            | false  |
| None             | null   |


## loads
### 语法
```python
loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
```

### json和python对象的对应关系

| JSON          | Python    |
| :------------ | :-------- |
| object        | dict      |
| array         | list      |
| string        | unicode   |
| number (int)  | int, long |
| number (real) | float     |
| true          | True      |
| false         | False     |
| null          | None      |

