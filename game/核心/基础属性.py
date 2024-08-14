from abc import ABC, abstractmethod, abstractproperty

# 其实就是抽象类，按理说基础类应该就是object才对，但是考虑到抽象类不好理解，所以在这里直接是用基类命名了，也就是基础类，基础类定义的基础方法都得实现
# 已弃用，留着用于注释把
基础类 = ABC
类基础方法 = abstractmethod
类基础属性 = abstractproperty

# 已弃用，留着用于注释把
类属性 = property
静态方法 = staticmethod
类方法 = classmethod


数据类型 = type

基础异常 = Exception


获取数据长度 = len
