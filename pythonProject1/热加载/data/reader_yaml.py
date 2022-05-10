import importlib
import inspect
import os
import jinja2
import yaml
import random
import json
from jinja2 import Template


class Hot:
    # tpl_path = 'F:\pythonProject1\热加载\data\demo_03.yaml',读取yaml文件
    def reander(self,**kwargs):
        tpl_path = 'F:\pythonProject1\热加载\data\demo_03.yaml'
        path,filename = os.path.split(tpl_path)
        return jinja2.Environment(loader=jinja2.FileSystemLoader(path)).get_template(filename).render(**kwargs)





# 加载debug模块
    def all_functions(self=None):
        debug_module = importlib.import_module("debug")
        all_function = inspect.getmembers(debug_module,inspect.isfunction)
        print(dict(all_function))
        return dict(all_function)

    r = reander(self=None,**all_functions())
    print(r)
    print(yaml.safe_load(r))

if __name__ == '__main__':
    Hot()
