fib(0,1).
fib(1, 1).
fib(N,F) :-
        N > 1,fib(N,1,1,F).
fib(2,F1,F2,F):-F is F1+F2.
fib(N,F1,F2,F):-N>2,N1 is N-1,NF1 is F1+F2,fib(N,NF1,F1,F)

        
