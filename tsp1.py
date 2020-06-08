import random

def sum_path(way,c,k):
    x = 0
    path = ''
    for i in range(0,len(way)-1):
        m=way[i]
        n=way[i+1]
        x += c[m][n]
        path = path + str(m) + '-->'
    path =path + str(way[-1]) + '-->' + str(k)
    x += c[k][way[-1]]
    print('所需最小旅费为： '+str(x))
    print('路线为：' + path)
#描绘最后的路线及计算所需旅费 

def find_path(x,c):
    way = []
    way.append(x)
    now_spot = x
    for k in range(0,14):
        now_spot_lenlist = c[now_spot][:]
        cp_list = c[now_spot][:]
        for l in way:
            now_spot_lenlist.remove(c[now_spot][l])
            cp_list[l] = 'N'
        min_e = min(now_spot_lenlist)
        now_spot = cp_list.index(min_e)
        way.append(now_spot)
    return way
#找路径的函数

for z in range(0,10):
    c=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for x in range(0,15):
        for y in range(0,15):
            c[x].append(random.randint(1,15))
    for x in range(0,15):
        for y in range(0,15):
            c[x][y]=c[y][x]
    for i in range(0,15):
        c[i][i]=0
    for i in range(0,15):
        print(c[i])
    #生成一个tsp问题
    way = find_path(0,c)
    sum_path(way,c,0)


        
        





    




    
