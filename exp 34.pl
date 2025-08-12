% Monkey and Banana Problem
% State is represented as: state(MonkeyPosition, MonkeyOnBox?, BoxPosition, HasBanana?)

% The goal is to have HasBanana = yes
goal_state(state(_, _, _, yes)).

% Initial state: Monkey at door, on the floor, box at window, doesn't have banana
start_state(state(at_door, on_floor, at_window, no)).

% Move action
move(state(MP, on_floor, BP, HB), move(MP, NP), state(NP, on_floor, BP, HB)) :-
    MP \= NP,
    member(NP, [at_door, at_window, middle_room]).

% Push action (Monkey can push box if at same location)
move(state(P, on_floor, P, HB), push(P, NP), state(NP, on_floor, NP, HB)) :-
    P \= NP,
    member(NP, [at_door, at_window, middle_room]).

% Climb action (Monkey climbs the box)
move(state(P, on_floor, P, HB), climb, state(P, on_box, P, HB)).

% Grab banana action
move(state(middle_room, on_box, middle_room, no), grab, state(middle_room, on_box, middle_room, yes)).

% Path finding
path(State, []) :- goal_state(State).
path(State, [Action|Rest]) :-
    move(State, Action, NewState),
    path(NewState, Rest).

% Solve and display steps
solve :-
    start_state(Start),
    path(Start, Actions),
    write('Steps to get the banana: '), nl,
    write(Actions), nl.
