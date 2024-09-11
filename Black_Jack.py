import random

#**********SUM FUNCTION WHICH TAKES LIST AND PROVIDES SUM **********
def sum(list):
    sum_fun = 0
    for key in list:
        sum_fun += key
    
    return sum_fun
        
    
Cards = [1,2,3,4,5,6,7,8,9,10,10,10]

start_game = True

while start_game:
    choice_1 = input("You want to start the game, 'Y' for yes 'N' for no\n").lower()
    
    if choice_1 == 'n':
        print("Thank You for coming!")
        break
    else:
        restart = True
        
        while restart:
            card_player = []
            card_comp = []
    
            player_1 = random.choice(Cards)
            player_2 = random.choice(Cards)
            card_player.append(player_1)
            card_player.append(player_2)
            
            comp_1 = random.choice(Cards)
            card_comp.append(comp_1)
            
            print(f"Your cards = {card_player}")
            print(f"Comp cards = {card_comp}")
            
            choice_2 = input("You want to draw a card?\nY - Yes\nN - NO\n").lower()
            if choice_2 =='y':
                player_3 = random.choice(Cards)
                card_player.append(player_3)
                
                comp_2 = random.choice(Cards)
                comp_3 = random.choice(Cards)
                card_comp.append(comp_2)
                card_comp.append(comp_3)
                
                print(f"Your cards = {card_player}")
                print(f"Comp cards = {card_comp}")
                
            else:
                comp_2 = random.choice(Cards)
                card_comp.append(comp_2)
                
                print(f"Your cards = {card_player}")
                print(f"Comp cards = {card_comp}")
                
            comp_sum = sum(card_comp)
            player_sum = sum(card_player)
            
            if player_sum > 21:
                print("Computer Wins")
            elif comp_sum < player_sum <= 21:
                print("Player Wins")
            
            elif player_sum< comp_sum <= 21:
                print("Computer Wins")
            
            elif player_sum == comp_sum <= 21:
                print("Draw!") 
            
            
            choice_3 = input("You want to restart?\nY = Yes\nN = No\n").lower()
            if choice_3 == 'n':
                print("Thank You for playing")
                break
        break