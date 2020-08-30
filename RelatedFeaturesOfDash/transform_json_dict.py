#
# Refer to: https://www.cnblogs.com/xxpythonxx/p/12031446.html
#
# 在Python语言中，json数据与dict字典以及对象之间的转化，是必不可少的操作。
# 在Python中自带json库。通过import json导入。
# 在json模块有2组方法:
# loads()：将json数据转化成dict数据; dumps()：将dict数据转化成json数据。
# load()：读取json文件数据，转成dict数据； dump()：将dict数据转化成json数据后写入json文件。
#

import json

# some JSON string:
dt_jsonstr =  '{ "name":"John", "age":30, "city":"New York"}'

# parse json string:
dt_dict = json.loads(dt_jsonstr)

# the result is a Python dictionary:
print(dt_dict["age"])

dt_jsonstr2 = json.dumps(obj=dt_dict)
print(dt_jsonstr2)   # type(dt_jsonstr2) is str

with open('jsontxtout.json', 'w') as f:
    json.dump(dt_dict, f)  # 会在目录下生成一个jsontxtout.json的文件，文件内容是dict数据转成的json数据

with open('jsontxtout.json', 'r') as f:
    dt_dict2 = json.load(fp=f)
    print(dt_dict2)  # { "name":"John", "age":30, "city":"New York"}
