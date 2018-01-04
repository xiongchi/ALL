# -*- coding: utf-8 -*-
class yieldtest1(object):

    def power(self, values):
        for value in values:
            print 'powering values %s'%value
            yield value


    def adder(self, values):
        for value in values:
            print 'adding to %s'%value
            if value % 2 == 0:
                yield value + 3
            else:
                yield value + 2


class yieldtest2(object):

    def psychologist(self):
        print 'please tell me your problem'
        while True:
            answer = (yield)
            if answer is not None:
                if answer.endswith('?'):
                    print "Don't ask yourself too much questions"
                elif 'good' in answer:
                    print "that's great, go on"
                elif 'bed' in answer:
                    print "Don't be negative"


class yieldtest3(object):

    def my_generator(self):
        try:
            yield 'something'
        except ValueError:
            yield 'value error'
        finally:
            print 'close'


if __name__ == '__main__':
    eles = [1, 4, 7, 8, 9]
    yt1 = yieldtest1()
    res = yt1.adder(yt1.power(eles))
    print res.next()
    print res.next()
    #res.next()调用一次向下移动一位
    #当超过eles的长度后 抛出StopIteration的异常
    print [res.next() for i in xrange(3)]

    free = yieldtest2().psychologist()
    free.next()
    free.send("what should I do ?")
    free.send("I feel bed")
    free.send("I feel good")

    y3 = yieldtest3().my_generator()
    print y3.next()
    print y3.throw(ValueError('emmm'))
    y3.close()


