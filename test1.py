"""
 * Project name(项目名称)：Python运算符重载
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/28 
 * Time(创建时间)： 21:40
 * Version(版本): 1.0
 * Description(描述)：
 重载运算符	含义
__new__	创建类，在 __init__ 之前创建对象
__init__	类的构造函数，其功能是创建类对象时做初始化工作。
__del__ 	析构函数，其功能是销毁对象时进行回收资源的操作
__add__	加法运算符 +，当类对象 X 做例如 X+Y 或者 X+=Y 等操作，内部会调用此方法。
            但如果类中对 __iadd__ 方法进行了重载，则类对象 X 在做 X+=Y 类似操作时，会优先选择调用 __iadd__ 方法。
__radd__	当类对象 X 做类似 Y+X 的运算时，会调用此方法。
__iadd__	重载 += 运算符，也就是说，当类对象 X 做类似 X+=Y 的操作时，会调用此方法。
__or__	“或”运算符 |，如果没有重载 __ior__，则在类似 X|Y、X|=Y 这样的语句中，“或”符号生效
__repr__，__str__	格式转换方法，分别对应函数 repr(X)、str(X)
__call__	函数调用，类似于 X(*args, **kwargs) 语句
__getattr__	点号运算，用来获取类属性
__setattr__	属性赋值语句，类似于 X.any=value
__delattr__	删除属性，类似于 del X.any
__getattribute__	获取属性，类似于 X.any
__getitem__	索引运算，类似于 X[key]，X[i:j]
__setitem__	索引赋值语句，类似于 X[key], X[i:j]=sequence
__delitem__ 	索引和分片删除
__get__, __set__, __delete__	描述符属性，类似于 X.attr，X.attr=value，del X.attr
__len__ 	计算长度，类似于 len(X)
__lt__，__gt__，__le__，__ge__，__eq__，__ne__ 	比较，分别对应于 <、>、<=、>=、=、!= 运算符。
__iter__，__next__	迭代环境下，生成迭代器与取下一条，类似于 I=iter(X) 和 next()
__contains__	成员关系测试，类似于 item in X
__index__ 	整数值，类似于 hex(X)，bin(X)，oct(X)
__enter__，__exit__	在对类对象执行类似 with obj as var 的操作之前，会先调用 __enter__ 方法，
                    其结果会传给 var；在最终结束该操作之前，会调用 __exit__ 方法（常用于做一些清理、扫尾的工作）
 """


class MyClass:  # 自定义一个类
    def __init__(self, name, age):  # 定义该类的初始化函数
        self.name = name  # 将传入的参数值赋值给成员交量
        self.age = age

    def __str__(self):  # 用于将值转化为字符串形式，等同于 str(obj)
        return "name:" + self.name + ";age:" + str(self.age)

    __repr__ = __str__  # 转化为供解释器读取的形式

    def __lt__(self, record):  # 重载 self<record 运算符
        if self.age < record.age:
            return True
        else:
            return False

    def __add__(self, record):  # 重载 + 号运算符
        return MyClass(self.name, self.age + record.age)


if __name__ == '__main__':
    myc = MyClass("Anna", 42)  # 实例化一个对象 Anna，并为其初始化
    mycl = MyClass("Gary", 23)  # 实例化一个对象 Gary，并为其初始化
    print(repr(myc))  # 格式化对象 myc，
    print(myc)  # 解释器读取对象 myc，调用 repr
    print(str(myc))  # 格式化对象 myc ，输出"name:Anna;age:42"
    print(myc < mycl)  # 比较 myc<mycl 的结果，输出 False
    print(myc + mycl)  # 进行两个 MyClass 对象的相加运算，输出 "name:Anna;age:65"
    print(myc > mycl)
    print(mycl < myc)
