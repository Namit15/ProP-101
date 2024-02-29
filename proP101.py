import random

response = "y"
while response == "y":
    no = random.randint(1, 6)
    if no == 1:
        print("""
                 ______
                |       |
                |   1   |
                |_______|
                        |
                        |
                        |
                  ______|______
                """)
    elif no == 2:
        print("""
                 ______
                |       |
                |   2   |
                |_______|
                  |  |  |
                  |  |  |
                  |  |  |
                  |__|__|
                """)
    elif no == 3:
        print("""
                 ______
                |       |
                |   3   |
                |_______|
                  |  |  |
                  |    |
                  |____|
                        |
                        |
                        |
                  ______|______
                """)
    elif no == 4:
        print("""
                 ______
                |       |
                |   4   |
                |_______|
                  |  |  |
                  |  |  |
                  |  |  |
                  |  |  |
                  |__|__|
                """)
    elif no == 5:
        print("""
                 ______
                |       |
                |   5   |
                |_______|
                  |  |  |
                  |    |
                  |____|
                        |
                        |
                   _____|____
                """)
    elif no == 6:
        print("""
                 ______
                |       |
                |   6   |
                |_______|
                  |  |  |
                  |  |  |
                  |  |  |
                  |__|__|
                   ______
                """)
    else:
        print("Invalid number!")

    response = input("Do you want to roll again (y/n)? ").lower()

print("Thanks for playing!")