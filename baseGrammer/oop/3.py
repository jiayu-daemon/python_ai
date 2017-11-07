#OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类
#而被继承的class称为基类，父类或超类(Base class、Super class)

class Animal(object):
    def run(self):
        print("Animal is running...")

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

#多态:当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，
#在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态
dog = Dog()
dog.run()

cat = Cat()
cat.run()
#判断一个变量是否是某个类型可以用isinstance()判断
