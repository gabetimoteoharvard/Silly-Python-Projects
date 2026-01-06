import time
import sys


SEPARATION = '---------------------------------'


class TTTBoard():
    def __init__(self):
        self.board = [['','',''] for box in range(3)]
        self.conversion = {'1':[0,0], '2':[0,1], '3': [0,2], '4':[1,0], '5':[1,1], '6':[1,2],'7':[2,0], '8':[2,1], '9':[2,2]}
    

    def displayBoard(self):
        print(f'''
              | {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} | 123
               ---------
              | {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} | 456
               ---------
              | {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2] } | 789
              ''')


    def validPos(self, choice):
        if int(choice) in range(1,10) and self.board[self.conversion[choice][0]][self.conversion[choice][1]] == '':
            return True
        return False


    def winner(self, p):
        b = self.board[:]
        if b[0][0] == b[1][1] == b[2][2] == p:
            return True
        if b[0][2] == b[1][1] == b[2][0] == p:
            return True
        if b[0][0] == b[0][1] == b[0][2] == p:
            return True
        if b[1][0] == b[1][1] == b[1][2] == p:
            return True
        if b[2][0] == b[2][1] == b[2][2] == p:
            return True
        if b[0][1] == b[1][1] == b[2][1] == p:
            return True
        if b[0][0] == b[1][0] == b[2][0] == p:
            return True
        if b[0][2] == b[1][2] == b[2][2] == p:
            return True

        return False


    def board_is_full(self):
        for row in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[row][c] == '':
                    return False
        return True


class AISolver:
    def __init__(self, name):
        self.name = name
    
    def winner(self, p, b):
        if b[0][0] == b[1][1] == b[2][2] == p:
            return True
        if b[0][2] == b[1][1] == b[2][0] == p:
            return True
        if b[0][0] == b[0][1] == b[0][2] == p:
            return True
        if b[1][0] == b[1][1] == b[1][2] == p:
            return True
        if b[2][0] == b[2][1] == b[2][2] == p:
            return True
        if b[0][1] == b[1][1] == b[2][1] == p:
            return True
        if b[0][0] == b[1][0] == b[2][0] == p:
            return True
        if b[0][2] == b[1][2] == b[2][2] == p:
            return True

        return False

    def board_is_full(self, board):
        for row in range(len(board)):
            for c in range(len(board[0])):
                if board[row][c] == '':
                    return False
        return True
               
        
    def minimax(self, player, enemy, board, maximize, position=False):
        if maximize:
            copy = [x[:] for x in board]
        
            if position:
                copy[position[0]][position[1]] = enemy

            if self.winner(player, copy):
                return 1, position
            if self.winner(enemy, copy):
                return -1, position
            if self.board_is_full(copy):
                return 0, position

            empty_positions = [(r,c) for c in range(len(copy[0])) for r in range(len(copy)) if copy[r][c] == '']
            maximize = False
            value = (-100,'')

            for pos in empty_positions:
                val = self.minimax(player,enemy,copy,maximize,pos)
                if val[0] > value[0]:
                    value = (val[0],pos)
                    
            return value

        else: 
            copy = [x[:] for x in board]
            copy[position[0]][position[1]] = player
           
            if self.winner(player, copy):
                return 1,position
            if self.winner(enemy, copy):
                return -1,position
            if self.board_is_full(copy):
                return 0,position

            empty_positions = [(r,c) for c in range(len(copy[0])) for r in range(len(copy)) if copy[r][c] == '']
            maximize = True
            value = (100, '')
            
            for pos in empty_positions:
                val = self.minimax(player,enemy,copy,maximize,pos)
                if val[0] < value[0]:
                    value = (val[0],pos)

            return value

       

def main():
    print(f'''Terminal Tic-Tac-Toe by Gabriel

  Select numbers 1-9 in order to select what box you want to check off
             ''')
   
    player_valid = False
    while not player_valid:
        print(f'Choose a player: X or O')
        player = input('>').upper().strip()
        if player not in ('O','X'):
            print(f'Invalid choice\n\n')
            continue
        player_valid = True
     
    playerAI = AISolver('GABE')
    game = TTTBoard()

    if player == 'X':
        player_turn = True
        opponent = 'O'
    else:
        player_turn = False
        opponent = 'X'

    running = True
    while running:
        if player_turn:
            print(SEPARATION)
            game.displayBoard()
            print('Make a choice, enter a number from 1-9')
            choice = input('>').strip()
            if game.validPos(choice):
                pos = game.conversion[choice]
                game.board[pos[0]][pos[1]] = player
           
                if game.winner(player):
                    game.displayBoard()
                    print(f'You win, congratulations, but this will never happen')
                    sys.exit()
                if game.board_is_full():
                    game.displayBoard()
                    print(f'Tie! Nobody wins')
                    sys.exit()

                player_turn = False 
            continue

        if not player_turn:
            print(SEPARATION)
            game.displayBoard()
            opponent_position = playerAI.minimax(opponent, player, game.board, True)[1]
            game.board[opponent_position[0]][opponent_position[1]] = opponent
            
            if game.winner(opponent):
                game.displayBoard()
                print(f'You lost, better luck next time')
                sys.exit()
            if game.board_is_full():
                game.displayBoard()
                print(f'Tie, nobody wins')
                sys.exit()
            
            player_turn = True
            print('AI is making a move...')
            time.sleep(1)
            
           
    
   


if __name__ == '__main__':
    main()
    
   
