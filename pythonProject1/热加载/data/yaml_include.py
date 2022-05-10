import yaml
import os.path

class Loader(yaml.Loader):

    def __init__(self,stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader,self).__init__(stream)


    def include(self,node):
        filename = os.path.join(self._root,self.construct_scalar(node))

        with open(filename, 'r') as f:
            return yaml.load(f,Loader)

Loader.add_constructor('!include',Loader.include)

def load_yaml(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            dict_obj = yaml.load(f, Loader=Loader)

        return dict_obj
    else:
        raise FileNotFoundError('not found yaml file %s' % file_name)

if __name__ == '__main__':
    yaml_dict = load_yaml('a.yaml')
    print(yaml_dict)