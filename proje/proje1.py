
l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
n = []

def flatten(x):
    for i in x: 
        if(type(i)==list):
            flatten(i)
        else:
            n.append(i)
            
flatten(l)
print(n)