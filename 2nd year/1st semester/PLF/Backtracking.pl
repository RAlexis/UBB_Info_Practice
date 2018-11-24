% Seminar 4

% inserare(List, Element, Result)
% inserare(i, i, o)
ins(L, E, [E|L]).
ins([H|T], E, R) :- ins(T, E, R2), R = [H|R2].

% permutari(List, Result)
% permutari(i, o)
perm([], []).
perm([H|T], R) :-
    perm(T, R2),
    ins(R2, H, R).

allPerm(L, LS) :-
    findall(S, perm(L, S), LS).

% combinari(L, K, R)
% combinari(i, i, o)
comb(_, 0, []).
comb([], _, []).
comb([H|T], K, R) :-
    K > 0,
    K2 is K - 1,
    comb(T, K2, R2),
    R = [H|R2].
comb([_|T], K, R) :-
    K > 0,
    comb(T, K, R).

allComb(L, K, LS) :-
    findall(S, comb(L, K, S), LS).

% aranjamente(L, K, R)
% aranjamente(i, i, o)
aranj([], _, []).
aranj(_, 0, []).
aranj(L, K, R) :-
    comb(L, K, RC),
    perm(RC, R).

allAranj(L, K, LS) :-
    findall(S, aranj(L, K, S), LS).

listProduct([], P, P).
listProduct([H|T], P, R) :-
    P2 is P * H,
    listProduct(T, P2, R).

listSum([], S, S).
listSum([H|T], S, R) :-
    S2 is S + H,
    listSum(T, S2, R).

oneSol(L, K, S, P, R) :-
    aranj(L, K, LA),
    listSum(LA, 0, S),
    listProduct(LA, 1, P),
    R = LA.

% Aranjamentele de cate 2 elemente
% care au suma S si produsul P
% allSol([1, 3, 10], 2, 13, 30, R).
% R = [[3, 10], [10, 3]]
allSol(L, K, S, P, R) :-
    findall(RO, oneSol(L, K, S, P, RO), R).

% -------- %

% list1ToN(5, 1, R) => [1, 2, 3, 4, 5]
list1ToN(N, ACC, []) :- N =:= ACC - 1.
list1ToN(N, ACC, R) :-
    ACC2 is ACC + 1,
    list1ToN(N, ACC2, R2),
    R = [ACC | R2].

nlist(N, R) :- list1ToN(N, 1, R), !.

% ensures that all elements of a given array
% are consecutive

consec([_], true).
consec([H1, H2 | T], R) :-
    H2 =:= H1 + 1,
    consec([H2 | T], R).
consec([H1, H2 | _], false) :-
    H1 >= H2.


oneSolPr15(L, N, K, R) :-
    comb(L, K, LA),
    listSum(LA, 0, N),
    consec(LA, true),
    R = LA,
    write(R).

%oneSolPr15Wrapper2(_, N, K, []) :- K > N.

oneSolPr15Wrapper2(L, N, K, R) :-
   oneSolPr15(L, N, K, _), !,
   %write(K),
   K2 is K + 1,
   %write(k+K+k2+K2+n+N),put(10),
   K2 =< N, !,
   %write(cont),put(10),
   oneSolPr15Wrapper2(L, N, K2, R).

osp(0, []).
osp(N, R) :-
    nlist(N, NLST),
    %write(NLST),
    oneSolPr15Wrapper2(NLST, N, 1, R).
