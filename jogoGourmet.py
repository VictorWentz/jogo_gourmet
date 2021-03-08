from foodtree import FoodTree
from game import Game

if __name__ == "__main__":
    root = FoodTree("Massa", FoodTree("Lasanha"),
                    FoodTree("Bolo de Chocolate"))
    game = Game(root)

    game.start_game()
