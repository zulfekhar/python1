# def args_here(*args, **kwargs ):
#     print(args)
#     print(kwargs)

# args_here(101, 102, 103 , name = 'steve')



# maps

# find square

# def square(a):
#     return a * a

# # print(square(4))

# square_list = [4, 6, 8, 19, 10]

# # for num in square_list:
# #     print(square(num))


# # using MAPS

# result = (list(map(square,square_list)))
# print(result)




# CLASSES
# class sample():
#     pass

# print(sample)


# class facebook():
#     def __init__():
#         print("Hello user, Please Login")

# newphone = facebook('')


class dog():
    def __init__(self, breed, color, height):
        self.breed = breed
        self.color = color
        self.height = height

tommy = dog('lab', 'White', '3')
print(tommy.breed)
print(tommy.color)
print(tommy.height)
