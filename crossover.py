# based on @AKSHAYRAJ4's work
# https://www.geeksforgeeks.org/python-single-point-crossover-in-genetic-algorithm/

import random

def crossover(l, q, verbose = False):
	'''
	function for implementing the single-point crossover
	'''
  
	# converting the string to list for performing the crossover
	l = list(l)
	q = list(q)
  
	# generating the random number to perform crossover
	k1 = random.randint(0, len(l)-1)
	if verbose : print("Crossover point 1:", k1)

	# generating the random number to perform crossover
	k2 = random.randint(0, len(q)-1)
	if verbose : print("Crossover point 2:", k2)
  
	# interchanging the genes
	r1 = l[0:k1] + q[k2:len(q)]
	r2 = q[0:k2] + l[k1:len(l)]

	if verbose : print(r1)
	if verbose : print(r2, "\n\n")

	return ''.join(r1), ''.join(r2)

def mutate(s, p = 0.9):
	if random.random() < p: #p is the probability of the mutation to occur, 1 is 100 % and 0 is 0 %
		l = list(s)
		rank = random.randint(0, len(l)-1)
		char_ord = ord(l[rank])
		if char_ord == 122 : char_ord = 96 # pour le z
		char_ord = char_ord + 1
		l[rank] = chr(char_ord)
		return ''.join(l)
	return s

def getCrossovers(s1, s2, n, rec = False, verbose = True):
	for _ in range(n):
		r1, r2 = crossover(s1, s2)
		if rec : s1,s2 = r1, r2
		if verbose : printCenteredText(mutate(r1) + ', ' + mutate(r2))
	return r1, r2

def getCrossoversList(s1, s2, n, rec = False):
	res1 = []
	res2 = []
	for _ in range(n):
		r1, r2 = getCrossovers(s1, s2, 1, rec, False)
		if rec : s1,s2 = r1, r2
		res1.append(r1)
		res2.append(r2)
	return res1, res2
