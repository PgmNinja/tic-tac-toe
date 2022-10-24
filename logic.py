from moves.best_move import get_next_move

class TicTacToe:
    player = 1
    player_positions = {}

    def output(self, player_positions):
        for x in range(3):
            if x > 0:
                print('----------')
            for y in range(3):
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

    def winning_status(self, player_position):
        player_1 = {'x': {}, 'y': {}}
        player_2 = {'x': {}, 'y': {}}

        for x, y in player_position:
            if player_position[(x, y)]['value'] == '+':
                self.get_coordinate_count(player_1, x, y)
            else:
                self.get_coordinate_count(player_2, x, y)

        if 3 in player_1['x'].values() or 3 in player_1['y'].values():
            return 'Player 2', True
        elif 3 in player_2['x'].values() or 3 in player_2['y'].values():
            return 'Player 1', True
        else:
            return None, False

    def update_table(self):
        positions = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2)}
        count = 0
        self.output({(None, None)})
        while count <= 9:
            try:
                position = int(input\
                    ('Choose a position among 1 - (0,0), 2 - (0,1), 3 - (0,2), 4 - (1,0), 5 - (1,1), 6 - (1,2), 7 - (2,0), 8 - (2,1), 9 - (2,2): '))
            except Exception as e:
                position = 0

            if position not in list(range(1, 10)):
                print('Please enter a valid number')
                return False
            else:
                curr_position = positions[position]

                if self.player == 1:
                    self.player_positions[curr_position] = {'value': '+', 'move': count}
                    self.player = 2
                else:
                    self.player_positions[curr_position] = {'value': 'o', 'move': count}
                    self.player = 1
                self.output(self.player_positions)
                player, winning_status = self.winning_status(self.player_positions)
                if winning_status:
                    print(f'{player} wins')
                    break
                count += 1

    def input_loop(self):
        try:
            position = int(input\
                ('Choose a position among 1 - (0,0), 2 - (0,1), 3 - (0,2), 4 - (1,0), 5 - (1,1), 6 - (1,2), 7 - (2,0), 8 - (2,1), 9 - (2,2): '))
        except Exception as e:
            position = 0
        return position

    def update_table_(self):
        positions = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2)}
        count = 0
        curr_position = None
        while count <= 8:
            if self.player == 2:
                position = self.input_loop()
                if position not in list(range(1, 10)):
                    print('Please enter a valid number')
                    return False
                curr_position = positions[position]
                self.player_positions[curr_position] = {'value': '+', 'move': count}
                self.player = 1
            else:
                next_position = get_next_move(curr_position, count)
                self.player_positions[next_position] = {'value': 'o', 'move': count}
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
    tic_tac_toe.update_table_()

if __name__ == '__main__':
    main()
