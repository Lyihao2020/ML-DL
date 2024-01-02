"""
https://api.github.com/search/repositories?q=language:python&sort=stars
https://api.github.com/ 将请求发送到网址响应API调用的部分
search/repositories 让API搜索GitHub上所有的仓库
? 指出我们要传递一个实参
q=language:python 只想获取Python作为主语言的仓库
&sort=stars 按其星级进行排序
"""

import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code: ', r.status_code)   # 请求成功的标志

# 将API响应存储到一个变量中
response_dict = r.json()    # json() 将信息转换为一个Python字典
# 处理结果
print(response_dict.keys())
print('Total repositories: ', response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print('Repositories returned: ', len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]
print('\nKeys: ', len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print("\nSelected information about first repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

"""
大多数API都存在速率限制，即你在限定时间内可执行的请求数存在限制
https://api.github.com/rate_limit 可以查看
"""
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call, and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
try:
    r = requests.get(url)
    r.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
    exit()

print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': {'href': repo_dict['html_url']},
    }
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
