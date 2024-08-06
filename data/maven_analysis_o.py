import os
import subprocess
import re

import pandas as pd

repo_directory = "D:\dd"
dependency_pattern = r'(.+)\+\- (.+):(.+):jar:(.+):'

def get_project_dependencies(path):
    with open(path, 'r') as f:
        content = f.read()
        f.close()
        dependencies = set()
        for line in content.split('\n'):
            match = re.search(dependency_pattern, line)
            if match:
                dependencies.add((match.group(2), match.group(3), match.group(4)))
        return dependencies


def analyze_all_projects(repo_dir):
    """分析 repo_dir 目录下所有项目的依赖"""
    for project in os.listdir(repo_dir):
        project_path = os.path.join(repo_dir, project)
        print(project_path)
        if os.path.isdir(project_path):
            print(f"正在分析项目: {project}")
            dependencies = get_project_dependencies(project_path)
            # 处理依赖信息，例如打印或保存到文件
            print(f"{project} 的依赖：{dependencies}")

if __name__ == '__main__':
    pp = 'D:\\yzs_repos'
    deps = get_project_dependencies(os.path.join(pp, 'harbour-server', 'dev.txt'))
    # export deps to excel
    print(deps)
    pd.DataFrame(deps).to_excel(os.path.join(pp, 'harbour-server', 'dev.xlsx'))
