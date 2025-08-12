% --- Facts ---
has_hair(dog).
has_hair(cat).
gives_milk(dog).
gives_milk(cat).
lays_eggs(hen).
lays_eggs(snake).
has_scales(snake).
has_feathers(hen).

% --- Rules ---
mammal(X) :- has_hair(X), gives_milk(X).
bird(X) :- has_feathers(X), lays_eggs(X).
reptile(X) :- has_scales(X), lays_eggs(X).

% Top-level classification
animal_type(X, mammal) :- mammal(X).
animal_type(X, bird) :- bird(X).
animal_type(X, reptile) :- reptile(X).
