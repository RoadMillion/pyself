# 总的数据条数
total_rows = 12692
# 每次查询的数量
batch_size = 300

# SQL语句的基础部分
base_sql = """
select * from customer_standard_price c where CHARGE_ITEM_ID = '3a30fcdda29411e6b64c525400ce35a4_1' and BOUND_TYPE  = 'IB'
and EFFECTIVE_TIME <= '2023-11-09' and (EXPIRED_TIME > '2023-11-09' or EXPIRED_TIME is null) and mobilization_wharf_id is not null
  and `PORT_ID`  = 'SHANGHAI' and PORT_STANDARD_PRICE_SET_ID = 1
"""

# 计算需要生成的SQL查询语句的数量
num_queries = (total_rows + batch_size - 1) // batch_size

# 批量生成SQL查询语句
for i in range(num_queries):
    offset = i * batch_size
    batch_sql = f"{base_sql} LIMIT {offset}, {batch_size};"
    print(batch_sql)
