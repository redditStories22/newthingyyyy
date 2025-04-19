% Define the symptoms
symptom(fever).
symptom(cough).
symptom(headache).
symptom(fatigue).
symptom(sore_throat).
symptom(rash).
symptom(shortness_of_breath).
symptom(nausea).
symptom(chills).
symptom(muscle_ache).

% Define diseases and their associated symptoms
disease(flu, [fever, cough, sore_throat, fatigue, headache]).
disease(cold, [cough, sore_throat, fatigue]).
disease(covid19, [fever, cough, fatigue, sore_throat, shortness_of_breath, headache, chills]).
disease(pneumonia, [cough, fever, shortness_of_breath, fatigue, muscle_ache]).
disease(malaria, [fever, chills, headache, nausea, muscle_ache]).

% Ask user about symptoms and collect them
ask_symptoms(Symptoms) :-
    findall(Symptom, (symptom(Symptom), ask_symptom(Symptom)), Symptoms).

% Ask whether the user has a particular symptom
ask_symptom(Symptom) :-
    format('Do you have ~w? (yes/no): ', [Symptom]),
    read(Response),
    Response == yes.

matches_disease(Disease, Symptoms) :-
    disease(Disease, DiseaseSymptoms),
    intersection(DiseaseSymptoms, Symptoms, CommonSymptoms),
    length(CommonSymptoms, Length),
    Length >= 3.  % At least 3 symptoms must match

% Find all possible diagnoses
find_diagnoses(Symptoms, Diseases) :-
    findall(Disease, matches_disease(Disease, Symptoms), Diseases).

% Output the list of diagnosed diseases
output_diagnosis([]) :-
    write('No disease matched the symptoms.'), nl.
output_diagnosis(Diseases) :-
    maplist(write_disease, Diseases).

% Output each disease in the diagnosis list
write_disease(Disease) :-
    write('Diagnosed with: '), write(Disease), nl.

% Define intersection/3 to find common elements between two lists
intersection([], _, []).
intersection([X|Xs], Ys, [X|Zs]) :-
    member(X, Ys),
    intersection(Xs, Ys, Zs).
intersection([X|Xs], Ys, Zs) :-
    member(X, Ys),
    intersection(Xs, Ys, Zs).

% Run the forward chaining on start
:- initialization(forward_chaining).

% Forward chaining to collect symptoms and find diagnoses
forward_chaining :-
    ask_symptoms(Symptoms),
    find_diagnoses(Symptoms, Diseases),
    output_diagnosis(Diseases).
    