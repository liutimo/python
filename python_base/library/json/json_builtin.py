import json

if __name__ == '__main__':
    data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
    print(json.dumps(data))
    
    data = '[1, 2, 3]'
    l = json.loads(data)
    print(l)
    print(type(l))

    data = (1, 2, 3)
    print(json.dumps(data))

    dict = {1 : 2, 2 : 3}
    print(json.dumps(dict))