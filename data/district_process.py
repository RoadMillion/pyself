import json


def find_districts(data, parent_name=''):
    result = {}
    name = parent_name + data['name']
    if data['level'] == 'DISTRICT':
        result[data['code']] = name
    else:
        for child in data.get('children', []):
            result.update(find_districts(child, name))
    return result


json_str = '''
{
      "code": "330000000000",
      "name": "浙江省",
      "pinyin": "zhejiangsheng",
      "level": "PROVINCE",
      "children": [
        {
          "code": "330100000000",
          "name": "杭州市",
          "pinyin": "hangzhoushi",
          "level": "CITY",
          "children": [
            {
              "code": "330108000000",
              "name": "滨江区",
              "pinyin": "binjiangqu",
              "level": "DISTRICT"
            },
            {
              "code": "330127000000",
              "name": "淳安县",
              "pinyin": "chunanxian",
              "level": "DISTRICT"
            },
            {
              "code": "330111000000",
              "name": "富阳区",
              "pinyin": "fuyangqu",
              "level": "DISTRICT"
            },
            {
              "code": "330105000000",
              "name": "拱墅区",
              "pinyin": "gongshuqu",
              "level": "DISTRICT"
            },
            {
              "code": "330182000000",
              "name": "建德市",
              "pinyin": "jiandeshi",
              "level": "DISTRICT"
            },
            {
              "code": "330104000000",
              "name": "江干区",
              "pinyin": "jiangganqu",
              "level": "DISTRICT"
            },
            {
              "code": "330112000000",
              "name": "临安区",
              "pinyin": "linanqu",
              "level": "DISTRICT"
            },
            {
              "code": "330114000000",
              "name": "钱塘区",
              "pinyin": "qiantangqu",
              "level": "DISTRICT"
            },
            {
              "code": "330102000000",
              "name": "上城区",
              "pinyin": "shangchengqu",
              "level": "DISTRICT"
            },
            {
              "code": "330122000000",
              "name": "桐庐县",
              "pinyin": "tongluxian",
              "level": "DISTRICT"
            },
            {
              "code": "330103000000",
              "name": "下城区",
              "pinyin": "xiachengqu",
              "level": "DISTRICT"
            },
            {
              "code": "330109000000",
              "name": "萧山区",
              "pinyin": "xiaoshanqu",
              "level": "DISTRICT"
            },
            {
              "code": "330106000000",
              "name": "西湖区",
              "pinyin": "xihuqu",
              "level": "DISTRICT"
            },
            {
              "code": "330110000000",
              "name": "余杭区",
              "pinyin": "yuhangqu",
              "level": "DISTRICT"
            }
          ]
        },
        {
          "code": "330500000000",
          "name": "湖州市",
          "pinyin": "huzhoushi",
          "level": "CITY",
          "children": [
            {
              "code": "330523000000",
              "name": "安吉县",
              "pinyin": "anjixian",
              "level": "DISTRICT"
            },
            {
              "code": "330521000000",
              "name": "德清县",
              "pinyin": "deqingxian",
              "level": "DISTRICT"
            },
            {
              "code": "330503000000",
              "name": "南浔区",
              "pinyin": "nanxunqu",
              "level": "DISTRICT"
            },
            {
              "code": "330502000000",
              "name": "吴兴区",
              "pinyin": "wuxingqu",
              "level": "DISTRICT"
            },
            {
              "code": "330522000000",
              "name": "长兴县",
              "pinyin": "zhangxingxian",
              "level": "DISTRICT"
            }
          ]
        },
        {
          "code": "330400000000",
          "name": "嘉兴市",
          "pinyin": "jiaxingshi",
          "level": "CITY",
          "children": [
            {
              "code": "330481000000",
              "name": "海宁市",
              "pinyin": "hainingshi",
              "level": "DISTRICT"
            },
            {
              "code": "330424000000",
              "name": "海盐县",
              "pinyin": "haiyanxian",
              "level": "DISTRICT"
            },
            {
              "code": "330421000000",
              "name": "嘉善县",
              "pinyin": "jiashanxian",
              "level": "DISTRICT"
            },
            {
              "code": "330402000000",
              "name": "南湖区",
              "pinyin": "nanhuqu",
              "level": "DISTRICT"
            },
            {
              "code": "330482000000",
              "name": "平湖市",
              "pinyin": "pinghushi",
              "level": "DISTRICT"
            },
            {
              "code": "330483000000",
              "name": "桐乡市",
              "pinyin": "tongxiangshi",
              "level": "DISTRICT"
            },
            {
              "code": "330411000000",
              "name": "秀洲区",
              "pinyin": "xiuzhouqu",
              "level": "DISTRICT"
            }
          ]
        },
        {
          "code": "330700000000",
          "name": "金华市",
          "pinyin": "jinhuashi",
          "level": "CITY",
          "children": [
            {
              "code": "330783000000",
              "name": "东阳市",
              "pinyin": "dongyangshi",
              "level": "DISTRICT"
            },
            {
              "code": "330703000000",
              "name": "金东区",
              "pinyin": "jindongqu",
              "level": "DISTRICT"
            },
            {
              "code": "330781000000",
              "name": "兰溪市",
              "pinyin": "lanxishi",
              "level": "DISTRICT"
            },
            {
              "code": "330727000000",
              "name": "磐安县",
              "pinyin": "pananxian",
              "level": "DISTRICT"
            },
            {
              "code": "330726000000",
              "name": "浦江县",
              "pinyin": "pujiangxian",
              "level": "DISTRICT"
            },
            {
              "code": "330702000000",
              "name": "婺城区",
              "pinyin": "wuchengqu",
              "level": "DISTRICT"
            },
            {
              "code": "330723000000",
              "name": "武义县",
              "pinyin": "wuyixian",
              "level": "DISTRICT"
            },
            {
              "code": "330782000000",
              "name": "义乌市",
              "pinyin": "yiwushi",
              "level": "DISTRICT"
            },
            {
              "code": "330784000000",
              "name": "永康市",
              "pinyin": "yongkangshi",
              "level": "DISTRICT"
            }
          ]
        },
        {
          "code": "331100000000",
          "name": "丽水市",
          "pinyin": "lishuishi",
          "level": "CITY",
          "children": [
            {
              "code": "331127000000",
              "name": "景宁畲族自治县",
              "pinyin": "jingningshezuzizhixian",
              "level": "DISTRICT"
            },
            {
              "code": "331122000000",
              "name": "缙云县",
              "pinyin": "jinyunxian",
              "level": "DISTRICT"
            },
            {
              "code": "331102000000",
              "name": "莲都区",
              "pinyin": "liandouqu",
              "level": "DISTRICT"
            },
            {
              "code": "331181000000",
              "name": "龙泉市",
              "pinyin": "longquanshi",
              "level": "DISTRICT"
            },
            {
              "code": "331121000000",
              "name": "青田县",
              "pinyin": "qingtianxian",
              "level": "DISTRICT"
            },
            {
              "code": "331126000000",
              "name": "庆元县",
              "pinyin": "qingyuanxian",
              "level": "DISTRICT"
            },
            {
              "code": "331123000000",
              "name": "遂昌县",
              "pinyin": "suichangxian",
              "level": "DISTRICT"
            },
            {
              "code": "331125000000",
              "name": "云和县",
              "pinyin": "yunhexian",
              "level": "DISTRICT"
            }
          ]
        },
        {
          "code": "330200000000",
          "name": "宁波市",
          "pinyin": "ningboshi",
          "level": "CITY",
          "children": [
            {
              "code": "330206000000",
              "name": "北仑区",
              "pinyin": "beilunqu",
              "level": "DISTRICT"
            },
            {
              "code": "330282000000",
              "name": "慈溪市",
              "pinyin": "cixishi",
              "level": "DISTRICT"
            },
            {
              "code": "330213000000",
              "name": "奉化区",
              "pinyin": "fenghuaqu",
              "level": "DISTRICT"
            },
            {
              "code": "330203000000",
              "name": "海曙区",
              "pinyin": "haishuqu",
              "level": "DISTRICT"
            },
            {
              "code": "330205000000",
              "name": "江北区",
              "pinyin": "jiangbeiqu",
              "level": "DISTRICT"
            },
            {
              "code": "330226000000",
              "name": "宁海县",
              "pinyin": "ninghaixian",
              "level": "DISTRICT"
            },
            {
              "code": "330225000000",
              "name": "象山县",
              "pinyin": "xiangshanxian",
              "level": "DISTRICT"
            },
            {
              "code": "330212000000",
              "name": "鄞州区",
              "pinyin": "yinzhouqu",
              "level": "DISTRICT"
            },
            {
              "code": "330281000000",
              "name": "余姚市",
              "pinyin": "yuyaoshi",
              "level": "DISTRICT"
            },
            {
              "code": "330211000000",
              "name": "镇海区",
              "pinyin": "zhenhaiqu",
              "level": "DISTRICT"
            }
          ]
        },
        {
          "code": "330800000000",
          "name": "衢州市",
          "pinyin": "quzhoushi",
          "level": "CITY",
          "children": [
            {
              "code": "330822000000",
              "name": "常山县",
              "pinyin": "changshanxian",
              "level": "DISTRICT"
            },
            {
              "code": "330881000000",
              "name": "江山市",
              "pinyin": "jiangshanshi",
              "level": "DISTRICT"
            },
            {
              "code": "330824000000",
              "name": "开化县",
              "pinyin": "kaihuaxian",
              "level": "DISTRICT"
            },
            {
              "code": "330802000000",
              "name": "柯城区",
              "pinyin": "kechengqu",
              "level": "DISTRICT"
            },
            {
              "code": "330825000000",
              "name": "龙游县",
              "pinyin": "longyouxian",
              "level": "DISTRICT"
            },
            {
              "code": "330803000000",
              "name": "衢江区",
              "pinyin": "qujiangqu",
              "level": "DISTRICT"
            }
          ]
        },
        {
          "code": "330600000000",
          "name": "绍兴市",
          "pinyin": "shaoxingshi",
          "level": "CITY",
          "children": [
            {
              "code": "330603000000",
              "name": "柯桥区",
              "pinyin": "keqiaoqu",
              "level": "DISTRICT"
            },
            {
              "code": "330604000000",
              "name": "上虞区",
              "pinyin": "shangyuqu",
              "level": "DISTRICT"
            },
            {
              "code": "330683000000",
              "name": "嵊州市",
              "pinyin": "shengzhoushi",
              "level": "DISTRICT"
            },
            {
              "code": "330624000000",
              "name": "新昌县",
              "pinyin": "xinchangxian",
              "level": "DISTRICT"
            },
            {
              "code": "330602000000",
              "name": "越城区",
              "pinyin": "yuechengqu",
              "level": "DISTRICT"
            },
            {
              "code": "330681000000",
              "name": "诸暨市",
              "pinyin": "zhujishi",
              "level": "DISTRICT"
            }
          ]
        },
        {
          "code": "331000000000",
          "name": "台州市",
          "pinyin": "taizhoushi",
          "level": "CITY",
          "children": [
            {
              "code": "331003000000",
              "name": "黄岩区",
              "pinyin": "huangyanqu",
              "level": "DISTRICT"
            },
            {
              "code": "331002000000",
              "name": "椒江区",
              "pinyin": "jiaojiangqu",
              "level": "DISTRICT"
            },
            {
              "code": "331082000000",
              "name": "临海市",
              "pinyin": "linhaishi",
              "level": "DISTRICT"
            },
            {
              "code": "331004000000",
              "name": "路桥区",
              "pinyin": "luqiaoqu",
              "level": "DISTRICT"
            },
            {
              "code": "331022000000",
              "name": "三门县",
              "pinyin": "sanmenxian",
              "level": "DISTRICT"
            },
            {
              "code": "331023000000",
              "name": "天台县",
              "pinyin": "tiantaixian",
              "level": "DISTRICT"
            },
            {
              "code": "331081000000",
              "name": "温岭市",
              "pinyin": "wenlingshi",
              "level": "DISTRICT"
            },
            {
              "code": "331024000000",
              "name": "仙居县",
              "pinyin": "xianjuxian",
              "level": "DISTRICT"
            },
            {
              "code": "331083000000",
              "name": "玉环市",
              "pinyin": "yuhuanshi",
              "level": "DISTRICT"
            }
          ]
        },
        {
          "code": "330300000000",
          "name": "温州市",
          "pinyin": "wenzhoushi",
          "level": "CITY",
          "children": [
            {
              "code": "330327000000",
              "name": "苍南县",
              "pinyin": "cangnanxian",
              "level": "DISTRICT"
            },
            {
              "code": "330305000000",
              "name": "洞头区",
              "pinyin": "dongtouqu",
              "level": "DISTRICT"
            },
            {
              "code": "330382000000",
              "name": "乐清市",
              "pinyin": "leqingshi",
              "level": "DISTRICT"
            },
            {
              "code": "330383000000",
              "name": "龙港市",
              "pinyin": "longgangshi",
              "level": "DISTRICT"
            },
            {
              "code": "330303000000",
              "name": "龙湾区",
              "pinyin": "longwanqu",
              "level": "DISTRICT"
            },
            {
              "code": "330302000000",
              "name": "鹿城区",
              "pinyin": "luchengqu",
              "level": "DISTRICT"
            },
            {
              "code": "330304000000",
              "name": "瓯海区",
              "pinyin": "ouhaiqu",
              "level": "DISTRICT"
            },
            {
              "code": "330326000000",
              "name": "平阳县",
              "pinyin": "pingyangxian",
              "level": "DISTRICT"
            },
            {
              "code": "330381000000",
              "name": "瑞安市",
              "pinyin": "ruianshi",
              "level": "DISTRICT"
            },
            {
              "code": "330329000000",
              "name": "泰顺县",
              "pinyin": "taishunxian",
              "level": "DISTRICT"
            },
            {
              "code": "330328000000",
              "name": "文成县",
              "pinyin": "wenchengxian",
              "level": "DISTRICT"
            },
            {
              "code": "330371000000",
              "name": "温州经济技术开发区",
              "pinyin": "wenzhoujingjijishukaifaqu",
              "level": "DISTRICT"
            },
            {
              "code": "330324000000",
              "name": "永嘉县",
              "pinyin": "yongjiaxian",
              "level": "DISTRICT"
            }
          ]
        },
        {
          "code": "330900000000",
          "name": "舟山市",
          "pinyin": "zhoushanshi",
          "level": "CITY",
          "children": [
            {
              "code": "330921000000",
              "name": "岱山县",
              "pinyin": "daishanxian",
              "level": "DISTRICT"
            },
            {
              "code": "330902000000",
              "name": "定海区",
              "pinyin": "dinghaiqu",
              "level": "DISTRICT"
            },
            {
              "code": "330903000000",
              "name": "普陀区",
              "pinyin": "putuoqu",
              "level": "DISTRICT"
            },
            {
              "code": "330922000000",
              "name": "嵊泗县",
              "pinyin": "shengsixian",
              "level": "DISTRICT"
            }
          ]
        }
      ]
    }
'''


# dict 结果转换为sql的case key then value
def convert_to_sql(r: dict):
    sql = ''
    for key, value in r.items():
        sql += "when '" + key + "' " + "then '" + value + "'\n"
    return sql

data = json.loads(json_str)
result = find_districts(data)
print(json.dumps(result, ensure_ascii=False, indent=2))
#
print(convert_to_sql(result))
