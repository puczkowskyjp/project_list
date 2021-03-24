def fizzBuzz(num):
    num_list = []
    for number in range(: num):
        if number % 3 == 0:
            num_list.append('fizz')
        elif number % 5 == 0:
            num_list.append('buzz')
        else:
            num_list.append(number)
    return num_list


fizzBuzz(10)
