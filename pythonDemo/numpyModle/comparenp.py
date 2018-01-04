import time
from math import *
import numpy as np


def f(x):
    return 3*log(x) + cos(x) ** 2
loops = 25000000
# begin = time.time()
# for i in range(1, loops):
#     r = f(i)
# end = time.time()
# print str(end - begin)

begin = time.time()
for i in np.arange(1,loops):
    f(i)
end = time.time()
print str(end - begin)