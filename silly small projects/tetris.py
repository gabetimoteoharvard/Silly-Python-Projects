from pytimedinput import timedInput, timedKey
import random
import os
import sys

class Tetris:
    def __init__(self):
        self.WIDTH = 12
        self.HEIGHT = 22

        self.current_piece = None
        self.piece_name = "one_shaped"
        self.placed_tiles = []
        self.static_tiles = []

        self.curr_rotation = 0

    
    def getPiece(self):
        square = [[-1,6], [-1,7], [-2,6], [-2,7]]
        one_shaped = [[-1,6], [-2, 6], [-3,6], [-4,6]]
        s_shaped = [[-1,5], [-1, 6], [-2,6], [-2, 7]]
        z_shaped = [[-2,5], [-2,6], [-1,6], [-1,7]]
        l_shaped = [[-3, 6], [-2,6], [-1,6], [-1,7]]
        j_shaped = [[-3, 6], [-2,6], [-1,6], [-1,5]]
        t_shaped = [[-1,6], [-2,6], [-2, 5], [-2, 7]]

        ls = [square, one_shaped, s_shaped, z_shaped, l_shaped, j_shaped, t_shaped]
        names = ["square", "one_shaped", "s_shaped", "z_shaped", "l_shaped", "j_shaped", "t_shaped"]
       # index = random.randint(0, len(ls) - 1)
 
        
       # self.piece_name = names[index]
        return ls[1]
   
        
    def display_grid(self):
        os.system('clear')

        for row in range(self.HEIGHT):
            for column in range(self.WIDTH):
       
                if row in (0, self.HEIGHT - 1) or column in (0, self.WIDTH - 1):
                    print('+', end = '')
                elif (self.current_piece and [row, column] in self.current_piece) or [row,column] in self.placed_tiles:
                    print('*', end = '')
                else:
                    print(' ', end = '')
            print()

    def not_possible(self, point):
    
        
                        
                

    def rotate(self):
        
        if self.piece_name == "square":
            return
        elif self.piece_name == "one_shaped":
            
            rot_point = self.current_piece[1]

            if self.not_possible(rot_point):
                return
            
            if self.curr_rotation == 90 or self.curr_rotation == 270:
 
                self.current_piece[0][0] = rot_point[0]
                self.current_piece[0][1] = rot_point[1] - 1

                self.current_piece[2][0] = rot_point[0]
                self.current_piece[2][1] = rot_point[1] + 1
            
                self.current_piece[3][0] = rot_point[0]
                self.current_piece[3][1] = rot_point[1] + 2
                
            else:
 
                self.current_piece[0][1] = rot_point[1]
                self.current_piece[0][0] = rot_point[0] - 1

                self.current_piece[2][1] = rot_point[1]
                self.current_piece[2][0] = rot_point[0] + 1
            
                self.current_piece[3][1] = rot_point[1]
                self.current_piece[3][0] = rot_point[0] + 2
                
        
        


    def update_grid(self):
        char, timedOut = timedKey("", 0.5)
        if char == 'q':
            sys.exit()

        #makes pieces go down until collision
        for i in range(len(self.current_piece)):
            self.current_piece[i][0] += 1 

        move_back = False

        for i in range(len(self.current_piece)):
            if self.current_piece[i] in self.placed_tiles or self.current_piece[i][0] == self.HEIGHT - 1:
                move_back = True

        if move_back:
            for i in range(len(self.current_piece)):
                self.current_piece[i][0] -= 1 
                self.placed_tiles.append(self.current_piece[i])

            self.static_tiles.append(self.current_piece)
            self.current_piece = None

        
            
        #user input, moving left and right
        movement = 0
        if not timedOut:
            if char == 'd':
                movement = 1
            elif char == 'a':
                movement = -1

        if movement != 0 and self.current_piece is not None:
            for i in range(len(self.current_piece)):
                self.current_piece[i][1] += (movement)

            collision = False
            for i in range(len(self.current_piece)):
                if self.current_piece[i] in self.placed_tiles or self.current_piece[i][1] == self.WIDTH - 1 or self.current_piece[i][1] == 0:
                    collision = True

            if collision:
                 for i in range(len(self.current_piece)):
                     self.current_piece[i][1] -= (movement)

        #gravity applied on individual pieces
        self.handle_static_pieces()

        #user input, rotation
        if char == 'r' and self.current_piece is not None:
            self.rotate()
            self.curr_rotation = (self.curr_rotation + 90) % 360
            

    def handle_static_pieces(self):
 
        for piece in range(len(self.static_tiles)):

            cancelFall = False

            for tile in range(len(self.static_tiles[piece])):

                block = self.static_tiles[piece][tile]
        
                for i, t in enumerate(self.placed_tiles):
                    if t[0] == block[0] and t[1] == block[1]:
                        coord = [self.placed_tiles[i][0] + 1, self.placed_tiles[i][1]]
                        if (coord in self.placed_tiles and coord not in self.static_tiles[piece]) or self.placed_tiles[i][0] + 1 == self.HEIGHT - 1:
                        
                            cancelFall = True
                           
                        
                         
            
           

            if not cancelFall:

                for tile in range(len(self.static_tiles[piece])):
                    block = self.static_tiles[piece][tile]
       

                    clean_up = []
                    for t in self.placed_tiles:
                        if t not in clean_up:
                            clean_up.append(t)

                    for i, t in enumerate(clean_up):
                        if t[0] == block[0] and t[1] == block[1]:
                            
                            self.placed_tiles[i][0] += 1
                            
                           

                     

    def handle_break(self):
        for row in range(self.HEIGHT):

            filled = 0
            to_be_removed = []

            for element in range(self.WIDTH):
                if [row, element] in self.placed_tiles:
                    filled+=1
                    to_be_removed.append([row, element])

            if filled == self.WIDTH - 2:
                for el in to_be_removed:
                    self.placed_tiles.remove(el)
                    for piece in range(len(self.static_tiles)):
                           if el in self.static_tiles[piece]:
                               self.static_tiles[piece].remove(el)
                     
                

    def run(self):

        if self.current_piece is None:
            self.current_piece = self.getPiece()


        self.handle_break()
        self.update_grid()
        self.display_grid()
     


board = Tetris()

while True:
    board.run()
   
       
