% Define winning conditions
win(Player, Board) :-
    Board = [Player, Player, Player, _, _, _, _, _, _];
    Board = [_, _, _, Player, Player, Player, _, _, _];
    Board = [_, _, _, _, _, _, Player, Player, Player];
    Board = [Player, _, _, Player, _, _, Player, _, _];
    Board = [_, Player, _, _, Player, _, _, Player, _];
    Board = [_, _, Player, _, _, Player, _, _, Player];
    Board = [Player, _, _, _, Player, _, _, _, Player];
    Board = [_, _, Player, _, Player, _, Player, _, _].

% Rule to check if a position is free
free(Position, Board) :-
    nth0(Position, Board, empty).

% AI move: take the winning move if possible
best_move(Board, Move) :-
    nth0(Move, Board, empty),
    replace(Board, Move, x, NewBoard),
    win(x, NewBoard), !.

% AI move: block opponent if they are about to win
best_move(Board, Move) :-
    nth0(Move, Board, empty),
    replace(Board, Move, o, NewBoard),
    win(o, NewBoard), !.

% AI move: choose the first available move
best_move(Board, Move) :-
    nth0(Move, Board, empty), !.

% Replace an element at a specific position in a list
replace([_|T], 0, Elem, [Elem|T]).
replace([H|T], Index, Elem, [H|R]) :-
    Index > 0,
    Index1 is Index - 1,
    replace(T, Index1, Elem, R).

% Automatically run the sample query when the file is loaded
:- initialization(run_sample_query).

run_sample_query :-
    Board = [x, o, x, empty, o, empty, empty, empty, empty],
    best_move(Board, Move),
    write('AI\'s best move is at position: '), write(Move), nl.
