import pandas as pd

# 读取上传的Excel文件
file_path = '/mnt/data/front - 副本.xlsx'
df = pd.read_excel(file_path)

# 显示前几行以了解x`表格结构
df.head()
