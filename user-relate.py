 # -*- coding: UTF-8 -*-
import re
import json
from pathlib import Path
import os
import time
import numpy as np

if __name__ == "__main__":
    # path = '/home/riko/temp'
    # files = Path(path).rglob("*.md")
    # user_name = {}
    # thread_data = {}
    # for file in files:
    #     print(file)
    #     file_name = str(file)[16:23]
    #     print(file_name)
    #     with open (file, 'r', encoding='UTF-8') as f:
    #         lines = f.readlines()
    #         a = ''
    #         for line in lines:
    #             ids = re.findall(r"####\s\s([^#\s]+)\s\s", line)
    #             if(ids):
    #                 if(file_name in thread_data.keys()):
    #                     thread_data[file_name].append(ids[0])
    #                 else:
    #                     thread_data[file_name] = []
    # with open ("/home/riko/temp/thread_data.json","w",encoding='utf-8') as f:
    #     f.write(json.dumps(thread_data,indent=2,ensure_ascii=False))

    # with open ("/home/riko/temp/thread_data.json","r",encoding='utf-8') as f:
    #     thread_data = json.load(f)
    # user_set = set()
    # user_dict = {}
    # for i in thread_data.keys():
    #     user_set = user_set.union(set(thread_data[i]))
    # for i in user_set:
    #     user_dict[i] = []
    #     for j in thread_data.keys():
    #         user_dict[i].append(thread_data[j].count(i))
    # user_list = list(user_dict.keys())
    # for i in user_list:
    #     if(sum(user_dict[i]) < 5):
    #         user_dict.pop(i)
    #     else:
    #         x = np.array(user_dict[i])
    #         if(np.count_nonzero(x) < 5):
    #             user_dict.pop(i)
    # with open ("/home/riko/temp/user_data.json","w",encoding='utf-8') as f:
    #     f.write(json.dumps(user_dict,indent=2,ensure_ascii=False))

    with open ("/home/riko/temp/user_data.json","r",encoding='utf-8') as f:
        user_data = json.load(f)
    print(len(user_data.keys()))
    # used_set = set()
    # data = []
    # nodes = []
    # links = []
    # for i in list(user_data.keys()):
    #     used_set.add(i)
    #     snode = {}
    #     snode['name'] = i
    #     snode['symbolSize'] = sum(user_data[i])
    #     snode['value'] = sum(user_data[i])
    #     snode['draggable'] = False
    #     snode['itemStyle'] = {"color" : '#689d6a'}
    #     c = snode
    #     nodes.append(c)

    #     for j in list(user_data.keys()):
    #         if i != j or j not in used_set:
    #             t1 = np.array(user_data[i])
    #             t2 = np.array(user_data[j])
    #             a_norm = np.linalg.norm(t1)
    #             b_norm = np.linalg.norm(t2)
    #             slink_value = np.dot(t1,t2) / (a_norm * b_norm)
    #             if slink_value <= 0.5:
    #                 continue
    #             else:
    #                 slink = {}
    #                 slink['source'] = i
    #                 slink['target'] = j
    #                 slink['lineStyle'] = {}
    #                 slink['value'] = slink_value
    #                 slink['lineStyle']['width'] = slink_value
    #                 slink['lineStyle']['color'] = 'rgba(7,102,120,0.7)'
    #                 slink['lineStyle']['edge_label'] = '相似度：'+str(slink_value)
    #                 d = slink
    #                 links.append(d)
    # data.append(nodes)
    # data.append(links)
    # with open ("/home/riko/temp/result.json","w",encoding='utf-8') as f:
    #     f.write(json.dumps(data,indent=2,ensure_ascii=False))
