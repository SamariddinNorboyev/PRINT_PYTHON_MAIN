# def uppercase_decorator(func):
#     def wrapper(message):
#         result = func(message)
#         return result
#
#     return wrapper
#
#
# @uppercase_decorator
# def salom_ber(message):
#     return f"Salom {message}"
#
# print(salom_ber("Junyo"))
from time import clock_settime


# import time
#
# def time_decorate(func):
#     def wrapper(message):
#         start = time.time()
#         result = func(message)
#         end = time.time()
#         return f"{end-start} vaqt davomida {func.__name__} ishladi! Natija - {result}"
#     return wrapper
#
# @time_decorate
# def factorial(x):
#     f = 1
#     for i in range(1, x):
#         f = f*i
#     return f
#
# print(factorial(10))

# class UppercaseAttributes:
#     def __init__(self, cls):
#         self.cls = cls
#
#     def __call__(self, *args, **kwargs):
#         obj = self.cls(*args, **kwargs)
#
#         for attr in dir(obj):
#             if not attr.startswith("__") and isinstance(getattr(obj, attr), str):
#                 setattr(obj, attr, getattr(obj, attr).upper())
#
#         return obj
#
# @UppercaseAttributes
# class User:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city
#
# user = User(12, "Tashkent")
# print(user.name)
# print(user.city)

#1
#Faqat musbat sonlarni qabul qiluvchi dekorator
# def only_positive(func):
#     def wrapper(num):
#         if num<0:
#             return "Xatolik"
#         elif num>0:
#             return func(num)
#         elif num == 0:
#             return "Bu son 0"
#     return wrapper
#
# @only_positive
# def square(num):
#     return num ** 2
#
# print(square(5))
# print(square(-3))



#2
#Funksiya neci marta chaqirilganini hisobga oluvchi dekorator
# d = 0
# def count_calls(func):
#     def wrapper():
#         func()
#         global d
#         d += 1
#         return f"{func.__name__} - {d} marta chaqirilgan"
#     return wrapper
#
# @count_calls
# def hello():
#     print("Hello")
#
# print(hello())

#5
#Funksiya maksimal 3 marta chaqirilishi kerakd
# d = 0
# def call_limit(func):
#     def wrapper():
#         global d
#         if d<3:
#             d+=1
#             func()
#         elif d>=3:
#             print(f"{func.__name__}ni chaqiruvlar limiti oshdi")
#         return 0
#     return wrapper
#
# @call_limit
# def process_data():
#     print("Ma'lumotlar qayta ishlanmoqda...")
#
# process_data()
# process_data()
# process_data()
# process_data()
# process_data()
# process_data()

print('Salom')
print('Salom')
print('Salom')
print('Salom')
print('Salom')
print('Salom')