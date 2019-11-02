'''a=[1,2,3,4,"hello","世界"]#索引列表形式
print(type(a))
print(a[4])
a[1]='keyon'
print(a)

print(a[0:5])#切片和逆向切片

a.insert(3,'earth')
print(a)

del a[2:3]
print(a)

a.pop(0)
print(a)

print(len(a))'''

'''k={'name':"张三","age":14,"hobby":'打球'}
print(k["age"])'''

'''a={1,2,3,4,5,'上山打老虎'}
b=set([1,2,3,4,5])
print(b)

print(type(b))'''

'''list1=[1,22,3,4,4,5,5,7]
x=set(list1)
y=list(x)

list1=y
print(list1)
'''

#a={1,2,3,4,5}
'''b={6,7,4,5,8}
print(b-a)
print(b|a)
print(a&b)'''

 


		
'''for i in range(50,100,3):

	print(i)'''

'''i=0
while i<=100:
	print(i)
	if i==50:
		print('rest time')
	i=i+1'''
'''


i=0
summ=0
while i<=20:
	summ=summ+1.2
	print("第",i,"年 ")
	i=i+1
'''

#无限循环
'''
import time
i=1
while 1==1:
	print(i)
	i=i+1
	time.sleep(1)
'''

card1="1001"
pwd1="123456"
ban1="10000"

card2="1002"
pwd2="123456"
ban2="10000"

card3="1003"
pwd3="123456"
ban3="10000"


print("欢迎来到Python银行！")
times=0
while True:
	card=input("请输入银行卡号:")
	pwd=input("请输入密码：")

	ban=0

	if card==card1 and pwd==pwd1:
		ban=ban1
	elif card==card2 and pwd==pwd2:
		ban=ban2
	elif card==card3 and pwd==pwd3:
		ban=ban3
	else:
		times=times+1
		if times>=3:
			print("您已经3次输入错误，请联系银行柜台")
			break
		else:
			print("卡号输入错误!,请重新输入")
			continue

	while True:
		input("请输入要办理的业务：1出款 2取款 3退卡")
		if num=="1":
			inn=float(input("请输入存款金额："))
			if inn<=0:
				print("存款金额大于0！")
			else:
				ban=ban+inn
				print("存款成功！存入：",inn,"余额：",ban)
		elif num=="2":
			out=float(iput("请输入取款金额："))
			if out>ban:
				print("余额不足")
				continue
			else:
				ban=ban-out
				print("取款成功！取出：",out,"余额",ban)	
				break
		else:
			print("输入错误")
			continue
