import itertools
from itertools import groupby

def starting_at_five():
    value = raw_input().strip()
    while value != '':
        for e1 in itertools.islice(value.split(), 4, None):
            yield e1
        value = raw_input().strip()


def with_head(iterable, headsize = 1):
    a, b = itertools.tee(iterable)
    return list(itertools.islice(a, headsize)), b


def compress(data):
    return ((len(list(group)), name)
                for name, group in groupby(data))


def decompress(data):
    return (car * size for size, car in data)


if __name__ == '__main__':
    # iter = starting_at_five()
    # print iter.next()

    seq = [1,2,3,4]
    print with_head(seq)
    print with_head(seq, 5)

    print list(compress('get uuuuuuuuuuuuuuuuuuuuuuuuuuuuupppp'))
    compressed = compress('get uuuuuuuuuuuuuuuuuuuuuuuuuuuuupppp')
    print ''.join(decompress(compressed))