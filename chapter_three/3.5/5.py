from typing import List
from functools import total_ordering


@total_ordering
class StringText:
    def __init__(self, lst_words: List[str]):
        self.lst_words = lst_words
        self._len = len(lst_words)

    def __len__(self):
        return self._len

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]

new_stich = [i.strip("–?!,.;").split() for i in stich]
lst_text = [StringText(i) for i in new_stich]
lst_text_sorted = [' '.join(i.lst_words) for i in sorted(lst_text[:], reverse=True, key=lambda x: len(x))]
