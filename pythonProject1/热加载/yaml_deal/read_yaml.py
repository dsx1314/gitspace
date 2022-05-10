import yaml

#
def read_extract_data(file,key):
    with open(file,encoding='utf-8') as f:
        value = yaml.load(f,Loader=yaml.FullLoader)

        return value[key]


if __name__ == '__main__':
    a = read_extract_data('../data/demo.yaml','age')
    # b = a["age"]
    print(a)




























# import yaml
# import os
# import os.path
#
# class Loader(yaml.Loader): # 继承
#     def __init__(self, stream):
#         self._root =os.path.split(stream.name)[0]
#         super(Loader,self).__init__(stream)
#     def include(self, node):
#         filename =os.path.join(self._root,self.construct_scalar(node))
#         with open(filename,'r') as f:
#             return yaml.load(f, Loader)
#
# Loader.add_constructor('!include',Loader.include)
#
# project_path =os.path.split(os.path.realpath(__file__))[0].split('tools')[0]  # 项目路径
# def get_yaml_data(fileDir):
#     # 1、在内存里加载这个文件
#     # f = open(fileDir, 'r', encoding='utf-8')
#     with open('../configs/a.yaml','r') as f:
#         data = yaml.load(f, yaml.Loader)
#     print(data)
#
#     # 2、调用yaml读取文件
#     res = yaml.load(f, Loader=yaml.FullLoader)  # Loader=yaml.FullLoader 更加安全
#     return res
#
# if __name__ == '__main__':
#     info = get_yaml_data(project_path + r'../configs/a.yaml')
#     print(info)