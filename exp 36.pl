% Best First Search in Prolog

% Edge format: edge(Node1, Node2, Cost)
edge(a, b, 4).
edge(a, c, 3).
edge(b, d, 5).
edge(b, e, 12).
edge(c, f, 7).
edge(c, g, 10).
edge(d, h, 3).
edge(e, i, 2).
edge(f, j, 4).
edge(g, k, 6).

% Heuristic values (h-value for each node)
heuristic(a, 10).
heuristic(b, 8).
heuristic(c, 5).
heuristic(d, 7).
heuristic(e, 3).
heuristic(f, 6).
heuristic(g, 4).
heuristic(h, 0).
heuristic(i, 0).
heuristic(j, 0).
heuristic(k, 0).

% Best First Search
best_first_search(Start, Goal, Path) :-
    bfs([[Start]], Goal, Path).

% If first path's head is the Goal
bfs([[Goal | Rest] | _], Goal, Path) :-
    reverse([Goal | Rest], Path).

% Expand paths
bfs([ [Current | Rest] | Others], Goal, Path) :-
    findall([Next, Current | Rest],
            (edge(Current, Next, _), \+ member(Next, [Current | Rest])),
            NewPaths),
    evaluate_paths(NewPaths, Evaluated),
    append(Others, Evaluated, AllPaths),
    sort(0, @=<, AllPaths, SortedPaths),  % Sort based on heuristic
    bfs(SortedPaths, Goal, Path).

% Evaluate paths using heuristic
evaluate_paths([], []).
evaluate_paths([[Node | Rest] | T], [[Node | Rest] | ET]) :-
    heuristic(Node, _),
    evaluate_paths(T, ET).
