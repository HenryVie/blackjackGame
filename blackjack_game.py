import random

# Create a whole card deck
def create_deck():
    suits = ["♠", "♥", "♦", "♣"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
             "J", "Q", "K", "A"]
    
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# Take the last card from the deck
def deal_card(deck):
    return deck.pop()

# Calculate for the rank value
def calculate_hand(hand):
    value = 0
    ace = 0

    for rank, suit in hand:
        if rank in ['J', 'Q', 'K']:
            value += 10
        
        elif rank == 'A':
            value += 11
            ace += 1

        else:
            value += int(rank)

    while value > 21 and ace > 0:
        value -= 10
        ace = 1

    return value

# Show the card's value as rank-suit instead of in tuple-type value
def format_card(card):
    rank, suit = card
    return f"{rank}{suit}"

def format_hand(hand):
    return " ".join(format_card(card) for card in hand)

def player_turn(deck, player_hand, dealer_hand):
    while True:
        player_value = calculate_hand(player_hand)

        print(f"\nYour hand: {format_hand(player_hand)} ({player_value})")
        print(f"Dealer shows: {format_card(dealer_hand[0])}")

        if player_value > 21:
            print("You busted!")
            break

        # Ask player to take a card or stand
        choice = input("Hit or Stand? (h/s): ").lower()

        if choice == 'h':
            player_hand.append(deal_card(deck))

        elif choice == 's':
            break
        
        else:
            print("Invalid choice. Please enter h or s.")

# Dealer's turn after the player choose stand
def dealer_turn(deck, dealer_hand):
    print(f"\nDealer reveals hand: {format_hand(dealer_hand)}")

    # Dealer takes cards when the rank value is lower than 17
    while calculate_hand(dealer_hand) < 17:
        print("Dealer hits.")

        dealer_hand.append(deal_card(deck))

        print(f"Dealer hand: {format_hand(dealer_hand)}")

    dealer_value = calculate_hand(dealer_hand)

    print("Dealer stands with", dealer_value)

# Compare who has higher value, and if the player is busted
def check_winner(player_hand, dealer_hand):
    player_value = calculate_hand(player_hand)
    dealer_value = calculate_hand(dealer_hand)

    print(f"\nYour final hand: {format_hand(player_hand)} ({player_value})")
    print(f"Dealer final hand: {format_hand(dealer_hand)} ({dealer_value})")

    if player_value > 21:
        return "lose"
    
    if dealer_value > 21:
        return "win"
    
    if player_value > dealer_value:
        return "win"
    
    if player_value < dealer_value:
        return "lose"

    return "push"

# Game set-up
def play_blackjack():
    deck = create_deck()

    player_hand = []
    dealer_hand = []

    # Initial deal
    for _ in range(2):
        player_hand.append(deal_card(deck))
        dealer_hand.append(deal_card(deck))

    # Player turn
    player_turn(deck, player_hand, dealer_hand)

    # Dealer turn (only if player didn't bust)
    if calculate_hand(player_hand) <= 21:
        dealer_turn(deck, dealer_hand)

    # Decide winner
    result = check_winner(player_hand, dealer_hand)

    if result == "win":
        print("\n🎉 You win!")

    elif result == "lose":
        print("\n💀 You lose!")

    else:
        print("\n🤝 It's a push!")

def main():
    play_blackjack()

main()