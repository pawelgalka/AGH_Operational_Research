#Paweł Gałka
class GameNode:
    def __init__(self,player_max_turn,player_max_stacks,
                 player_min_stacks,prev_move,coins_stacks,score):
        self.nodes = []
        self.player_max_turn = player_max_turn
        self.player_max_stacks = player_max_stacks
        self.player_min_stacks = player_min_stacks
        self.prev_move = prev_move
        self.coins_stacks = coins_stacks
        self.score = score
        
    def create_children(self,obj):
        self.nodes.append(obj)
        
    def possible_move(self, possible_stacks):
        max_move = (2*self.prev_move,1)[self.prev_move == 0]
        return [(stack, coins_taken) for stack in possible_stacks for coins_taken in range(1, min(self.coins_stacks[stack]+1, max_move+1))]
    
    def check_if_exists_move(self):
        left_stacks = list(set(self.player_max_stacks + self.player_min_stacks))
        return any(self.coins_stacks[i] > 0 for i in left_stacks )
    
    def game(self):
        if self.player_max_turn:
            considered_stacks = self.player_max_stacks
        else:
            considered_stacks = self.player_min_stacks
        
        moves = self.possible_move(considered_stacks)
        
        for move in moves:
            coins_stacks = self.coins_stacks.copy()
            coins_stacks[move[0]] -= move[1]
            stacks_turn = considered_stacks.copy()
            stacks_turn.remove(move[0])
            if self.player_max_turn:
                score = self.score + move[1]
                self.create_children(GameNode(not self.player_max_turn,stacks_turn,self.player_min_stacks.copy(),move[1],coins_stacks, score))
            else:
                score = self.score - move[1]
                self.create_children(GameNode(not self.player_max_turn,self.player_max_stacks.copy(),stacks_turn,move[1],coins_stacks, score))
         
        if not len(moves) and self.check_if_exists_move():
                self.create_children(GameNode(not self.player_max_turn, self.player_max_stacks.copy(), self.player_min_stacks.copy(), self.prev_move, self.coins_stacks.copy(), self.score))
                
        for child in self.nodes:
            child.game()
    
def get_score(node : GameNode):
    if node.nodes == []:
        return node.score
    elif node.player_max_turn:
        return max([get_score(x) for x in node.nodes])
    else :
        return min([get_score(x) for x in node.nodes])
    
states = [[2,2,2],[3,3,3],[1,2,6]]

for state in states:
    root = GameNode(True,[0,1,2],[0,1,2],0,state,0)
    root.game()
    score = get_score(root)
    print('Init state',state, 'Player 1 scored', score, 'Player 2 scored', -score)
        
        