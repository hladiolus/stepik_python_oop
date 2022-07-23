import sys


class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))
head_obj = ListObject(lst_in[0])

current_obj = head_obj

for i in lst_in[1:]:
    new_obj = ListObject(i)
    current_obj.link(new_obj)
    current_obj = new_obj
