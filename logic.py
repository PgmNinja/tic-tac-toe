class TicTacToe:

    player = 1
    player_positions = {}

    def output_(self, player_positions):
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


    def update_table(self):
        positions = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2)}
        count = 0
        while count <= 8:
            position = input('Choose a position among 1 - (0,0), 2 - (0,1), 3 - (0,2), 4 - (1,0), 5 - (1,1), 6 - (1,2), 7 - (2,0), 8 - (2,1), 9 - (2,2): ')
            curr_position = positions[int(position)]

            if self.player == 1:
                self.player_positions[curr_position] = {'value': '+', 'count': count}
                self.player = 2
            else:
                self.player_positions[curr_position] = {'value': 'o', 'count': count}
                self.player = 1
            self.output_(self.player_positions)
            count += 1


tick_tac_toe = TicTacToe()
tick_tac_toe.update_table()