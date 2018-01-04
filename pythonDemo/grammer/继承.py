class Animal(object):
    def run(self):
        print "hello Animal"

    def run_twice(self, animal):
        animal.run()
        animal.run()


class Dog(Animal):

    def run(self):
        super(Dog, self).run()
        print "hello Dog"

    def run_twice(self, animal):
        super(Dog, self).run_twice(animal)


class Cat(Animal):
    pass

# dog = Dog()
# dog.run()

"""
继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
"""
animal = Animal()
animal.run_twice(Dog())
