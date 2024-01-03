import pandas as pd
import json
# 读取Excel文件
excel_file_path = "../files/b.xlsx" # 更改为你的Excel文件路径
df = pd.read_excel(excel_file_path)

# 将DataFrame转换为JSON格式
json_result = df.to_dict('records')

# 保存JSON数据到文件
json_file_path = "../files/json_file.json" # 更改为你希望保存JSON文件的路径
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_result, json_file, ensure_ascii=False, indent=4)

print("Excel file has been converted to JSON file successfully!")
