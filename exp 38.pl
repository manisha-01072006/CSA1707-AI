% ---------- Facts ----------
fact(has_fever).
fact(has_cough).
fact(has_sore_throat).
fact(has_body_ache).

% ---------- Rules ----------
rule(flu, [has_fever, has_cough, has_body_ache]).
rule(common_cold, [has_cough, has_sore_throat]).
rule(covid19, [has_fever, has_cough, has_sore_throat, has_body_ache]).

% ---------- Forward Chaining Engine ----------
forward_chain :-
    find_new_fact(Fact),
    \+ fact(Fact),    % if not already known
    assert(fact(Fact)),
    write('New fact deduced: '), writeln(Fact),
    forward_chain.
forward_chain :- 
    write('No new facts can be deduced.'), nl.

find_new_fact(Conclusion) :-
    rule(Conclusion, Conditions),
    all_facts_known(Conditions).

all_facts_known([]).
all_facts_known([H|T]) :-
    fact(H),
    all_facts_known(T).

% ---------- Query to Run ----------
diagnose :-
    forward_chain,
    write('Final facts: '), nl,
    list_facts.

list_facts :-
    fact(F),
    write('- '), writeln(F),
    fail.
list_facts.
