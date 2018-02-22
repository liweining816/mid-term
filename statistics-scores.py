# -*- coding: utf-8 -*-
# windows 下如果出现编码问题，将 utf-8 改为 cp936

f = open('report.txt')#打开成绩单文件report.txt
lines = f.readlines()
f.close()

total_score = []#设置班级的总成绩为一个空列表
for l in lines:
    s = l.split()#把每个学生的成绩拆分成list
    student_sum = 0#每个学生的总成绩赋初值为0
    for i in range(1,10):
        student_sum = student_sum + int(s[i])
    s.append(str(student_sum))#求和并写入
    student_avg = round(student_sum / 9,1)
    s.append(str(student_avg))#求平均并写入
    total_score.append(s)#将每个学生的成绩添加到总成绩列表

s1 =  sorted(total_score, key=lambda total_score: total_score[10])#按总成绩升序排列
total_avg = ['平均']#定义平均成绩列表
for i in range(1,12):
    sum = 0
    for j in range(len(s1)):
        sum = sum + float(s1[j][i])#对单科成绩进行求和
    if i != 11:#如果是平均分求平均，则保留1为小数，其他则取整数
        avg = round(sum/len(s1))
    else:
        avg = round(sum / len(s1),1)
    total_avg.append(str(avg))
s1.append(total_avg)#把平均成绩列表加入到总成绩列表

head = '名次 姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理 总分 平均分'
with open('report1.txt', 'a') as f:  #创建一个新文件report1.txt,写入列头
    f.write(head+'\n')

i = len(s1)#i赋初值为总成绩列表的长度
rank = 0 #名次赋初值为0
while i > 0:
    for j in range(1,12):#替换60分以下的成绩为“不及格”；
        if  float(s1[i-1][j]) < 60:
            s1[i-1][j] = "不及格"
    s = str(rank) + ' ' + ' '.join(s1[i-1])#把处理后的成绩转换成字符串
    with open('report1.txt','a') as f:#写入report1.txt并保存
        f.write(s+'\n')
    if i <= len(s1):#如果两个学生的总成绩相等，则他们的名词也相同
        if s1[i-2][10] != s1[i-1][10]:
            rank += 1
    i -= 1
