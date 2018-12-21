# A：我没有偷砖石          thief!=A    chr(64+1)
# B：D就是罪犯              thief==D   chr(64+3)
# C：B是盗窃这块砖石的罪犯  thief==B   chr(64+2)
# D：B有意诬陷我            thief!=D   chr(64+2)
# 假设只要一个人说的是真话，编程序判断谁偷走了砖石。

for i in range(1,4):
    if 1==((i!=1)+(i==3)+(i==2)+(i!=2)):
        str=chr(64+i)+"偷走了砖石"
        print(str)

