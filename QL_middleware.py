#    ___   ___  ____  ____    __ 
#   / _ | / _ \/  _/ / __ \  / / 
#  / __ |/ ___// /  / /_/ / / /__
# /_/ |_/_/  /___/__\___\_\/____/
#               /___/            

"""
青龙面板API
~~~~~~~~~~~~~~~~~~~~~
本模块参照青龙面板API编写, 开箱即用, 包含任务, 环境变量, 日志, 系统信息等...
作者: 神奇海螺
QQ: 3426767388
Blog: https://rxgo.cn

"""

import requests
from pprint import pprint
from typing import List, Any

# os.environ['URL'] = 'http://192.168.1.200:5960'
# os.environ['ID'] = '-Z4vSdHyWgXL'
# os.environ['SECRET'] = 'ZGiUdjN5W8EZ-JnxiQlZw--4'
# os.environ['token'] = '94b5a3de-7059-49cc-9eae-1841d28d27bd'

class QL_API:
    """青龙API"""
    def __init__(self, URL, ID, SECRET):
        self.url = URL
        self.ID = ID
        self.SECRET = SECRET
        self.token = ""

    def get_token(self):
        """获取你的token"""
        response = requests.get(f'{self.url}/open/auth/token', params={'client_id': self.ID, 'client_secret': self.SECRET}).json()
        self.token = response['data']['token']
        return self.token

class Tasks(QL_API):  
    """任务相关"""
    def __init__(self, token, URL=None, ID=None, SECRET=None):
        super().__init__(URL, ID, SECRET)
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}',
            'Accept': 'application/json'
        }

    def timed_task(self):
        """获取定时任务视图管理"""
        # pprint(self.headers)
        response = requests.get(f"{self.url}/open/crons/views", headers=self.headers).json()
        return response

    def get_timed_task(self):
        """获取所有定时任务"""
        response = requests.get(f"{self.url}/open/crons", headers=self.headers).json()
        return response

    def get_tasks_detail(self, id: int):
        """获取定时任务详情"""
        response = requests.get(f"{self.url}/open/crons/{id}", headers=self.headers).json()
        return response

    def creat_tasks(self, command: str=None, schedule: str=None, name: str=None, labels: List[str]= [], sub_id: int = None, extra_schedules: List[Any]=None, task_before: str=None, task_after: str=None):
        """创建定时任务"""
        task_data = {
            'command': command,     
            'schedule': schedule,
            'name': name,
            'labels': labels,
            'sub_id': sub_id,
            'extra_schedules': extra_schedules,
            'task_before': task_before,
            'task_after': task_after
        }
       
        try:
            response = requests.post(f"{self.url}/open/crons", headers=self.headers, json=task_data).json()
            return response
            # print(response.json())
        except Exception as e:
            return f"Error occurred: {e}"
    
    def run_task(self, task_id: List[int]):
        """运行定时任务"""
        response = requests.put(f"{self.url}/open/crons/run", headers=self.headers, json=task_id).json()
        return response

    def stop_task(self, task_id: List[int]):
        """停止定时任务"""
        response = requests.put(f"{self.url}/open/crons/stop", headers=self.headers, json=task_id).json()
        return response
    
    def get_tasks_logs(self, task_id: int):
        """获取指定任务的执行日志"""
        response = requests.get(f"{self.url}/open/crons/{task_id}/log", headers=self.headers).json()
        return response

    def topping_tasks(self, taks_id: List[int]):
        """置顶任务"""
        response = requests.put(f"{self.url}/open/crons/pin", headers=self.headers, json=taks_id).json()
        return response
    
    def un_topping_tasks(self, taks_id: List[int]):
        """取消置顶任务"""
        response = requests.put(f"{self.url}/open/crons/unpin", headers=self.headers, json=taks_id).json()
        return response

class Env(Tasks):
    """环境变量相关"""
    def __init__(self, token: str, URL: str=None):
        super().__init__(URL=URL, token=token)
        self.token = token

    def create_variable(self, name: str, value: str, remarks: str):
        """创建变量"""
        data = [{
            'name': name,      # 变量名
            'value': value,    # 变量值
            'remarks': remarks       # 备注
        }]
        res = requests.post(f"{self.url}/open/envs", headers=self.headers, json=data).json()
        return res

    def get_env_list(self, query_key_word: str = None):
        """查询指定变量 默认获取环境变量列表"""
        res = requests.get(f"{self.url}/open/envs", headers=self.headers, params=f"searchValue: {query_key_word}").json()
        return res
    
    def get_single_env(self, env_id: int):
        """查询单个环境变量"""
        res = requests.get(f"{self.url}/open/envs/{env_id}", headers=self.headers).json()
        return res
    
    def del_varibale(self, env_id: List[int]):
        """删除变量"""
        res = requests.delete(f"{self.url}/open/envs", headers=self.headers, json=env_id).json()
        return res
    
    def update_varible(self, env_id: int, name: str, value: str, remarks: str):
        """更新环境变量"""
        data = {
            'id': env_id,      # 环境变量ID
            'name': name,      # 变量名
            'value': value,    # 变量值
            'remarks': remarks       # 备注
        }

        res = requests.put(f"{self.url}/open/envs", headers=self.headers, json=data).json()
        return res
    
class Logs(Tasks):  
    def __init__(self, token: str, URL: str=None):
        super().__init__(URL=URL, token=token)

    def logs(self):
        """基础路径logs 获取日志列表"""
        response = requests.get(f"{self.url}/open/logs", headers=self.headers).json()
        return response

    def detail_logs(self, log_path, file_name):
        """获取日志详情"""
        response = requests.get(f"{self.url}/open/logs/detail/{log_path}/{file_name}", headers=self.headers).json()
        return response
    
class System(QL_API):
    """系统信息"""
    def __init__(self):
        super().__init__()
    
    def basic_infomation(self):
        """系统初始化状态和版本信息"""
        res = requests.get(f"{self.url}/open/system", headers=self.headers).json()
        return res
    def get_system_config(self):
        """获取系统配置"""
        res = requests.get(f"{self.url}/open/config", headers=self.headers).json()
        return res



