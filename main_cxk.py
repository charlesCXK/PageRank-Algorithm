#-*- coding:utf-8 -*-
import os, sys
from pygraph.classes.digraph import digraph

class PRAlgrothm(object):
    __doc__ = '''根据信息建图并计算PageRank值'''

    def __init__(self, dg):
        self.alpha = 0.85
        self.max_iterations = 100       #最大迭代次数
        self.delta = 0.0001     #判断迭代结束的标志
        self.graph = dg

    def PageRank(self):
        '''
        #将没有出链的节点改成对所有节点都有出链
        j = 0
        for node in self.graph.nodes():
            print(j)
            j += 1
            if len(self.graph.neighbors(node)) == 0:
                for other_node in self.graph.nodes():
                    digraph.add_edge(self.graph, (node, other_node))
        '''

        nodes = self.graph.nodes()
        graph_size = len(nodes)     #节点个数

        if graph_size == 0:
            return {}
        page_rank = dict.fromkeys(nodes, 1.0 / graph_size)  # 给每个节点赋予初始的PR值

        for i in range(self.max_iterations):
            print("迭代次数：", i)
            change = 0
            pg = {}     #用一个字典来记录每个节点的新的PageRank值，最后统一更新
            for node in nodes:
                pg[node] = 0
                pg[node] += (1-self.alpha) / graph_size       #随机游走
                for neighbour in self.graph.incidents(node):
                    pg[node] += page_rank[neighbour] / len(self.graph.neighbors(neighbour)) * self.alpha
                change += abs(pg[node]-page_rank[node])       #加上这一个节点的变化值

            #更新PageRank值
            for node in nodes:
                page_rank[node] = pg[node]

            if change <= self.delta:
                print("已完成迭代，迭代次数：", i)
                break

        return page_rank


if __name__ == '__main__':
    print("哈哈，主程序已运行")