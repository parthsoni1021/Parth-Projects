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
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
