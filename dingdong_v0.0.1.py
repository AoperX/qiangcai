import os
import time
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

        if d(text="重新加载").exists:
            d(text="重新加载").click()

        if d(textContains="结算").exists:
            d(textContains="结算").click()

        if d(text="确认订单").exists:
            hierarchy_str = d.dump_hierarchy()
            if "自动尝试" in hierarchy_str:
                d.press("back")
                break
            while True:
                if d(text="重新加载").exists:
                    d(text="重新加载").click()

                if d(text="立即支付").exists:
                    d(text="立即支付").click()
                    if d(text="选择送达时间").exists:
                        for elem in d.xpath("//android.widget.TextView").all():
                            if "-" in elem.text:
                                recv_time_list.append(elem.text)
                    d(text=recv_time_list[-1]).click()
if __name__ == '__main__':
    print("叮咚抢菜插件程序正在运行中....")
    start()
