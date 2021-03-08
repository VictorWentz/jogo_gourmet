from foodtree import FoodTree


class Game:

    def __init__(self, root: FoodTree):
        self.decisionTree = root

    def new_food(self, guess: FoodTree) -> tuple:
        newFood = input("Qual é o nome da comida? ")
        newTyp = input(f"{newFood} é ____ mas {guess.data} não é? ")
        return (newFood, newTyp)

    def try_guess(self) -> FoodTree:
        root_tree = self.decisionTree

        while not root_tree.is_child():
            if input(f"O prato que você pensou é {root_tree.data}? (y/n)").lower() == "y":
                root_tree = root_tree.left
            else:
                root_tree = root_tree.right
        return root_tree

    def start_game(self) -> None:
        while 1:
            input("Pense em um prato que gosta? pressione enter")
            guess = self.try_guess()

            acertou = input(
                f"O prato que você pensou é {guess.data}? (y/n)").lower() == "y"
            if acertou:
                self.win()
                continue

            (food, typ) = self.new_food(guess)

            if not guess.is_child():
                continue
            self.add_food(guess, food, typ)

    def add_food(self, decisionTree, food, typ) -> None:
        decisionTree.right = FoodTree(decisionTree.data)
        decisionTree.left = FoodTree(food)
        decisionTree.data = typ

    def win(self) -> None:
        print("Acertei de novo!")
