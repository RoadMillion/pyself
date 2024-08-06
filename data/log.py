# 示例日志输入
log_sql = """
SELECT COUNT(CASE WHEN status = 0 THEN 1 END) AS untreatedCount, COUNT(CASE WHEN status = 1 THEN 1 END) AS processedCount FROM price_warning_task pwt join price_warning_task_process pwtp2 on pwt.id = pwtp2.task_id WHERE pwtp2.plan_deal_date >= ? and pwtp2.plan_deal_date < ? and pwtp2.plan_deal_date < ? 
"""


log_params = "2024-01-01 00:00:00(String), 2024-04-30 23:59:59(String), 2024-04-30 23:59:59(String)"


def replace_placeholders(sql, params):
    # 将参数分割并去除类型信息
    params_values = [p.split("(")[0] for p in params.split(", ")]
    # 用正则表达式找到所有的占位符，并逐一替换
    for value in params_values:
        sql = sql.replace("?", '\'' + value + '\'', 1)
    return sql


# 执行替换
final_sql = replace_placeholders(log_sql, log_params)
print(final_sql)
