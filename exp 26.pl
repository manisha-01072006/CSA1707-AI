% sum_to_n(N, Sum) :- Sum is the sum of integers from 1 to N.

sum_to_n(0, 0).  % Base case: sum of numbers up to 0 is 0.

sum_to_n(N, Sum) :-
    N > 0,                  % Ensure N is positive
    N1 is N - 1,            % Decrease N
    sum_to_n(N1, Sum1),     % Recursive call
    Sum is Sum1 + N.        % Add current N to sum
