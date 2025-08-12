% Facts: name(Name, DOB)
name_dob('Alice', date(12, 5, 2000)).
name_dob('Bob', date(23, 8, 1998)).
name_dob('Charlie', date(1, 1, 2002)).
name_dob('David', date(15, 7, 1995)).

% Rule to display DOB for a given name
get_dob(Name) :-
    name_dob(Name, date(Day, Month, Year)),
    format('~w was born on ~w/~w/~w.~n', [Name, Day, Month, Year]).
