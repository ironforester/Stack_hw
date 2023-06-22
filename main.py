from data import ballanced_list, unballanced_list
from classStack import Stack, check_balance

if __name__ == '__main__':
    s = Stack()
    print(f'функция is_empty - {s.is_empty()}')
    s.push(1)
    s.push(2)
    s.push(6)
    print(f'функция size - {s.size()}')
    print(f'функция peek - {s.peek()}')
    print(f'функция pop - {s.pop()}')
    print(f'функция pop - {s.pop()}')
    print(f'функция size - {s.size()}')
    print(f'функция pop - {s.pop()}')
    print(f'функция pop - {s.pop()}')
    #
    for row in unballanced_list:
        print(check_balance(row))

    print()
    for row in ballanced_list:
        print(check_balance(row))