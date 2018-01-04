# -*- coding: utf-8 -*-
import tokenize
def list_case():
    arr = [i for i in xrange(10) if i % 2 == 0]
    print arr


def list_case_1():
    seq = ['one', 'two', 'three']
    for i, ele in enumerate(seq):
        #seq[i] = '%d: %s' % (i, seq[i])
        seq[i] = '%d: %s' % (i, ele)
    seq2 = [_1_treatment(i, ele) for i, ele in enumerate(seq)]
    seq3 = ['%d: %s' % (pos, element) for pos, element in enumerate(seq)]
    print seq, seq2, seq3


def _1_treatment(pos, element):
    return '%d: %s' % (pos, element)


def _iter_case_2():
    i = iter('abc')
    print i.next()


def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b


def tok_model():
    reader = open('cases.py').next
    tokens = tokenize.generate_tokens(reader)
    print tokens.next()
    print tokens.next()

if __name__ == '__main__':
    list_case()
    list_case_1()
    _iter_case_2()
    fib = fibonacci()
    print fib.next()
    print fib.next()
    print fib.next()
    print [fib.next() for i in xrange(100)]
    tok_model()


