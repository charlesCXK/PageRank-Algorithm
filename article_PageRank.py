#-*- coding:utf-8 -*-
from homework_cxk import PRAlgrothm
import re
from pygraph.classes.digraph import digraph

if __name__ == '__main__':
    #处理论文
    article_dg = digraph()
    #带缓存的读文件
    #读取作者引用信息，构建有向图

    with open("aan/release/2014/networks/paper-citation-network-nonself.txt", 'r', encoding='utf-8') as article_file:
        #i = 1
        while 1:
            lines = article_file.readlines(100000)   #每次读十万行
            if not lines:
                break
            for line in lines:
                #print(i)        #只是用来确认是否全部读进去了
                #i += 1
                #print(line)
                my_list = line.split("==>")
                node1 = my_list[0][:-1]
                node2 = my_list[1][1:-1]
                #如果没有这个节点，就加上去
                if article_dg.has_node(node1) == False:
                    article_dg.add_node(node1)
                if article_dg.has_node(node2) == False:
                    article_dg.add_node(node2)
                new_edge = [node1, node2]
                if article_dg.has_edge(new_edge) == False:
                    article_dg.add_edge(new_edge)      #加上这条引用的有向边
    print("论文文件图中点的数量：", len(article_dg.nodes()))
    print("论文文件图中边的数量：", len(article_dg.edges()))
    Article = PRAlgrothm(article_dg)
    article_pagerank = Article.PageRank()
    #将字典转化成有序元组
    new_article = sorted(article_pagerank.items(), key=lambda x:x[1], reverse = True)

    #读取论文信息，将论文ID和论文标题对应起来
    article_dict = {}       #字典，将编号与标题一一对应
    with open("aan/release/2014/acl-metadata.txt", 'r', encoding='utf-8') as article_name:
        while 1:
            lines = article_name.readlines(60000)   #每次读6万行
            if not lines:
                break
            for line in lines:
                if line[0] == 'i': #是ID
                    #正则表达式提取花括号中的编号
                    id = re.findall(r'\{.*?\}', line)
                    id[0] = id[0][1:-1]
                if line[0] == 't': #是论文标题
                    title = re.findall(r'\{.*?\}', line)
                    title[0] = title[0][1:-1]
                    article_dict[id[0]] = title[0]
        '''
        测试dict的内容是否正确
        for key, value in article_dict.items():
            print(key + '\t' + value + '\n')
        '''

    #输出文件
    article_file = open("article_rank.txt", "w")
    for it in range(len(new_article)):
        article_file.write(article_dict[str(new_article[it][0])] + '\t' + str(new_article[it][1]) + '\n')
    article_file.close()