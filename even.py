def even_num(x):
    if x%2==0:
        return "number is even"
    else:
        return "number is not even"

num=int(input("enter the number:"))
re=even_num(num)
print(re)
