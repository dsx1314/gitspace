import yaml


def write_yaml_demo(data):
    with open('F:\\pythonProject1\\dsx3.yaml',encoding='utf-8',mode='w') as f:
        yaml.dump(data,stream=f,allow_unicode=True)


