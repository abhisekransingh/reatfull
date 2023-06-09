

# def m1(n):
#     ticket=['user1','user2','user3','user4','user5']
#     b={}
#     c=1
    
    
#     for i in n:
#         if 'user'+str(c) not in ticket:
#             break
#         b['user'+str(c)]=i
#         n.append(i)
#         c=c+1
#     print(b)
# m1([1,2,3])
# import copy
# l=[1,2,3,4,5]
# l3 =l.copy()
# l.append(10)
# print(l)
# print(l3)



# def outer(fun):
#     def inner(name):
#         if name=="MR":
#               print('MR'+name)
              
#         else:
#             fun(name)
#     return inner


# @outer
# def main(name):
#     print('MRS'+name)
# main('MR')


# def m1(a):
#     max=0
#     min=len(a)
#     if(type(a)!=list):
#         print('error')

#     elif len(a)>5:
#         for i in a:
#             if i>max:
#                 max=i
                
#         return max
        
#     else:
#         for i in a:
#             if i<min:
#                 min=i
#         return min

# b=range(1,10)
# a = list((lambda x: x ** 3, b))21
# a=[1,2,3,4,5,6,9,79]
# # l=set(a)
# b=len(a)
# c=0
# d=0
# for i in a:
#     if c==b-1:
#         break
#     elif(i>d):
#         d=i
#         c=c+1
# print(d)

# class A():
#     def m1():
#         print('Abhisek')
# class B(A):
#     def m2():
#         print('Abhisek')

# o=B()
# o.m2()

# def m1():
#     print(10)

# if __name__=='__main__':
#     m1()
# def decor1(fun):
#     def inner(value):
#         b=0
#         for i in value:
#             if i>0:
#                 b=b+i
#         print(b)
#         return b
#     return inner
    





# @decor1
# def m1(a):
#     print(a)
# a=m1([0,1,2,3])
# print(a)








    


    














