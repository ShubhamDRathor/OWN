# # # # # # # def say_hello():#function defination 
# # # # # # #     print("Hello WORLD")



# # # # # # # print("MY NAME ",end="end= ")
# # # # # # # say_hello()#function calling



# # # # # # def say_hello(name):#function defination 
# # # # # #     print("Hello WORLD")
# # # # # #     print(name)



# # # # # # print("MY NAME ")
# # # # # # say_hello("SHUBHAM")#function calling



# # # # # x=7

# # # # # def num():
# # # # #     print(f"x value is : {x}")
# # # # # print(x)
# # # # # num()    




# # # # x=7

# # # # def num():
# # # #     x=3.5
# # # #     print(f"x value is : {x}")
# # # # print(x)
# # # # num()  # 7
# # # # #         x value is : 3.5 



# # # x=7

# # # def num():
# # #     global y ,x  #once declared global it will not use the previous \
# # #     x=3.5        #it will use the new value even out of the function
# # #     y="name"
# # #     print(f"x value is : {x}")
# # #     print(f"x value is : {y}")
# # # print(x)
# # # y="sub"
# # # num()

# # # print(y)
# # # print(x)


# # def add(n1,n2):
# #     total=n1+n2
# #     print(id(n1),id(n2))
# #     print(f"sum of {n1} and {n2} is {total}")


# # n1=int(input("ENter 1st value: "))
# # n2=int(input("ENter 1st value: "))
# # print(id(n1),id(n2))
# #  add(n1,n2)     # ENter 1st value: 10
# # #                 ENter 1st value: 20
# # #                 140717543213784 140717543214104
# # #                 140717543213784 140717543214104       
# # #                 sum of 10 and 20 is 30


# def display1():
#     print("I am in display 1")
#     display2()
#     print("Back in display 1")

# def display2():
#     print("I am in display 2")
#     display3()
#     print("Back in display 2") 
# def display3():
#     print("I am in display 3")
#     print("Going back in display 2")  

# display1() 
# # output:
# #         I am in display 1
# #         I am in display 2
# #         I am in display 3
# #         Going back in display 2
# #         Back in display 2
# #         Back in display 1