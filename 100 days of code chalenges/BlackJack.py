import random
def deal_card():
    """return a random card from the deck"""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, ]
    return random.choice(cards)
def calculate_score(cards):
    """Take a List of cards and calculate the score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) >= 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare (p_score, c_score):
    if p_score == c_score:
        return "Drow"
    elif c_score == 0:
        return "you lose opponent has a BLACK JACK  !!"
    elif p_score == 0 :
        return "you win with a BLACK JACK !!"
    elif p_score > 21 :
        return "you have too much point you lose"
    elif c_score > 21 :
        return "opponent went over you Win"
    elif p_score > c_score :
        return "you win with higher score"
    else:
        return "you lose"
def play_game():
    player_cards =[]
    computer_cards = []
    computer_score = -1
    player_score = -1
    more_card = ""
    is_game_over = False

    for _ in range(2):
        computer_cards.append(deal_card())
        player_cards.append(deal_card())
    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"youre cards: {player_cards},and the current score is {player_score}")
        print(f"computer first card is : {computer_cards[0]},")
        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            more_card = input("you want to pick another card? yes or no: ").lower()

        if more_card == "yes":
            player_cards.append(deal_card())
        else:
            is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"youre cards: {player_cards},and the final score is {player_score}")
    print(f"computer cards: {computer_cards},and the final score is {computer_score}")

    print(compare(player_score, computer_score))

while input("do you want to play ?(yes or no)").lower() == "yes":
    print("\n"*20)
    play_game()











