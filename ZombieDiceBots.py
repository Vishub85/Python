import random

class ZombieDiceGame:
    DICE_POOL = {
        'green': ['brain', 'brain', 'brain', 'footsteps', 'footsteps', 'shotgun'],
        'yellow': ['brain', 'brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun'],
        'red': ['brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun', 'shotgun']
    }
    
    ALL_DICE = ['green'] * 6 + ['yellow'] * 4 + ['red'] * 3
    
    def __init__(self):
        self.scores = {'Bot A': 0, 'Bot B': 0}
        self.players = list(self.scores.keys())
    
    def roll_die(self, color):
        return random.choice(self.DICE_POOL[color])
    
    def draw_dice(self, dice_pool, n=3):
        return [dice_pool.pop(random.randint(0, len(dice_pool)-1)) 
                for _ in range(min(n, len(dice_pool)))]
    
    def zombie_bot_turn(self, name="Bot"):
        try:
            dice_pool = self.ALL_DICE.copy()
            random.shuffle(dice_pool)
            
            brains = 0
            shotguns = 0
            footprints = []
            
            print(f"\n{name}'s turn begins!")
            
            while True:
                needed = 3 - len(footprints)
                drawn_dice = footprints + self.draw_dice(dice_pool, needed)
                footprints = []
                
                print(f"\nRolling: {drawn_dice}")
                roll_results = [self.roll_die(color) for color in drawn_dice]
                
                for i, result in enumerate(roll_results):
                    print(f"Rolled a {drawn_dice[i]} die: {result}")
                    if result == 'brain':
                        brains += 1
                    elif result == 'shotgun':
                        shotguns += 1
                    else:
                        footprints.append(drawn_dice[i])
                
                print(f"Current: {brains} brains, {shotguns} shotguns")
                
                if shotguns >= 3:
                    print(f"{name} got blasted! Turn over. No brains this round.")
                    return 0
                
                if brains >= 2 or shotguns == 2:
                    print(f"{name} decides to stop and bank {brains} brains.")
                    return brains
                    
        except Exception as e:
            print(f"Error in {name}'s turn: {str(e)}")
            return 0
    
    def simulate_game(self):
        try:
            turn = 0
            while max(self.scores.values()) < 13:
                player = self.players[turn % 2]
                gained = self.zombie_bot_turn(player)
                self.scores[player] += gained
                print(f"{player} total score: {self.scores[player]}")
                turn += 1
            
            winner = max(self.scores, key=self.scores.get)
            print(f"\n🏆 {winner} wins with {self.scores[winner]} brains!")
            
        except Exception as e:
            print(f"Game simulation error: {str(e)}")
            return

# Run the game
game = ZombieDiceGame()
game.simulate_game()
