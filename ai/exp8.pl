% Prior probabilities for weather conditions 
prior(sunny, 0.5). 
prior(rainy, 0.3). 
prior(cloudy, 0.2). 

% Conditional probabilities of evidence given weather condition 
probability(cloudy, sunny, 0.2). 
probability(cloudy, rainy, 0.7). 
probability(cloudy, cloudy, 0.9). 
probability(humidity, sunny, 0.3). 
probability(humidity, rainy, 0.8). 
probability(humidity, cloudy, 0.6). 

% Bayesian inference for weather prediction 
bayes(Weather, Evidence, Posterior) :- 
    prior(Weather, Prior), 
    probability(Evidence, Weather, GivenProb), 
    Posterior is Prior * GivenProb.

% Automatically run the query to display the posterior probability 
:- initialization(run_sample_query). 

% Run the sample query when the file is loaded 
run_sample_query :- 
    bayes(sunny, cloudy, P), 
    write('Posterior Probability for sunny with cloudy evidence: '), 
    write(P), nl.
