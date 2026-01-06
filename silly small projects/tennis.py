import random
import math


class Tennis:
    def __init__(self, opponent_1, opponent_2):
        self.p1 = opponent_1
        self.p2 = opponent_2

        self.p2_attributes = [0, 0, 0, 0]
        self.p1_attributes = []

        
    def setup(self, name, fh, bh, serve, volley):
        if name == self.p1:
            self.p1_attributes = [fh, bh, serve, volley]
        elif name == self.p2:
            self.p2_attributes = [fh, bh, serve, volley]


    def calculate(self, attributes, opp_attributes):
        ans = [0,0] #chances of winning serve, chances of winning rally at serve

        calc = (attributes[2]*attributes[3] - opp_attributes[0]*opp_attributes[1])/3
        chance = min(99, max(50 + calc,10))
  
        good_s = min(99, math.sqrt(max(1,(attributes[2]**2 - opp_attributes[0]*opp_attributes[1]) + 50)))

        ans = [good_s/100, chance/100]
        return ans



    def tiebreak(self, curr_serve, b_out_p):
        player_1 = self.calculate(self.p1_attributes, self.p2_attributes)
        player_2 = self.calculate(self.p2_attributes, self.p1_attributes)

        p1 = 0
        p2 = 0
        
        served = 0

        if player_1[0] > random.random():
            p1+=1
        elif player_1[1] > random.random():
            p1+=1
        else:
            p2+=1
        curr_serve = '2'

        while True:
            if (p1 >= b_out_p and p2 <= p1 - 2) or (p2 >=b_out_p and p1 <= p2 - 2):
                if p1 < p2:
 
                    return f'6-7 ({p1}-{p2})'
                else:
                    return f'7-6 ({p1}-{p2})'
      
            if curr_serve == '1':
                if player_1[0] > random.random():
                    p1+=1
                elif player_1[1] > random.random():
                    p1+=1
                else:
                    p2+=1
                
                served+=1 
                if served == 2:
                    if curr_serve == '1':
                        curr_serve = '2'
                    else:
                        curr_serve = '1'
                    served = 0
            else:
                if player_2[0] > random.random():
                    p2+=1
                elif player_2[1] > random.random():
                    p2+=1
                else:
                    p1+=1
                
                served+=1 
                if served == 2:
                    if curr_serve == '1':
                        curr_serve = '2'
                    else:
                        curr_serve = '1'
                    served = 0
                
        
     
    def simulate(self):
        player_1 = self.calculate(self.p1_attributes, self.p2_attributes)
        player_2 = self.calculate(self.p2_attributes, self.p1_attributes)
        
        print(player_1, player_2)
        curr_set = 1
        curr_serve = None
        set_1 = None
        set_2 = None
        set_3 = None

        set_1W= None
        set_2W = None

        p1_games = 0
        p2_games = 0

        serve = random.randint(0,1)
        if not serve:
            curr_serve = '1'
        else:
            curr_serve = '2'

        done = False

        p1_points = 0
        p2_points = 0
        while not done:
            if p1_points >= 4 and p2_points <= p1_points - 2 :
                p1_games+=1
                p1_points = 0
                p2_points = 0

                if curr_serve == '1':
                    curr_serve = '2'
                else:
                    curr_serve = '1'

            if p2_points >= 4 and p1_points <= p2_points - 2:
                p2_games+=1
                p1_points = 0
                p2_points = 0

                if curr_serve == '1':
                    curr_serve = '2'
                else:
                    curr_serve = '1'

            if (p1_games >= 6 and p2_games <= p1_games - 2) or (p2_games >= 6 and p1_games <= p2_games - 2):
                if curr_set == 1:
                    set_1 = f'{p1_games}-{p2_games}'
                    curr_set+=1
                elif curr_set == 2:
                    set_2 = f'{p1_games}-{p2_games}'
                    
                    curr_set+=1
                else:
                    set_3 = f'{p1_games}-{p2_games}'
                    break

                p1_games = 0
                p2_games = 0

            if p1_games == p2_games and p1_games == 6:
                if curr_set == 1:
                    set_1 = self.tiebreak(curr_serve,7)
                    curr_set+=1
                elif curr_set == 2:
                    set_2 = self.tiebreak(curr_serve,7)
                    curr_set+=1
                else:
                    set_3 = self.tiebreak(curr_serve,7)
                    break

                p1_games = 0
                p2_games = 0
            


            if curr_serve == '1':
                if player_1[0] > random.random():
                    p1_points+=1
                    continue

                if player_1[1] > random.random():
                    p1_points+=1
                else:
                    p2_points+=1

            else:
                if player_2[0] > random.random():
                    p2_points+=1
                    continue

                if player_2[1] > random.random():
                    p2_points+=1
                else:
                    p1_points+=1

        print(set_1 + '\n' + set_2 + '\n' + set_3)
            




match = Tennis('Federer', 'Djokovic')
match.setup('Federer',10,8,9,10)
match.setup('Djokovic',9,10,8,8)
match.simulate()


