% Facts: fruit and its color
fruit_color(apple, red).
fruit_color(apple, green).
fruit_color(banana, yellow).
fruit_color(grapes, green).
fruit_color(grapes, purple).
fruit_color(orange, orange).
fruit_color(mango, yellow).
fruit_color(blueberry, blue).

% Rule to get color of a fruit
color_of_fruit(Fruit, Color) :-
    fruit_color(Fruit, Color).

% Rule to get fruit by color
fruit_with_color(Color, Fruit) :-
    fruit_color(Fruit, Color).
