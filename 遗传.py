import random
import copy
import numpy as np
best_answer = []
#初始化群体，群体的规模为5，每个染色体为（x1,x2,x3,x4)的形式表示
#返回群体中的染色体矩阵
def init():
    x = (np.mat(np.random.rand(5, 4)))
    x *= 10
    x -= 5
    print('随机生成染色体：')
    print(x)
    return x
#方程为f（x）= 1/（x1^2+x2^2+x3^2+x4^4+1)
#把每个群体中的染色体代入方程中，得到每个群体中染色体的适应值
#返回每个染色体的适应值
def adapt(x):
    f = []
    for i in x:
        k = 0
        for j in i:
            k += pow(j, 2)
        k += 1
        k = 1 / k
        f.append(k)
    return f
#把适应值求和，求出每个染色体适应值与总和的比
#返回每个染色体适应值与总和的比
def select(f):
    sum = 0
    f1 = []
    for i in f:
        sum += i
    print(f)
    print('群体适应性的总和：')
    print(sum)
    for i in f:
        i /= sum
        f1.append(i)
    print('单体适应性值与群体适应性的总和的比：')
    print(f1)
    return f1
#随机产生随机数，再与染色体适应值比，判断是否选中该染色体
#返回选中后的染色体
def select1(f, x):
    f1 = f.copy()
    c = np.random.rand(1,5).tolist()
    print('每组染色体的随机数')
    print(c)
    C = []
    f2 = []
    for i in c:
        sum = 0
        for k,j in enumerate(i):
            sum += f1[k]
            f1[k] = sum     #适应值的和
            C.append(j)
    for i in C:
        for j in range(len(f1)):
            if i < f1[j]:
                f2.append(f1.index(f1[j]))  #得到选中染色体的坐标
                break;
    x1 = x.copy()
    for i,j in enumerate(f2):
        x1[i] = x[j]       #得到种群
    print('选择后得到的种群：')
    x1 = np.around(x1, decimals = 4)
    print(x1)
    return x1
#交配率为0.85，随机产生每个染色体的随机数，判断是否参与交配
#在参与交配的染色体中再随机产生作为交配的交配位进行交配
#返回交配后的新群体
def copulation(f):
    f1 = []
    f2 = []
    c = np.random.rand(1, 5).tolist()
    print('随机产生的交配概率与0.85对比：')
    print(c)
    for i in c:
        for j in i:
            if j < 0.85:     #交配概率
                f1.append(i.index(j))  #交配的染色体位置
    for i in f1:
        f2.append(f[i])           #交配的染色体
    print('需要交配的染色体组：')
    print(f2)
    print('每两组分别随机产生的交配位：')
    for i in range(len(f1)):
        if i % 2 != 0:
            rand = random.randint(0,3)      #随机产生交配位
            print(rand)
            for k in range(rand + 1, len(f2[0])):
                f2[i-1][k],f2[i][k] = f2[i][k],f2[i-1][k] #交配
    for i,j in enumerate(f1):
        f[j] = f2[i]
    print('交配后的种群：')
    print(f)
    return f
#变异的概率为0.1，每个染色体的每个基因都有可能会产生变异
#随机对应染色体的基因产生随机数，判断是否变异，
#如果变异，再在变异的基因上，随机产生一个基因接受范围的数
#返回变异后的新群体
def variation(f):
    c = np.random.rand(5, 4) #染色体生成随机数
    print('每组染色体的每个基因随机生成的随机数：')
    print(c)
    c = np.where(c < 0.1, -1, c)  #判断随机数小于0.1为变异
    print('随机数小于0.1的为变异，变异的随机数变为-1')
    print(c)
    #print(f)
    for n, i in enumerate(c):
        if -1 in i:
            for m, j in enumerate(i):
                if j == -1:
                    #print('变异的位置：', n, m)
                    f[n][m] = np.random.rand()* 10 - 5  #随机数替代变异数
    print('变异染色体替换后：')
    print(f)
    return f



if __name__ == '__main__':
    print('遗传算法开始：')
    print('算法开始：')
    x = init()            #返回群体的染色体
    x = x.tolist()        #转成列表形式
    f = adapt(x)          #返回每个染色体的适应值
    best = max(f)         #每个染色体的适应值的最优值
    print("Best的染色体：",best)
    print('每个染色体的适应性评价:')
    print(f)
    for i in range(1000):   #算法迭代一千次
        f1 = select(f)   #返回染色体适应值的比
        c = select1(f1, x)   #返回选择染色体后的种群
        C = copulation(c)     # 返回交配后的种群
        x = variation(C)      #返回变异后的种群
        f = adapt(x)          #重新评估适应值
        best1 = max(f)        #选择变异后的最优适应值
        print('重新每个染色体的适应性评价:')
        print(f)
        print('判断染色体：', max(f))
        print('判断染色体与Best染色体比较')
        if best < best1:      #判断每次变异后的最有适应值与选择出来的适应值，哪个更优，选择最优的那个
            best = best1
        print(best)
        if i != 20 -1:
            print('第', i + 1, '次循环：')
        best_answer.append(best)
    print('循环100次的所有最大值：')
    #print(best_answer)
    print('最优解为：',best)