from moves.move import get_next_move

class TicTacToe:
    player = 1
    player_positions = {}

    def __init__(self, size=3):
        self.size = size

    def output(self, player_positions):
        for x in range(self.size):
            if x > 0:
                print('----------')
            for y in range(self.size):
                if (x, y) in player_positions and ((x,y) == (0,2) or (x,y) == (1,2) or (x,y) == (2,2)):
                    print(player_positions[(x,y)]['value'])
                elif (x,y) in player_positions:
                    print(player_positions[(x,y)]['value'], end=' | ')
                elif y == 2:
                    print(' ')
                else:
                    print(' ', end=' | ')

    def get_coordinate_count(self, player, x, y):
        if x not in player['x']:
            player['x'][x] = 1
        else:
            player['x'][x] += 1

        if y not in player['y']:
            player['y'][y] = 1
        else:
            player['y'][y] += 1

        if x == y:
            player['z']['forward'] += 1
        if x + y == self.size - 1:
            player['z']['backward'] += 1


    def winning_status(self, player_position):
        player_1 = {'x': {}, 'y': {}, 'z' : {'backward': 0, 'forward': 0}}
        player_2 = {'x': {}, 'y': {}, 'z' : {'backward': 0, 'forward': 0}}

        for x, y in player_position:
            if player_position[(x, y)]['value'] == 'o':
                self.get_coordinate_count(player_1, x, y)
            else:
                self.get_coordinate_count(player_2, x, y)

        if self.size in player_1['x'].values() or self.size in player_1['y'].values() or \
            self.size in player_1['z'].values():
            return 'Player 1', True
        elif self.size in player_2['x'].values() or self.size in player_2['y'].values() or \
            self.size in player_2['z'].values():
            return 'Player 2', True
        else:
            return None, False

    def input_loop(self):
        try:
            position = int(input\
                ('Choose a position among 1 - (0,0), 2 - (0,1), 3 - (0,2), 4 - (1,0), 5 - (1,1), 6 - (1,2), 7 - (2,0), 8 - (2,1), 9 - (2,2): '))
        except Exception as e:
            position = 0
        return position

    def update_table(self):
        positions = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2)}
        count = 0
        curr_position = None
        while count <= 8:
            if self.player == 2:
                position = self.input_loop()
                if position not in list(range(1, 10)):
                    print('Please enter a valid number!')
                    continue
                curr_position = positions[position]
                if curr_position in self.player_positions:
                    print('This position is already occupied!')
                    continue
                self.player_positions[curr_position] = {'value': '+'}
                self.player = 1
            else:
                next_position = get_next_move(self.player_positions)
                self.player_positions[next_position] = {'value': 'o'}
                self.player = 2
            self.output(self.player_positions)
            print()
            player, winning_status = self.winning_status(self.player_positions)
            if winning_status:
                print(f'{player} wins')
                break
            count += 1


def main():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.update_table()

if __name__ == '__main__':
    main()
