import time

import requests
from tqdm import tqdm
import json

def parse_response(json_str):
    try:
        data = json.loads(json_str)
        if data.get('success') is not True:
            return json_str
    except json.JSONDecodeError:
        return None
    return None
def sync_customer_contracts(ids, output_file, batch=20):
    url = 'https://new.carrierglobe.com/ws-truck/customerContract/sync'
    # url = 'http://localhost:8080/ws-truck/customerContract/sync'
    # url = 'http://new2.fat.driverglobe.com/ws-truck/customerContract/sync'
    headers = {
        'X-Requested-By': 'eshipping',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json'
    }

    with open(output_file, 'a') as file:
        for i in tqdm(range(0, len(ids), batch), desc="Processing batches"):
            batch_ids = ids[i:i + batch]
            data = {'ids': batch_ids}
            response = requests.post(url, json=data, headers=headers)
            s = parse_response(response.text)
            if s is not None:
                file.write(f"ID {id}: {s}\n")

# 示例使用
# 0-3200 数字循环
ids = [i for i in range(99, 8227)]
# ids = [i for i in range(1,2)]
start = time.time()
sync_customer_contracts(ids, 'output.txt')
end = time.time()
print(f"Time elapsed: {end - start} seconds")