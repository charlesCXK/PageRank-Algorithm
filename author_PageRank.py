#-*- coding:utf-8 -*-
from homework_cxk import PRAlgrothm
from pygraph.classes.digraph import digraph

if __name__ == '__main__':
    #先处理作者
    author_dg = digraph()
    #带缓存的读文件
    #读取作者引用信息，构建有向图
    with open("aan/release/2014/networks/author-citation-network-nonself.txt", 'r', encoding='utf-8') as author_file:
        i = 1
        while 1:
            lines = author_file.readlines(100000)   #每次读十万行
            if not lines:
                break
            for line in lines:
                #print(i)        #只是用来确认是否全部读进去了
                i += 1
                #print(line)
                my_list = line.split("==>")
                node1 = my_list[0][:-1]
                node2 = my_list[1][1:-1]
                #如果没有这个节点，就加上去
                if author_dg.has_node(node1) == False:
                    author_dg.add_node(node1)
                if author_dg.has_node(node2) == False:
                    author_dg.add_node(node2)
                new_edge = [node1, node2]
                if author_dg.has_edge(new_edge) == False:
                    author_dg.add_edge(new_edge)      #加上这条引用的有向边
    print("作者文件图中点的数量：", len(author_dg.nodes()))
    print("作者文件图中边的数量：", len(author_dg.edges()))
    Author = PRAlgrothm(author_dg)
    author_pagerank = Author.PageRank()
    #将字典转化成有序元组
    new_author = sorted(author_pagerank.items(), key=lambda x:x[1], reverse = True)
    author_file = open("author_rank.txt", "w")
    for it in range(len(new_author)):
        author_file.write(str(new_author[it][0]) + '\t' + str(new_author[it][1]) + '\n')
    author_file.close()