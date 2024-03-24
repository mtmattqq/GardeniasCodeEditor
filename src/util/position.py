from test import rep_test_result

class Position:
    """
    Position for CTk objects. 'row' start from 1, 'col' start from 0
    """
    def __init__(self, row: int, col: int):
        self.pos = f'{row}.{col}'
    """
    Add two position. For example: 
        '1.2' + '3.4' -> '4.6', 
        '1.10' + '85.54' -> '86.64'
    """
    def __add__(self, other: object) -> object:
        self_r, self_c = self.pos.split('.')
        other_r, other_c = other.pos.split('.')
        return Position(int(self_r) + int(other_r), int(self_c) + int(other_c))
    
    def __sub__(self, other: object) -> object:
        self_r, self_c = self.pos.split('.')
        other_r, other_c = other.pos.split('.')
        return Position(int(self_r) - int(other_r), int(self_c) - int(other_c))
    """
    Multiply by other. For example: 
        '1.2' * 2 -> '2.4', 
        '1.10' * 11 -> '11.110'
    """
    def __mul__(self, other: int) -> object:
        self_r, self_c = self.pos.split('.')
        return Position(int(self_r) * other, int(self_c) * other)

    def __eq__(self, other: object) -> bool:
        return self.pos == other.pos
    def __ne__(self, other: object) -> bool:
        return self.pos != other.pos

def main():
    pos1 = Position(14, 16)
    pos2 = Position(28, 7)
    print(rep_test_result('add Position', pos1 + pos2 == Position(14 + 28, 16 + 7)))
    print(rep_test_result('sub Position', pos1 - pos2 == Position(14 - 28, 16 - 7)))
    print(rep_test_result('mul Position with int', pos1 * 156 == Position(14 * 156, 16 * 156)))

if __name__ == '__main__':
    main()