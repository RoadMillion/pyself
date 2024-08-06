import os
import subprocess
import re

repo_directory = "D:\dd"
dependency_pattern = r'\[INFO\].+\s[\-|\+]\s([a-zA-Z0-9\.\-_]+):([a-zA-Z0-9\.\-_]+):jar:([a-zA-Z0-9\.\-_]+):'

def get_project_dependencies(project_path):
    """对单个项目执行 Maven 依赖分析并返回依赖列表"""
    command = ['cmd', 'mvn', 'dependency:tree']
    process = subprocess.Popen(command, cwd=project_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    print(stdout)
    print(stderr)
    dependencies = set()
    for line in stdout.split('\n'):
        match = re.search(dependency_pattern, line)
        print(match)
        if match:
            dependencies.add((match.group(1), match.group(2), match.group(3)))

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
    print(os.environ['PATH'])
    analyze_all_projects(repo_directory)
