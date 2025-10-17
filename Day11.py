# Capstone project: Game of Blackjack or 21
"""
# Bust - If cards sum > 21, lost!
# cards till 2 to 10, are counted as per their face values
# cards K, Q, J are counted as 10 
# Ace counted as 1 or 11 - depending on over or under 21. We can decide the value ourselves

# Dealer v/s you. 

# First both cards will be revealed. Then dealer deals another card to both of you, but dealer's second hand is concealed. You can again request or not another card. If you get another, and again want to request more, you can. If not, the dealer will reveal his card, and the one who has higher total will win

# games.washingtonpost.com/games/blackjack/

# Assumed Infinite deck - So in real life, probability of the same card again decreases after a draw. But we won't get into this complication
"""
art = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      '------'                           |__/           
"""
import random
print(art, "\n Welcome to Blackjack")

def blackjack():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    p_cards = list(random.choices(cards,k=2))
    d_cards = [random.choice(cards)]
    current_score = sum(p_cards)
    dealer_sum = sum(d_cards)

    print(f"Your cards: {p_cards}, current_score = {current_score} \n Computer's first card: {d_cards}")

    while current_score <= 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass:")       #anything else to pass
        if another_card == 'y':
            p_cards.append(random.choice(cards))

            if 11 in p_cards:
                if sum(p_cards) <= 21:
                    current_score = sum(p_cards)            # Very important to note. We need to update. won't happen automatically.
                else:
                    p_cards = [1 if x == 11 else x for x in p_cards]
                    current_score = sum(p_cards)

            current_score = sum(p_cards)
            print(f"player's cards: {p_cards}; Current_score: {current_score}")
            if current_score > 21:
                print("You lost")    
                break                   # exit()

        else:
            if dealer_sum < 17 and dealer_sum < current_score:
                while dealer_sum < 17:
                    d_cards.append(random.choice(cards))

                    if 11 in d_cards:
                        if sum(d_cards) <= 21:
                            dealer_sum = sum(d_cards)            # Very important to note. We need to update. won't happen automatically.
                        else:
                            d_cards = [1 if x == 11 else x for x in d_cards]
                            dealer_sum = sum(d_cards)

                    dealer_sum = sum(d_cards)
                print(f"dealer's cards: {d_cards}")

            if dealer_sum > current_score and dealer_sum <= 21:
                print("You lost")
                break
            
            if dealer_sum >= 17:
                if dealer_sum > 21:
                    print("You Won!")
                elif dealer_sum == current_score:
                    print("Draw")
                elif dealer_sum < current_score:
                    print("You Won !")    
                
                break

    play_again = input("You want to play again? True or False")
    if play_again == "True":
        blackjack()
    else:
        exit()
    
blackjack()



    
        






