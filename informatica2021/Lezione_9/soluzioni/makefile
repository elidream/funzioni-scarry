# Questo makefile contiene le istruzioni per compilare tutti gli esercizi
# Qui ho utilizzato alcune funzionalita' piu' avanzate del makefile come
# la definizione di variabili, CC, e riferimenti $@ e $<.
CC=g++

all: prog1 prog4

prog1: esercizio1.cc funzioni.cc
	$(CC) -o $@ esercizio1.cc funzioni.cc

prog4: esercizio4.cc
	$(CC) -o $@ $<

clean:
	rm -f prog1 prog4
