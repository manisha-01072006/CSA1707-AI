% Towers of Hanoi in Prolog
% hanoi(N, Source, Destination, Auxiliary)

hanoi(1, Source, Destination, _) :-
    write('Move disk from '), write(Source),
    write(' to '), write(Destination), nl.

hanoi(N, Source, Destination, Auxiliary) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Auxiliary, Destination),
    hanoi(1, Source, Destination, _),
    hanoi(M, Auxiliary, Destination, Source).
