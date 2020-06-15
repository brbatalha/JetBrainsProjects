class TicTacToe:

    def __init__(self):
        self.m = {}
        self.p = []
        self.t = ''

    def difficulty(self):
        pass

    def print_m(self, m):
        self.m = m
        print('---------')
        print('|', self.m[13], self.m[23], self.m[33], '|')
        print('|', self.m[12], self.m[22], self.m[32], '|')
        print('|', self.m[11], self.m[21], self.m[31], '|')
        print('---------')

    def check_result(self, m):
        self.m = m
        result = ''
        result_x = result_o = 0
        count_x = count_o = count_ = 0
        for c in self.m.values():
            if c == 'X':
                count_x += 1
            elif c == 'O':
                count_o += 1
            elif c == ' ':
                count_ += 1
        if self.m[11] == self.m[12] == self.m[13] == 'X':
            result_x += 1
        if self.m[21] == self.m[22] == self.m[23] == 'X':
            result_x += 1
        if self.m[31] == self.m[32] == self.m[33] == 'X':
            result_x += 1
        if self.m[11] == self.m[21] == self.m[31] == 'X':
            result_x += 1
        if self.m[12] == self.m[22] == self.m[32] == 'X':
            result_x += 1
        if self.m[13] == self.m[23] == self.m[33] == 'X':
            result_x += 1
        if self.m[11] == self.m[22] == self.m[33] == 'X':
            result_x += 1
        if self.m[13] == self.m[22] == self.m[31] == 'X':
            result_x += 1
        if self.m[11] == self.m[12] == self.m[13] == 'O':
            result_o += 1
        if self.m[21] == self.m[22] == self.m[23] == 'O':
            result_o += 1
        if self.m[31] == self.m[32] == self.m[33] == 'O':
            result_o += 1
        if self.m[11] == self.m[21] == self.m[31] == 'O':
            result_o += 1
        if self.m[12] == self.m[22] == self.m[32] == 'O':
            result_o += 1
        if self.m[13] == self.m[23] == self.m[33] == 'O':
            result_o += 1
        if self.m[11] == self.m[22] == self.m[33] == 'O':
            result_o += 1
        if self.m[13] == self.m[22] == self.m[31] == 'O':
            result_o += 1
        if result_x > 0:
            if result_x == result_o:
                result = 'Impossible'
            else:
                result = 'X wins'
        if result_o > 0:
            if result_x == result_o:
                result = 'Impossible'
            else:
                result = 'O wins'
        # if count_ > 0 and result_x == 0 and result_o == 0:
            # result = 'Game not finished'
        if (count_x - count_o) >= 2 or (count_o - count_x) >= 2:
            result = 'Impossible'
        if count_ == 0 and result_x == 0 and result_o == 0:
            result = 'Draw'
        return result

    def check_position(self, p, t):
        self.p = p
        self.t = t
        if len(self.p) == 0:
            check = False
            msg = 'Coordinates should be from 1 to 3!'
            return check, msg
        elif len(self.p) == 1:
            for c in self.p:
                if c.isalpha():
                    check = False
                    msg = 'You should enter numbers!'
                    return check, msg
                else:
                    check = False
                    msg = 'Coordinates should be from 1 to 3!'
                    return check, msg
        elif len(self.p) == 2:
            for c in self.p:
                if c.isalpha():
                    check = False
                    msg = 'You should enter numbers!'
                    return check, msg
                if not c.isalpha():
                    position_dict = int(''.join(p))
                    if position_dict == 11 or position_dict == 12 or position_dict == 13 \
                            or position_dict == 21 or position_dict == 22 or position_dict == 23 \
                            or position_dict == 31 or position_dict == 32 or position_dict == 33:
                        if self.free_cell(position_dict):
                            self.m[position_dict] = self.t
                            check = True
                            return check, self.print_m(self.m)
                        else:
                            check = False
                            msg = 'This cell is occupied! Choose another one!'
                            return check, msg
                    else:
                        check = False
                        msg = 'Coordinates should be from 1 to 3!'
                        return check, msg
        elif len(self.p) > 2:
            for c in self.p:
                if c.isalpha():
                    check = False
                    msg = 'You should enter numbers!'
                    return check, msg
                elif not c.isalpha():
                    check = False
                    msg = 'Coordinates should be from 1 to 3!'
                    return check, msg

    def free_cell(self, p_d):
        if self.m[p_d] == ' ':
            return True


def main():
    game = TicTacToe()
    """starting_game = input('Enter cells: ').strip().upper().replace('_', ' ')
    matriz = []
    for i in starting_game:
        matriz.append(i)"""
    matriz = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display = {13: matriz[0], 23: matriz[1], 33: matriz[2],
               12: matriz[3], 22: matriz[4], 32: matriz[5],
               11: matriz[6], 21: matriz[7], 31: matriz[8]}
    game.print_m(display)
    turn = 'X'
    for i in range(10):
        position = input('Enter the coordinates: ').split()
        check, msg = game.check_position(position, turn)
        while not check:
            print(msg)
            position = input('Enter the coordinates: ').split()
            check, msg = game.check_position(position, turn)
        print(game.check_result(display))
        if game.check_result(display) == 'X wins' \
                or game.check_result(display) == 'O wins' \
                or game.check_result(display) == 'Draw':
            break
        else:
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'


if __name__ == "__main__":
    main()
