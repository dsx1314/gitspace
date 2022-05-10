import json

import jsonpath as jsonpath
def get_text(key):
    data = {'name':'dsx','age':18,'sex':'男','student':{'grade':1,'teacher':'dsx'}}

    print(type(data))
    a = json.dumps(data,ensure_ascii=False)
    print(a)

    print(json.loads(a))
    value = jsonpath.jsonpath(data,'$..{0}'.format(key))

    print(value)


if __name__ == '__main__':
    get_text('teacher')