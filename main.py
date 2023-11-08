import random
from datetime import date

def solution1():
    myList = []
    sum = 0

    for x in range(10):
        myList.append(random.randint(0, 100))

    for x in myList:
        sum += x
    
    print(f'The sum is: {sum}')

def solution2():
    width = input("Enter width: ")
    height = input("Enter height: ")
    length = input("Enter length: ")

    print(f"Volume is: {int(width) * int(height) * int(length)}")

def solution3():
    some_list = input("Enter list of numbers: ")
    some_list = list(map(int, filter(lambda x: x != ',', some_list)))
    if some_list[0] == some_list[-1]:
        print(True)
    else:
        print(False)

def solution4():
    some_string = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
    count = 0

    list_of_words = some_string.split(" ")

    for x in list_of_words:
        if x == "Python":
            count += 1

    print(count)

def solution5():
    myList = [1,2,3]
    mySet = {3,4,5}
    mySet = mySet.union(myList)
    print(mySet)

def solution6():
    my_list = [11, 100, 101, 999, 1001]
    my_list.reverse()
    print(my_list)
    
def solution7():
    some_number = random.randint(1,100)
    if some_number < 10:
        print(f"{some_number}: You lose.")
    elif some_number < 50:
        print(f"{some_number}: Try again.")
    else:
        print(f"{some_number}: You win!")

def solution8():
    myList = [6,2,7,3,77,7,1]
    min_number = myList[0]

    for num in myList:
        if num < min_number:
            min_number = num

    print(min_number)

def solution9():
    input_string = input("Enter string: ")
    print(bool(input_string.isupper()))

def isVowel(letter):
    return letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'

def solution10():
    input_string = input("Enter string: ")
    vowels_freq = len(list(filter(lambda x: isVowel(x), 
                                    input_string.upper())))
    print(f"Vowels: {vowels_freq}")
    print(f"Consonants: {len(input_string) - vowels_freq}")

def solution11():
    some_file = open("output.txt", "w")
    some_file.write(f"Today's date is: {date.today()}")
    some_file.close()

def solution12():
    some_int = input("Enter an integer: ")
   
    if (float(some_int) % 1.0) != 0.0:
        print(f"ERROR: {some_int} is not an integer")
        return

    print(-int(some_int))
    
def solution13():
    continue_iterating = True

    while (continue_iterating):
        num1 = input("Enter first integer:")
        if num1 == "exit":
            continue_iterating = False
        else:
            num2 = input("Enter second integer: ")
            if num2 == "exit":
                continue_iterating = False
            else:
                print(f"Answer: {int(num1) + int(num2)}")

def solution13_2():
    while (True):
        num1 = input("Enter first integer:")
        if num1 == "exit":
            break
        num2 = input("Enter second integer: ")
        if num2 == "exit":
            break
        print(f"Answer: {int(num1) + int(num2)}")


if __name__ == '__main__':
    # solution1()
    # solution2()
    # solution3()
    # solution4()
    # solution5()
    # solution6()
    # solution7()
    # solution8()
    # solution9()
    # solution10()
    # solution11()
    # solution12()
    # solution13()
    solution13_2()