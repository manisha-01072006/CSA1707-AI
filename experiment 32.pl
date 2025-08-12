% Facts: gender
female(pam).
female(liz).
female(ann).
female(pat).

male(tom).
male(bob).
male(jim).

% Facts: parent-child relationships
parent(pam, bob).
parent(tom, bob).
parent(pam, liz).
parent(tom, liz).
parent(bob, ann).
parent(pat, ann).
parent(bob, jim).
parent(pat, jim).

% Rules

% mother: X is mother of Y if X is female and parent of Y
mother(X, Y) :-
    female(X),
    parent(X, Y).

% father: X is father of Y if X is male and parent of Y
father(X, Y) :-
    male(X),
    parent(X, Y).

% grandfather: X is grandfather of Y if X is male and parent of Z, and Z is parent of Y
grandfather(X, Y) :-
    male(X),
    parent(X, Z),
    parent(Z, Y).

% grandmother: X is grandmother of Y if X is female and parent of Z, and Z is parent of Y
grandmother(X, Y) :-
    female(X),
    parent(X, Z),
    parent(Z, Y).

% sister: X is sister of Y if X is female, they have the same parent, and X is not Y
sister(X, Y) :-
    female(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% brother: X is brother of Y if X is male, they have the same parent, and X is not Y
brother(X, Y) :-
    male(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.
