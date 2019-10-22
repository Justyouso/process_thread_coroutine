# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-10-22 上午11:02


def consumer():
    r = ''
    while True:
        # 返回给生产者,以及接收生产者传来的参数
        n = yield r
        if not n:
            return
        print("[消费者] 正在消费 %s" % n)
        r = "OK"


def produce(c):
    # 启动消费者,必须先send一个None
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("[生产者] 正在生产 %s" % n)
        r = c.send(n)
        print("[生产者] 消费者返回 %s" % r)
    c.close()


if __name__ == "__main__":
    c = consumer()
    produce(c)

    # 运行流程
    # 1. 执行c.send(None),启动消费者
    # 2. 消费者首先执行 yield r ,将空字符r返回给生产者
    # 3. 生产者执行r=c.send(n),将n=1发送给消费者
    # 4. 消费者执行n=yield,接收生产者传过来的n=1,进行消费,并赋值r="OK",再执行 yield r ,
    # 传回消费信息给生产者
    # 特别提示: 协程的暂停是在消费者执行 yield r 的时候,并不是在n=yield
