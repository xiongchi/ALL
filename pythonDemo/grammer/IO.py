
try:
    f = open('test.txt', 'w')
    f.write('hello world')
finally:
    if f:
        f.close()

"""
相当于上方try: finally:
"""
with open('test.txt', 'r') as f:
    print f.read()
