# from collections import deque

"""Создаем Стек"""


class Stack:
    def __init__(self, list_):
        self.list_ = list(list_)

    def is_empty(self):
        if len(self.list_) == 0:
            return True
        else:
            return False

    def push(self, el):
        el = str(el)
        self.list_.append(el)

    def pop(self):
        if not self.is_empty():
            pop_el = self.list_.pop(-1)
        else:
            pop_el = None
        return pop_el

    def peek(self):
        if not self.is_empty():
            peek_el = self.list_[-1]
        else:
            peek_el = None
        return peek_el

    def is_list(self):
        list__ = self.list_
        return list__


"""Создаем метод проверки скобок на симметричность"""


def is_brackets_balanced(str_with_brackets):

    stack_origin = Stack(str_with_brackets)
    new_stack = Stack('')
    counter = 0
    while not stack_origin.is_empty():
        counter += 1
        brackets = {')': '(', '}': '{', ']': '['}

        if stack_origin.peek() in brackets.keys():
            val = stack_origin.pop()
            new_stack.push(val)

        if stack_origin.peek() in brackets.values():
            if brackets[new_stack.peek()] == stack_origin.peek():
                new_stack.pop()
                stack_origin.pop()
            else:
                print('Несбалансированно')
                break

    else:
        if new_stack.is_empty():
            print('Cбалансированно')
        else:
            print('Несбалансированно')


"""Проверяем метод"""

if __name__ == '__main__':

    test_cases = ['(((([{}]))))',
                  '[([])((([[[]]])))]{()}',
                  '{{[()]}}',
                  '}{}',
                  '{{[(])]}}',
                  '[[{())}]'
                  ]

    for case in test_cases:
        is_brackets_balanced(case)
