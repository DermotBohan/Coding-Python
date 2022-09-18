

def f1(f):
    def f2():
        print('This is before the function call')
        f()
        print('This is after the function call')
    return f2

@f1
def f3():
    print('This is f3')


# f3 = f1(f3)
# f3()


f3()
