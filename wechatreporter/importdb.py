import pymysql
import re

conn = pymysql.connect(
    host='122.254.94.211',
    user='root',
    password='o#DwN&JSa56',
    db='wechat_reporter',
    charset='utf8mb4',
    port=3306)

cur = conn.cursor()

with open(r"C:\Users\admin\Documents\fish\毛驴儿.txt", encoding='utf-8') as f:
    lines = f.readlines()
    filter_lines = []
    reg = "^.+[\u4E00-\u9FFF]\s\(.+\):"

    for line in lines:
        # 去除转发的聊天记录 简单过滤
        if (line.startswith('毛驴儿') or line.startswith('fish')) and re.match(reg, line):
            filter_lines.append(line.strip())

for line in filter_lines:
    s1 = line.find(" ")
    s2 = line.find("):")
    name = line[:s1]
    time = line[s1 + 2:s2]
    content = line[s2 + 2:]
    print(line)
    insert_sql = f"insert into log(user,datetime,content) values ('{name}','{time}' ,'{pymysql.converters.escape_string(content)}')"
    cur.execute(insert_sql)
conn.commit()
