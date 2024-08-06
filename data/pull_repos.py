# Excel文件路径
excel_path = 'C:\\Users\\admin\\Documents\\repo.xlsx'  # 请替换为你的Excel文件路径
# 指定的目录
target_directory = 'D:\\yzs_repos'  # 请替换为你想存放仓库的目录路径

import pandas as pd
import subprocess
import os
import concurrent.futures

def clone_repo(git_url, target_dir):
    """使用git命令克隆仓库"""
    cmd = ['git', 'clone', git_url, target_dir]
    print(f"克隆开始: {git_url}")
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"克隆完成: {git_url}")

def main():
    df = pd.read_excel(excel_path)
    # 使用集合去重
    unique_repos = set(df['代码仓库'])

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for repo_url in unique_repos:
            # 移除URL末尾的.git后缀
            repo_name = repo_url.split('/')[-1].replace('.git', '')
            target_path = os.path.join(target_directory, repo_name)
            futures.append(executor.submit(clone_repo, repo_url, target_path))

        # 等待所有线程任务完成
        concurrent.futures.wait(futures)

if __name__ == '__main__':
    main()


