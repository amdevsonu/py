def f():
    c=4
    def f1():
        print(c)
        c=8
    f1()
f()