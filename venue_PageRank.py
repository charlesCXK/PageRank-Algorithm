#-*- coding:utf-8 -*-
from homework_cxk import PRAlgrothm
import re
from pygraph.classes.digraph import digraph

if __name__ == '__main__':
    #处理会议，思路是先读取acl-metadata.txt，确定论文ID和会议之间的关系；然后读取paper-citation-network-nonself.txt，根据paper之间的引用关系来确定venue之间的引用关系
    #建两个图
    paper_venue = digraph()
    venue_dg = digraph()
    #带缓存的读文件
    #读取信论文和会议之间关系，构建有向图
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
                if line[0] == 'v': #是会议名称
                    venue = re.findall(r'\{.*?\}', line)
                    venue[0] = venue[0][1:-1]
                    print(venue[0])
                    venue[0] = venue[0].split("\t")[0]      #去掉后面的制表符
                    #构建paper-venue的有向图，paper指向venue
                    if paper_venue.has_node(id[0]) == False:
                        paper_venue.add_node(id[0])
                    if paper_venue.has_node(venue[0]) == False:
                        paper_venue.add_node(venue[0])
                    paper_venue_edge = [id[0], venue[0]]
                    if paper_venue.has_edge(paper_venue_edge) == False:
                        paper_venue.add_edge(paper_venue_edge)

    #读取论文之间的引用关系，获得会议之间的引用关系
    with open("aan/release/2014/networks/paper-citation-network-nonself.txt", 'r', encoding='utf-8') as article_file:
        while 1:
            lines = article_file.readlines(100000)   #每次读十万行
            if not lines:
                break
            for line in lines:
                my_list = line.split("==>")
                node1 = my_list[0][:-1]
                node2 = my_list[1][1:-1]

                #寻找两篇文章相关的会议，以文章之间引用关系作为会议之间引用关系
                for venue1 in paper_venue.neighbors(node1):
                    for venue2 in paper_venue.neighbors(node2):
                        if venue_dg.has_node(venue1) == False:
                            venue_dg.add_node(venue1)
                        if venue_dg.has_node(venue2) == False:
                            venue_dg.add_node(venue2)
                        venue_edge = [venue1, venue2]
                        if venue_dg.has_edge(venue_edge) == False:
                            venue_dg.add_edge(venue_edge)

    print("会议文件图中点的数量：", len(venue_dg.nodes()))
    print("会议文件图中边的数量：", len(venue_dg.edges()))
    Venue = PRAlgrothm(venue_dg)
    venue_pagerank = Venue.PageRank()
    #将字典转化成有序元组
    new_venue = sorted(venue_pagerank.items(), key=lambda x:x[1], reverse = True)

    #输出文件
    venue_file = open("venue_rank.txt", "w")
    for it in range(len(new_venue)):
        venue_file.write(str(new_venue[it][0]) + '\t' + str(new_venue[it][1]) + '\n')
    venue_file.close()