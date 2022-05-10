import yaml

def load_yaml(filename):
    stream = open(filename,'r')
    data = yaml.load(stream,yaml.FullLoader)
    return data

if __name__ == '__main__':
    a= load_yaml('../data/data_read.yaml')
    print(a)