import os
import time
import sys
import uiautomator2 as u2


# v0.0.1 
# author by william
def conn_phone(id):
    d = u2.connect(id)
    if not d.service("uiautomator").running():
        d.service("uiautomator").start()
        time.sleep(3)

    if not d.agent_alive:
        u2.connect()
        d = u2.connect(id)
    return d


def start():
    # 此处需要设置为你的手机的序列号
    id = "415cd4ea"
    d = conn_phone(id)
    hierarchy_str = ""
    recv_time_list = []

    while True:
        if d(text="我知道了").exists:
            d(text="我知道了").click()

        if d(textContains="结算").exists:
            d(textContains="结算").click()
        if d(text="返回购物车").exists:
            d(text="返回购物车").click()

        if d(text="确定").exists:
            d(text="确定").click()

        if d(text="立即支付").exists:
            d(text="立即支付").click()

        if d(text="支付订单").exists:
            print("抢菜成功,请手动支付!")
            sys.exit(0)
if __name__ == '__main__':
    print("美团抢菜插件程序正在运行中....")
    start()
