#input: [[1, 2], [3, 4], [5, 6, 7]]
#output: [[[7, 6, 5], [4, 3], [2, 1]]

l = [[1, 2], [3, 4], [5, 6, 7]]

def func(x):
    for i in x :
        if (type(i)==list):
            i.reverse()
    x.reverse()

func(l)
print(l)