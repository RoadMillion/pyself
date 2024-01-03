import json
import os

import pandas as pd
import requests
from tqdm import tqdm


def read_excel_files(directory):
    data_list = []  # 初始化空列表，用于存储所有数据

    for filename in os.listdir(directory):  # 遍历目录中的所有文件
        if filename.endswith('.xlsx') or filename.endswith('.xls'):  # 如果是Excel文件
            file_path = os.path.join(directory, filename)  # 构造文件路径
            df = pd.read_excel(file_path)  # 读取Excel文件

            # 我们知道Excel列索引从1开始，而Python索引从0开始，所以我们需要-1进行转换
            # 我们需要的数据在'H','F','G','Q','S'列，对应索引7, 5, 6, 16, 18
            for index, row in df.iterrows():
                data_dict = {"taskId": row[7], "taskCostId": row[5], "containerId": row[6],
                             "startPoint": row[16], "endPoint": row[18]}
                data_list.append(data_dict)  # 将字典数据添加到列表中
    return data_list


directory = '../files/result'  # Excel文件夹路径，可以根据实际情况修改


def post_data_to_api(data_list):
    url = "https://new.carrierglobe.com/ws-truck/pricing/driverCost/redo"
    headers = {'Content-Type': 'application/json', 'X-Requested-By': 'eshipping'}  # 设置请求头

    for data in tqdm(data_list, desc="Sending data", unit="item"):
        # 将数据包装在"dataList"中以满足API需求
        payload = {"dataList": [data]}

        # 将字典转化为JSON格式的字符串
        json_payload = json.dumps(payload)

        # 发送POST请求
        response = requests.post(url, headers=headers, data=json_payload)

        if response.status_code != 200:  # 如果请求成功
            print(f"Failed to send data {data}. Status code: {response.status_code}, response: {response.text}")


# 调用函数

result = read_excel_files(directory)
post_data_to_api(result)
# print(len(result))
# print(json.dumps(result, indent=4, ensure_ascii=False))
