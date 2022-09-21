import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.start = None

    def first_insert_end(self, data):
        a = Node(data)
        if self.start is None:
            self.start = a
            return
        check = self.start
        while check.next is not None:
            check = check.next
        check.next = a

    def second_insert_beg(self, data):
        a = Node(data)
        if self.start is None:
            self.start = a
            return
        a.next = self.start
        self.start = a

    def third_del_end(self):
        if self.start is None:
            print('\nСписок пустой, удаление невозможно')
            return
        if self.eighth_get_size() == 1:
            self.fourth_del_beg()
            return
        check = self.start
        while check.next.next is not None:
            check = check.next
        check.next = None

    def fourth_del_beg(self):
        if self.start is None:
            print('\nСписок пустой, удаление невозможно')
            return

        self.start = self.start.next

    def fifth_insert_index(self, data, ind):
        a = Node(data)
        if self.start is None:
            self.start = a
            return
        if ind == 1:
            self.second_insert_beg(data)
            return
        check = self.start
        numb = 1
        while (numb + 1) != ind:
            check = check.next
            numb = numb + 1
        a.next = check.next
        check.next = a

    def sixth_get_ind(self, ind):
        if self.start is None:
            return 'Список пуст'

        check = self.start
        numb = 1
        while (numb + 1) != ind:
            check = check.next
            numb = numb + 1
        return check.next.data

    def seventh_del_ind(self, ind):
        if self.start is None:
            return 'Список пуст'
        if ind == 1:
            self.fourth_del_beg()

        size = self.eighth_get_size()
        if size == 'Список пуст':
            print(self.eighth_get_size())
            return
        if size == ind:
            self.third_del_end()
            return

        check = self.start
        numb = 1
        while (numb + 1) != ind:
            check = check.next
            numb = numb + 1

        check.next = check.next.next

    def eighth_get_size(self):
        if self.start is None:
            return 'Список пуст'
        check = self.start
        size = 1
        while check.next is not None:
            check = check.next
            size += 1
        return size

    def ninth_del_all(self):
        if self.start is None:
            return 'Список пуст'
        check = self.start
        while check is not None:
            self.fourth_del_beg()
            check = check.next

    def tenth_swap_ind(self, data, ind):
        a = Node(data)
        if self.start is None:
            return 'Список пуст'

        check = self.start
        numb = 1
        while (numb+1) != ind:
            check = check.next
            numb = numb + 1
        a.next = check.next.next
        check.next = a

    def eleventh_check_empty(self):
        if self.start is None:
            return 'Список пуст'
        else: return 'Список не пуст'

    def twelfth_show_all(self):
        if self.start is None:
            print('Список пуст')
            return
        check = self.start
        while check is not None:
            print(check.data, ' ')
            check = check.next
        print('\n')



    def finder_ind(self, data):
        c=1
        check = self.start
        while check is not None:
            if data == check.data:
                return c
            else:
                check = check.next
                c=c+1


def seventeenth_finder_list(a, b):
    size_a = a.eighth_get_size()
    size_b = b.eighth_get_size()

    check_a_start = a.start
    c = False
    for i in range(size_a - size_b + 1):
        check_a = check_a_start
        check_b = b.start
        if (check_b.data == check_a.data):
            for j in range(size_b):
                if (check_a.data == check_b.data):
                    check_a = check_a.next
                    check_b = check_b.next
                    c = True
                else:
                    c = False
        if not c:
            check_a_start = check_a_start.next

    if c:
        print('Список входит в искомый на позиции ', a.finder_ind(check_a_start.data))
    else:
        print('Список не является частью искомого')

def menu():
    time.sleep(0)
    print('\nВыберите пункт из меню:\n'
          '--------------------------------\n'
          '1.добавление в конец списка\n'
          '2.добавление в начало списка\n'
          '3.удаление последнего элемента\n'
          '4.удаление первого элемента\n'
          '5.добавление элемента по индексу\n'
          '6.получение элемента по индексу\n'
          '7.удаление элемента по индексу\n'
          '8.получение размера списка\n'
          '9.удаление всех элементов списка\n'
          '10.замена элемента по индексу на передаваемый элемент\n'
          '11.проверка на пустоту списка\n'
          '12.посмотреть список\n'
          '17.поиск первого вхождения другого списка в список\n'
          '--------------------------------\n')


def main():
    ind = -1
    a = List()
    b = List()
    while ind:
        menu()
        try:
            ind = int(input('Выбор: '))
        except:
            print('Введено некорректное значение')
        if ind == 0:
            return 0
        if ind == 1:
            x = input('Введите слово, которое хотите вставить в конец списка: ')
            a.first_insert_end(x)
        elif ind == 2:
            x = input('Введите слово, которое хотите вставить в начало списка: ')
            a.second_insert_beg(x)
        elif ind == 3:
            a.third_del_end()
        elif ind == 4:
            a.fourth_del_beg()
        elif ind == 5:
            size = a.eighth_get_size()
            if size == 'Список пуст':
                print(a.eighth_get_size())
            else:
                x = input('Введите слово, которое хотите вставить по индексу: ')
                check = int(input('По какому индексу необходимо изменить слово: '))
                if (check > size) | (check < 1):
                    print('Введен некорректный индекс')
                else:
                    a.fifth_insert_index(x, check)
        elif ind == 6:
            size = a.eighth_get_size()
            if size == 'Список пуст':
                print(a.eighth_get_size())
            else:
                check = int(input('По какому индексу необходимо отобразить слово: '))
                if (check > size) | (check < 1):
                    print('Введен некорректный индекс')
                else:
                    print(a.sixth_get_ind(check))
        elif ind == 7:
            size = a.eighth_get_size()
            if size == 'Список пуст':
                print(a.eighth_get_size())
            else:
                check = int(input('По какому индексу необходимо удалить слово: '))
                if (check > size) | (check < 1):
                    print('Введен некорректный индекс')
                else:
                    print(a.sixth_get_ind(check))
                    a.seventh_del_ind(check)
        elif ind == 8:
            print('Размер списка: ', a.eighth_get_size())
        elif ind == 9:
            a.ninth_del_all()
        elif ind == 10:
            size = a.eighth_get_size()
            if size == 'Список пуст':
                print(a.eighth_get_size())
            else:
                check = int(input('По какому индексу необходимо изменить слово: '))
                if (check > size) | (check < 1):
                    print('Введен некорректный индекс')
                else:
                    word = input('На какое слово необходимо заменить: ')
                    a.tenth_swap_ind(word, check)
        elif ind == 11:
            print(a.eleventh_check_empty())
        elif ind == 12:
            a.twelfth_show_all()
        elif ind == 17:
            b.ninth_del_all()
            if (a.eighth_get_size() == 'Список пуст'):
                print(a.eighth_get_size())
            else:
                while ind != '0':
                    print('Для окончания ввода введите 0')
                    ind = input('Введите слово, которое необходимо вставить в начало списка: ')
                    if ind != '0':
                        b.second_insert_beg(ind)
                seventeenth_finder_list(a,b)



        else: print('Выберите значение из меню\n')

main()