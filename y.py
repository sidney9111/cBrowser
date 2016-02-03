# -*- coding: utf-8 -*-
import random

from flow.FlowItem import FlowItem
def get_data():
    """返回0到9之间的3个随机数，模拟异步操作"""
    return random.sample(range(10), 3)
 
def consume():
    """显示每次传入的整数列表的动态平均值"""
    running_sum = 0
    data_items_seen = 0
    
    while True:
        print('Waiting to consume')
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print('Consumed, the running average is {}'.format(running_sum / float(data_items_seen)))
 
def produce(consumer):
    """产生序列集合，传递给消费函数（consumer）"""
    while True:
        data = get_data()
        print('Produced {}'.format(data))
        consumer.send(data)
        yield
from LinkSave import LinkSave
from MongoSave import MongoSave
if __name__ == '__main__':
    # item = FlowItem()
    # print(item)

    # boa = [{'name':'//h/a/img/@href','index':1}]
    # boa[0]['key']=38
    # print(boa)
    # print(boa[0])
    # print(boa[0]['key'])
    # consumer = consume()
    # consumer.send(None) 
    # producer = produce(consumer)
 
    # # for _ in range(10):
    # #     print('Producisng...')
    # next(producer)
    
    link = LinkSave()
    ret = link.readlines("data")
    save = MongoSave()
    for v in ret:
        item = eval(v)
        item['date_x']=item['date'][:10]
        save.add(item)