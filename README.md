# Cooccurrence


cooccurrence probability is defined as: 
p (A, B , k ) = cooccurrence(A, B, k) / count(A)

Given an input document, calculates all cooccurrence probabilities for a document and 
given range K. For one word pair A and B per line; prints the cooccurrence probability of A, B. 


	python3 src/cooccurrence.py test/cat-in-the-hat.txt 3 < test/inputs.txt

unit tests

	nosetests

