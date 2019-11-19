# class Dog:
#     def __init__(self,name,kinds,color):
#         self.name = name
#         self.kinds = kinds
#         self.color = color
#
#     def eat(self,food):
#         print('%s正在吃%s' % (self.name,food))
#
#     def run(self,speed):
#         print('%s的%s正在以%skm/h的速度飞奔' %(self.color,self.kinds,speed))
#
# #创建两个Dog对象
# #调用__init__
# wangcai = Dog('旺财','中华田园犬','黄色')
# wangcai.eat('骨头')
# wangcai.run(40)

# 创建一个列表 在列表中保存3条学生记录
# stu01 = Student('无忌',80,28)
# stu01.name
# list01 = [
#
#     Student('无忌',80,28),
#     Student('赵敏',99,26),
#     Student('芷若',48,24)
# ]
# print(list01[0].name,list01[1].age,list01[2].score)


class ICBC:
    #类变量 总行的钱
    total_money = 1000000
    #类方法
    @classmethod
    #cls保存当前类的地址
    def print_total_money(cls):
        print(id(cls),id(ICBC))
        print(cls.total_money)

    def __init__(self,name,money):
        self.name = name
        self.money = money
        #从总行扣除钱数
        ICBC.total_money -= money

    #查询/操作类中的数据 不要用实例方法
    # def print_total_money(self):
    #     print(ICBC.total_money)

i01 = ICBC('北京天坛支行',100000)
i02 = ICBC('北京万寿路支行',100000)
ICBC.print_total_money()
# 非主流：通过对象访问类成员
# i02.print_total_money()
























































