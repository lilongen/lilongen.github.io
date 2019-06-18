#!/usr/bin/env python
# coding: utf-8
#

keywords = """CDH Hdaoop HDFS Spark Hive Greenplum ETL Kafka 推荐系统 实时计算 数据仓库
AI NLP CNN RNN 机器学习 神经网络
DevOps Docker Kubernetes Network
Linux Kerberos Virtulization VMware vSphere ESXi 虚拟化 私有云
Python Perl Bash Java DesignPattern 正则表达式 设计模式 数据结构
算法 Dijkstra A* DFS BFS
Nginx OpenResty Redis MySQL
"""

def get_weight(idx):
    return max(3, int(10 - idx));


def output_cloud_keywords(content):
    f = open('./logo.keywords.txt', 'w')
    f.write(content)
    f.close()

    
def get_cloud_keywords():
    outlines = []
    for idx, line in enumerate(keywords.splitlines()):
        outlines.append((line + ' ') * get_weight(idx))
    return ' '.join(outlines)


def main():
    output_cloud_keywords(get_cloud_keywords())


main()