# Collatz Conjecture - Start with a number n > 1.
# Find the number of steps it takes to reach one using the following process:
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.


# def collatz(num):
#     counter = 0
#     # Determine if num is > 1
#     while num > 1:
#         # if num is even divide by 2
#         if num % 2 == 0:
#             num = num // 2
#             counter += 1
#         # if num is odd multiply by 3 and add 1
#         else:
#             num = (num * 3) + 1
#             counter += 1
#     return counter
# print(collatz(25))

def re_collatz(num, counter=0):
    if num <= 1:
        return counter
    elif num % 2 == 0:
        return re_collatz(num//2, counter + 1)
    else:
        return re_collatz((num*3) + 1, counter + 1)


print(re_collatz(10))
