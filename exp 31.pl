% Facts: Birds that can fly
can_fly(sparrow).
can_fly(eagle).
can_fly(pigeon).
can_fly(parrot).

% Facts: Birds that cannot fly
cannot_fly(ostrich).
cannot_fly(penguin).
cannot_fly(kiwi).

% Rule: To check if a bird can fly
bird_can_fly(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly.'), nl.

bird_can_fly(Bird) :-
    cannot_fly(Bird),
    write(Bird), write(' cannot fly.'), nl.
