

import yaml

def read():
    with open('F:\\pythonProject1\\dsx3.yaml',mode='r',encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)

        # print(value["token"])
        return value["token"]

def write_yaml_demo(data):
    with open('F:\\pythonProject1\\dsx3.yaml',encoding='utf-8',mode='w') as f:
        yaml.dump(data,stream=f,allow_unicode=True)

def clear():
    with open('F:\\pythonProject1\\dsx3.yaml',mode='w',encoding='utf-8') as f:
        f.truncate()

if __name__ == '__main__':
    # clear()
    read()
    print()
