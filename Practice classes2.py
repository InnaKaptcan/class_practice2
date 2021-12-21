from abc import ABC, abstractmethod


class ComputerColor(ABC):

    @classmethod
    @abstractmethod
    def __repr__(self):
        return

    @classmethod
    @abstractmethod
    def __mul__(self, other):
        return

    @classmethod
    @abstractmethod
    def __rmul__(self, other):
        return


class Color(ComputerColor):
    def __init__(self, red_level: int, green_level: int, blue_level: int):
        self.R = red_level
        self.G = green_level
        self.B = blue_level

    def __repr__(self):
        END = '\033[0'
        START = '\033[1;38;2'
        MOD = 'm'
        return f'{START};{self.R};{self.G};{self.B}{MOD}●{END}{MOD}'

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.R == other.R and self.G == other.G and self.B == other.B
        else:
            raise ValueError('Недопустимое сравнение')

    def __hash__(self):
        return hash((self.R, self.G, self.B))

    def __add__(self, other):
        if isinstance(other, Color):
            mix = Color(self.R + other.R, self.G + other.G, self.B + other.B)
            return mix
        else:
            raise ValueError('Недопустимое сложение')

    def __radd__(self, other):
        return self + other

    def __mul__(self, c):
        contrast_level = -256*(1 - c)
        F = 259*(contrast_level + 255)/(255*(259 - contrast_level))
        if isinstance(c, float) and 0 <= c <= 1:
            new_color = Color(int(F * (self.R - 128) + 128),
                              int(F * (self.G - 128) + 128),
                              int(F * (self.B - 128) + 128))
            return new_color
        else:
            raise ValueError

    def __rmul__(self, c):
        return self * c


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    red = Color(255, 0, 0)
    print(print_a(red))
