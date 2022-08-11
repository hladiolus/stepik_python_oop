from typing import Tuple, List


class Morph:
    def __init__(self, *words):
        self.words: List[str] = list(words)

    def add_word(self, word: str) -> None:
        self.words.append(word)

    def get_words(self) -> Tuple[str]:
        return tuple(self.words)

    def __eq__(self, other):
        if isinstance(other, str):
            return other.lower() in self.words


dict_words = [
    Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях'),
    Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
    Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'),
    Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'),
    Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')
]

text = input()

counter = 0
for i in text.split():
    replaced = i.strip('!,?-_.')
    for j in dict_words:
        if replaced == j:
            counter += 1
            break
print(counter)
