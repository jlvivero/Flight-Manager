/* prolog tutorial 2.15 Graph structures and paths */

vuelos(A, B, C, Path, Len) :- path(A, B, Path, Len), length(Path, C1), C is C1 - 2.

path(A,B,Path,Len) :-
       travel(A,B,[A],Q,Len),
       reverse(Q,Path).

travel(A,B,P,[B|P],L) :-
       edge(A,B,L).
travel(A,B,Visited,Path,L) :-
       edge(A,C,D),
       C \== B,
       \+member(C,Visited),
       travel(C,B,[C|Visited],Path,L1),
       L is D+L1.
