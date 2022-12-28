import random


def main():
    random_list = []
    list1 = []
    list2 = []
    list3 = []
    n = int(input('Input amount of numbers in list: '))
    for i in range(n):
        random_list.append(random.randint(0, 100))
    print(f'The list of random numbers: {random_list}')

    for i in range(1, n, 2):
        list1.append(random_list[i])
    print(f'The first list: {list1}')

    for i in range(2, n, 3):
        list2.append(random_list[i])
    print(f'The second list: {list2}')

    for i in range(n-1, -1, -1):
        list3.append(random_list[i])
    print(f'The third list: {list3}')


main()
