% Facts defining diseases and their symptoms  
symptom(flu, fever).  
symptom(flu, cough).  
symptom(flu, headache).  
symptom(flu, fatigue).  
symptom(flu, sore_throat).  
symptom(common_cold, sneezing).  
symptom(common_cold, runny_nose).  
symptom(common_cold, sore_throat).  
symptom(common_cold, cough).  
symptom(covid_19, fever).  
symptom(covid_19, cough).  
symptom(covid_19, loss_of_taste).  
symptom(covid_19, shortness_of_breath).  
symptom(covid_19, fatigue).  
symptom(pneumonia, fever).  
symptom(pneumonia, cough).  
symptom(pneumonia, shortness_of_breath).  
symptom(pneumonia, fatigue).  
symptom(malaria, fever).  
symptom(malaria, chills).  
symptom(malaria, headache).  
symptom(malaria, nausea).  
symptom(malaria, muscle_ache).  

% Rule to diagnose disease based on at least two matching symptoms  
diagnose(Disease) :-
    symptom(Disease, Symptom1),
    symptom(Disease, Symptom2),
    Symptom1 \= Symptom2,
    write('the patient may have '), write(Disease), nl.