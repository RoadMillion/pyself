# -*- coding: utf-8 -*-
import jieba
import re
time_reg = re.compile(r'\(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}\)')
common_text_reg = re.compile(r'^.+[\u4E00-\u9FFF]\s\(.+\):')
special_reg = re.compile(r'\[(.+)]')
blank_reg = re.compile(r'\s|[^\u4e00-\u9fa5]+|的|也|了|么|图片|是|语音|吗|吧|有|一个|一下|这个|一点|')

with open(r'./chat.txt', 'a+', encoding='utf-8') as wf:
    with open(r"C:\Users\admin\Documents\fish\毛驴儿.txt", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if (line.startswith('毛驴儿') or line.startswith('fish')) and common_text_reg.match(line):
                line = line.removeprefix("毛驴儿").removeprefix("fish")
                line = re.sub(time_reg, '', line)
                line = re.sub(special_reg, '', line)
                line = re.sub(blank_reg, '', line)
                if not line:
                    continue
                print(line)
                wf.write(','.join(jieba.lcut(line, cut_all=False)) + ',')
        f.close()
    wf.close()
