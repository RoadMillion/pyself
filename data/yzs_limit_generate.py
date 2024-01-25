def generate_paginated_sql(original_sql, page_size, total_count):
    # 计算需要生成多少个分页SQL语句
    num_pages = (total_count + page_size - 1) // page_size

    paginated_sqls = []
    for page in range(num_pages):
        offset = page * page_size
        paginated_sql = f"{original_sql} LIMIT {page_size} OFFSET {offset};"
        paginated_sqls.append(paginated_sql)

    return paginated_sqls

# 示例使用
original_sql = """select bd.NAME as 港口, ppd.name 港区, da.NAME as 区域名称, CASE WHEN esp.truck_type = 4 then '四轴' WHEN esp.truck_type = 5 then '五轴' WHEN esp.truck_type = 6 then '六轴' ELSE '未知' END as 车型, esp.outward_price 去程价格, esp.homeward_price 回程价格, date(esp.effective_time) 生效日期 from `area_port_rel` apr join `etc_standard_price` esp on apr.id = esp.area_port_rel_id join basic_data bd on bd.id = apr.port_id join pricing_port_district ppd on ppd.id = apr.port_district_id join door_area da on da.id = apr.door_area_id and da.is_active is TRUE where effective_time <= '2024-01-09 12:00:00'   AND ( expired_time IS NULL OR expired_time > '2024-01-09 12:00:00' )   and apr.port_id = 'SHENZHEN' ORDER by 区域名称"""  # 这里替换为你的原始SQL语句
page_size = 300  # 每页300条数据
total_count = 8991  # 总共10000条数据

paginated_sqls = generate_paginated_sql(original_sql, page_size, total_count)
for sql in paginated_sqls:
    print(sql)

