% Medical Diagnosis System

% Facts: symptom(Disease, Symptom)
symptom(cold, sneezing).
symptom(cold, runny_nose).
symptom(cold, sore_throat).

symptom(flu, fever).
symptom(flu, headache).
symptom(flu, body_ache).
symptom(flu, chills).

symptom(malaria, fever).
symptom(malaria, chills).
symptom(malaria, sweating).
symptom(malaria, nausea).

symptom(typhoid, fever).
symptom(typhoid, headache).
symptom(typhoid, abdominal_pain).
symptom(typhoid, diarrhea).

% Rule: diagnosis
diagnose(Disease) :-
    write('Enter symptoms one by one, end with "done":'), nl,
    read_symptoms(Symptoms),
    match_disease(Disease, Symptoms).

% Read symptoms from user
read_symptoms(Symptoms) :-
    read(Symptom),
    ( Symptom == done ->
        Symptoms = []
    ; read_symptoms(Rest),
      Symptoms = [Symptom | Rest]
    ).

% Match disease if all required symptoms are present
match_disease(Disease, Symptoms) :-
    findall(S, symptom(Disease, S), DiseaseSymptoms),
    subset(DiseaseSymptoms, Symptoms),
    write('You might have: '), write(Disease), nl.

% Helper: check subset
subset([], _).
subset([H|T], List) :-
    member(H, List),
    subset(T, List).
