# snake_game
In this project, I use a turtle module to build a snake game

1) Set up a screen
    1.1) Background color is black
    1.2) Width = 600px and height = 600px
    1.3) Title is Snake game

2) Create a snake with 3 part of its body: snake file
    2.1) Create a snake with head, body and tail and append them into an empty list
        2.1.1) When a snake ate an apple, the length increase one part... NOTE have to add a part into the (x,y)cor
        of tail
        2.1.2) When a snake hit 4 limit lines..... Game is Over
        2.1.3) When a snake ate itself..... Game is Over

    2.2) MOVING: Create a function that when it moves its tail move to a position of its body and body move to
    a position of its head and then head move forward. That mean all of these must follow the head of snake
        2.2.1) Detail: the x_cor and y_cor of the tail then move to x_cor and y_cor of the body
        2.2.2) Turn UP, DOWN, LEFT, RIGHT.... NOTE (when head position in the opposite side of position that YOU CHOOSE,
        it cannot be true).

3) Create an apple: apple file
    3.1) It locates at random position
    3.2) If snake ate an apple
        3.2.1) Score increase 1
        3.2.2) Return (3.1)

4) Create a scoreboard: score file
    4.1) It locates at top center with default value is 0
    4.2) Keep track the highest score and use sheety api to save playing history
