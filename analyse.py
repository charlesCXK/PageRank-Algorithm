#-*- coding:utf-8 -*-

if __name__ == '__main__':
    with open("author_rank.txt", 'r', encoding='utf-8') as author_file:
        author_list = []
        Count = 0       #计数，统计行数
        tot_sum = 0
        tot_sum = float(tot_sum)        #统计总和
        my_sum = float(0)
        while 1:
            lines = author_file.readlines(10000)   #每次读一万行
            if not lines:
                break
            for line in lines:
                Count += 1
                my_list = line.split("\t")
                #print(my_list[0], len(my_list[0]), my_list[1][:-1], len(my_list[1][:-1]))
                author_list.append(my_list[1][:-1])
                tot_sum += float(my_list[1][:-1])
    for i in range(int(Count/10)):
        my_sum += float(author_list[i])
    #print(Count)
    #print(tot_sum)
    print("前 %10 的作者的PageRank值之和占总和的 %", my_sum/tot_sum*100)

    #处理论文
    with open("article_rank.txt", 'r', encoding='utf-8') as article_file:
        article_list = []
        Count = 0       #计数，统计行数
        tot_sum = 0
        tot_sum = float(tot_sum)        #统计总和
        my_sum = float(0)
        while 1:
            lines = article_file.readlines(10000)   #每次读一万行
            if not lines:
                break
            for line in lines:
                Count += 1
                my_list = line.split("\t")
                #print(my_list[0], len(my_list[0]), my_list[1][:-1], len(my_list[1][:-1]))
                article_list.append(my_list[1][:-1])
                #print(my_list[1][:-1])
                try:
                    tot_sum += float(my_list[1][:-1])
                except:
                    #print("failed")
                    print(my_list)
                    tot_sum += float(my_list[2][:-1])       #那一行有两个制表符。这个情况会在报告中详细说明
    for i in range(int(Count/10)):
        my_sum += float(article_list[i])
    print("前 %10 的文章的PageRank值之和占总和的 %", my_sum/tot_sum*100)

    #处理veneue
    with open("venue_rank.txt", 'r', encoding='utf-8') as venue_file:
        venue_list = []
        Count = 0       #计数，统计行数
        tot_sum = 0
        tot_sum = float(tot_sum)        #统计总和
        my_sum = float(0)
        while 1:
            lines = venue_file.readlines(10000)   #每次读一万行
            if not lines:
                break
            for line in lines:
                Count += 1
                my_list = line.split("\t")
                #print(my_list[0], len(my_list[0]), my_list[1][:-1], len(my_list[1][:-1]))
                venue_list.append(my_list[1][:-1])
                tot_sum += float(my_list[1][:-1])
    for i in range(int(Count/10)):
        my_sum += float(venue_list[i])
    #print(Count)
    #print(tot_sum)
    print("前 %10 的论文的PageRank值之和占总和的 %", my_sum/tot_sum*100)