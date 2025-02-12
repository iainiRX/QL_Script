#   --------------------------------注释区--------------------------------
#   入口:杜蕾斯
#   变量:dlsck
#   多号分割方式 [ & 或 新建同名变量 ]
#   完成小程序任务 抽奖, 签到, 查询
#   corn: 一天一次即可
#   --------------------------------祈求区--------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#   --------------------------------代码区--------------------------------

'''
Powered By XXM
QQ Group:3426767388
Create at [2025-2-13 1:20]

 .----------------. .----------------. .----------------. .----------------. .-----------------.
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |   _____      | | |     _____    | | |    ___       | | | _____  _____ | | | ____  _____  | |
| |  |_   _|     | | |    |_   _|   | | |  .'   '.     | | ||_   _||_   _|| | ||_   \|_   _| | |
| |    | |       | | |      | |     | | | /  .-.  \    | | |  | |    | |  | | |  |   \ | |   | |
| |    | |   _   | | |      | |     | | | | |   | |    | | |  | '    ' |  | | |  | |\ \| |   | |
| |   _| |__/ |  | | |     _| |_    | | | \  `-'  \_   | | |   \ `--' /   | | | _| |_\   |_  | |
| |  |________|  | | |    |_____|   | | |  `.___.\__|  | | |    `.__.'    | | ||_____|\____| | |
| |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------' 
'''
import requests, re, os, time

os.environ["dlsck"] = "Bk3gcWf1RBDQiHpmAxAVN6zedhIQPECd-w_mpj4XNy0Dfp0Cda83f4wBvbXoMH6C"

class DLS():
    def __init__(self, token):
        self.curl = "https://vip.ixiliu.cn/mp/activity.lottery/draw"
        self.token = token
        self.headers = {
            "Host": "vip.ixiliu.cn",
            "Connection": "keep-alive",
            "content-type": "application/json;charset=utf-8",
            "Enterprise-hash": "10006",
            "platform": "MP-WEIXIN",
            "Access-Token": self.token, # Bk3gcWf1RBDQiHpmAxAVN6zedhIQPECd-w_mpj4XNy0Dfp0Cda83f4wBvbXoMH6C
            "sid": "10006",
            "charset": "utf-8",
            "Referer": "https://servicewechat.com/wxe11089c85860ec02/43/page-frame.html",
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; M2012K11C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.103 Mobile Safari/537.36 XWEB/1300333 MMWEBSDK/20241202 MMWEBID/2582 MicroMessenger/8.0.56.2800(0x28003856) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
            "Accept-Encoding": "gzip, deflate, br"
        }
        self.params = {
            "snId": "391840383318656",
            "channelSn": "0"
        }
        self.sign_url = ''
        self.query_url = 'https://vip.ixiliu.cn/mp/points.log/info'

    def main(self):
        """拆分变量&登录账号"""
        if 'dlsck' in os.environ:
            dlsck = os.environ.get('dlsck')
            account_list = dlsck.split('&')
            print(f'查找到{len(account_list)}个叼毛')
            # print(account_list)
        else:
            dlsck = ''
            print('没有叼毛')

        z = 1
        try:
            for account in account_list:    # 用 '#' 分割 ck 和 uid
                print(f"\n\n登录第{z}个账号")
                # print(account)
                self.token = account
                self.CJ()   # 抽奖
                self.query() # 查询

                z+=1
                time.sleep(0.6)
        except Exception as e:
            print(e, '未知错误1')  

    def CJ(self):
        """抽奖"""
        try:
            r = requests.get(self.curl, headers=self.headers, params=self.params).json()
            if r.get('status') == 40001:  # Token invalid
                print("Access-Token 无效，请检查 Token")
            else:
                print(r['msg'])
        except Exception as e:
            print(f"抽奖请求发生错误: {e}")

    def query(self):
        r  = requests.get(self.query_url, headers=self.headers).json()
        print("余额" + str(r['data']['balance']) + r['data']['points_name'])
        # print(r)

dls = DLS(token=os.environ.get("dlsck"))
dls.main()
