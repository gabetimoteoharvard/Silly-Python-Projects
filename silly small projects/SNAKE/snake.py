from pytimedinput import timedInput, timedKey
from custom import CustomFunctions
import os
import sys
import random

class Game:
    def __init__(self):
       
        self.WIDTH = 30
        self.HEIGHT = 10

        self.snake = [[4, 10]]
       
        self.fruit = None
        self.place_fruit()
        self.dir = "r"

        self.high_score = 0
 
        self.running = True

    def new_head(self):
        curr_head = self.snake[0][:]

        if self.dir == "r":
            curr_head[1] += 1
        elif self.dir == "l":
            curr_head[1] -= 1
        elif self.dir == "u":
            curr_head[0] -= 1
        else:
            curr_head[0] += 1

        return curr_head

    def place_fruit(self):
        _y = random.randint(1, self.HEIGHT - 2)
        _x = random.randint(1, self.WIDTH - 2)
        while CustomFunctions.array_in_array([_y, _x], self.snake):
            _y = random.randint(1, self.HEIGHT - 2)
            _x = random.randint(1, self.WIDTH - 2)
        self.fruit = [_y, _x]


    def obstacle_collision(self):
        head = self.snake[0][:]

        if CustomFunctions.array_in_array(head, self.snake[1:]):
            self.running = False
            score = len(self.snake)
            self.high_score = max(score, self.high_score)
            self.reset()
            
        
        if head[0] in (0, self.HEIGHT - 1) or head[1] in (0, self.WIDTH - 1):
            self.running = False
            score = len(self.snake)
            self.high_score = max(score, self.high_score)
            self.reset()


    def fruit_collision(self):
        head = self.snake[0][:]

        new_h = self.new_head()

        if CustomFunctions.equal_array(head, self.fruit):
            self.fruit = None
            self.place_fruit()

        else:
            self.snake.pop()

        self.snake = CustomFunctions.append_arr([new_h], self.snake)
            
    
       

    def change_possible(self, d):
        if len(self.snake) >= 2:
            neck = self.snake[1]
            head = self.snake[0]
            if d == "r":
                if CustomFunctions.equal_array([head[0],head[1] + 1], neck):
                    return False
            elif d == "l":
                if CustomFunctions.equal_array([head[0],head[1] - 1], neck):
                    return False
            elif d == "u":
                if CustomFunctions.equal_array([head[0] - 1,head[1]], neck):
                    return False
            elif d == "d":
                if CustomFunctions.equal_array([head[0] + 1 ,head[1]], neck):
                    return False

        
        return True
 


    def display_grid(self):
        os.system('clear')

        for row in range(self.HEIGHT):
            for column in range(self.WIDTH):
                if row in (0, self.HEIGHT - 1) or column in (0, self.WIDTH - 1):
                    print('+', end = '')
                elif CustomFunctions.array_in_array([row, column], self.snake):
                    print('#', end='')
                elif CustomFunctions.equal_array([row, column], self.fruit):
                    print('@', end='')
                else:
                    print(' ', end='')
            print()

    def update_grid(self):
        char, timedOut = timedKey("", 0.5)
 
        if not timedOut:
            
            if char == "q":
                sys.exit()

            if char == "w" and self.change_possible("u"):
                self.dir = "u"
            elif char == "d" and self.change_possible("r"):
                self.dir = "r"
            elif char == "a" and self.change_possible("l"):
                self.dir = "l"
            elif char == "s" and self.change_possible("d"):
                self.dir = "d"

        self.fruit_collision()
        self.obstacle_collision()

    def reset(self):
        self.snake = [[4, 10]]
       
        self.fruit = None
        self.place_fruit()
        self.dir = "r"
        

    def run(self):
        while True:

            if self.running:
            
                self.display_grid()
                self.update_grid()

            else:
                print(f'YOU DIED \n HIGH SCORE is {self.high_score} \n')
                print(f'PLAY AGAIN? (y/n) ')
                key, timedOut = timedKey("", float("inf"))
                if key and key.lower() == "n":
                    sys.exit()
                elif key and key.lower() == "y":
                    self.running = True

                

           

def main():
    print("TERMINAL SNAKE \n BY GABRIEL TIMOTEO\n")
    print("PRESS ANY KEY TO START \n PRESS 'q' TO QUIT")

    key, timedOut = timedKey("")
    if key == "q":
       sys.exit()
    
    new_game = Game()
    new_game.run()


if __name__ == "__main__":
    main()
    
  



