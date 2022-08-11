from typing import Tuple, List


class MaxPooling:
    def __init__(self, step: Tuple[int, int], size: Tuple[int, int]):
        self.step = step
        self.size = size

    def get_square_elements(self, matrix: List[List[int]], pos: Tuple[int, int]):
        result = []
        for x in range(self.size[0]):
            new_x = pos[0] + x
            for y in range(self.size[1]):
                new_y = pos[1] + y
                result.append(matrix[new_y][new_x])
        return result

    def __call__(self, matrix: List[List[int]]) -> List[List[int]]:
        if not isinstance(matrix, list):
            raise ValueError("Неверный формат для первого параметра matrix.")
        if not matrix:
            return []

        m_len = len(matrix)

        for row in matrix:
            if not isinstance(row, list) or len(row) != m_len:
                raise ValueError("Неверный формат для первого параметра matrix.")
            for element in row:
                if not isinstance(element, (int, float)):
                    raise ValueError("Неверный формат для первого параметра matrix.")

        x, y = 0, 0
        res = []
        while y < int(m_len / self.step[1]):
            res.append([])
            while x < int(m_len / self.step[1]):
                sq_elements = self.get_square_elements(matrix, (x * self.step[0], y * self.step[1]))
                if sq_elements:
                    res[-1].append(max(sq_elements))
                x += 1
            x = 0
            y += 1
        return res
