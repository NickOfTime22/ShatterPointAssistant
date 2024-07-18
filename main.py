class player:
        def __init__(self, name):
            self.name = name

# Initial game setup function
def setup(player1, player2):
    p1_name = input("Player 1, enter your name: ")
    player1.name = p1_name
    p2_name = input("Player 2, enter your name: ")
    player2.name = p2_name

# Loop for each turn
def take_turn(player):
    print(player.name, "'s turn!", sep="")
    # print()

# Main loop for running the app
def main():
    p1 = player("")
    p2 = player("")
    setup(p1, p2)
    take_turn(p1)

if __name__ == "__main__": 
    main()