from util.test import rep_test_result
from typing import Tuple

class Position:
    """
    Position for CTk objects. 'row' start from 1, 'col' start from 0
    """
    def __init__(self, pos: Tuple[int, int]|str):
        if type(pos) is str:
            self.pos = pos
            return
        self.pos = f'{pos[0]}.{pos[1]}'
    """
    Add two position. For example: 
        '1.2' + '3.4' -> '4.6', 
        '1.10' + '85.54' -> '86.64'
    """
    def __add__(self, other: object) -> object:
        self_r, self_c = self.pos.split('.')
        other_r, other_c = other.pos.split('.')
        return Position((int(self_r) + int(other_r), int(self_c) + int(other_c)))
    
    def __sub__(self, other: object) -> object:
        self_r, self_c = self.pos.split('.')
        other_r, other_c = other.pos.split('.')
        return Position((int(self_r) - int(other_r), int(self_c) - int(other_c)))
    """
    Multiply by other. For example: 
        '1.2' * 2 -> '2.4', 
        '1.10' * 11 -> '11.110'
    """
    def __mul__(self, other: int) -> object:
        self_r, self_c = self.pos.split('.')
        return Position((int(self_r) * other, int(self_c) * other))

    def __eq__(self, other: object) -> bool:
        return self.pos == other.pos
    def __ne__(self, other: object) -> bool:
        return self.pos != other.pos
    
    def __repr__(self) -> str:
        return self.pos

def main():
    pos1 = Position('14.16')
    pos2 = Position((28, 7))
    print(rep_test_result('add Position', pos1 + pos2 == Position((14 + 28, 16 + 7))))
    print(rep_test_result('sub Position', pos1 - pos2 == Position((14 - 28, 16 - 7))))
    print(rep_test_result('mul Position with int', pos1 * 156 == Position((14 * 156, 16 * 156))))
    ret: bool = (
        (pos1 != pos2) and (Position((-10, 10)) == Position((-10, 10))) and 
        (Position((1, 2)) != Position((2, 1))) and (Position((1, 1)) != Position((1, 2))) and
        (Position((2, 2)) != Position((5, 2))))
    print(rep_test_result('equal and not equal', ret))

if __name__ == '__main__':
    main()