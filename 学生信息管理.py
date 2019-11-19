class StudentModel:
    '''
    学生模型
    '''
    #id不需要传值 放在最后一位
    def __init__(self, name="", age=0, score=0,id=0):
        '''
        创建学生对象
        :param id: 编号 该学生的唯一标识
        :param name: 姓名 str
        :param age: 年龄 int
        :param score: 成绩 int
        '''
        self.id = id
        self.name = name
        self.age = age
        self.score = score

class StudentManagerController:
    '''
    学生管理控制器 处理业务逻辑
    '''
    __stu_id = 1000
    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self,stu):
        #为学生设置id 递增
        stu.id = StudentManagerController.__stu_id + 1
        #将学生添加到学生列表
        self.__stu_list.append(stu)

    def remove_student(self,id):
        for item in self.stu_list:
            if item.id == id:
                self.stu_list.remove(item)
                return  True
        raise ValueError('删除失败：id错误')

    def update_student(self,stu):
        for item in self.__stu_list:
            if item.id == stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return  True
        raise ValueError('未找到对应学员')






        #根据成绩排序
    def order_by_score(self):
        for i in range(len(self.__stu_list)-1):
            for c in range(i+1,len(self.__stu_list)):
                if self.stu_list[i].score > self.__stu_list[c].score:
                    self.stu_list[i],self.stu_list[c] = \
                        self.stu_list[c],self.stu_list[i]




#界面视图
class StudentManagerView:
    def __init__(self):
        self.__manager = StudentManagerController()
    def __display_menu(self):
        print('+--------------------------+')
        print('| 1)添加学生信息             |')
        print('| 2)显示学生信息             |')
        print('| 3)删除学生信息             |')
        print('| 4)修改学生信息             |')
        print('| 5)按照成绩升序排序          |')
        print('+--------------------------+')

    def __select_menu(self):
        option = input('请输入：')

        if option == '1':
            pass

        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        elif option == '5':
            pass

    def main(self):
        '''
        界面入口
        :return:
        '''
        while True:
            self.__display_menu()
            self.__select_menu()
    #输入学生__input_students
    def __input_students(self):
        name = input('请输入学生姓名')
        age = int(input('请输入学生年龄'))
        score = int(input('请输入学生成绩'))
        stu = StudentModel(name,age,score)
        self.__manager.add_student(stu)
    #输出学生__output_students
    def __output_students(self,list):
        for item in list:
            print(item.name,item.age,item.score,item.id)

    #删除学生__delete_student
    def __delete_student(self):
        id = int(input('请输入要删除学生的学号：'))
        if self.__manager.remove_student(id):
            print('删除成功')
        else:
            print('删除失败')
    #修改学生信息__modify_student
    def __modify_student(self):
        id = int(input('请输入要修改学生的学号'))
        name = input('请输入新的学生姓名：')
        age = int(input('请输入新的学生年龄'))
        score = int(input('请输入新的学生成绩'))
        stu = StudentModel(name,age,score,id)
        if self.__manager.update_student(stu):
            print('修改成功')
        else:
            print('修改失败')

    # 根据成绩排序__output_student_by_socore
    def __output_student_by_socore(self):
        self.__manager.order_by_score()
        self.__output_students(self.__manager.stu_list)
view = StudentManagerView()
# view.display_menu()
view.main()


























































