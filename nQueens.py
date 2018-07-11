from __future__ import print_function
import random
import copy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--mutate", help="mutation rate",default=0.01,type=float)
parser.add_argument("--cross", help="crossover rate",default=0.5,type=float)
parser.add_argument("--pop", help="initial population",default=100,type=int)
parser.add_argument("--n", help="board size",default=8,type=int)
parser.add_argument("--iter", help="number of iterations",default=200,type=int)

args = parser.parse_args()
mutation_rate = args.mutate
crossover_rate = args.cross
population = args.pop
board_size = args.n
max_iter = args.iter

boards = []

def init():
	for i in range(population):
		board = [0] * board_size
		available = list(range(0,board_size))
		for j in range(board_size):
			board[j] = random.choice(available)
			available.remove(board[j])
		boards.append(board)

def fitness(board):
	fitness = 0
	for i in range(len(board)):
		isSafe = True
		for j in range(len(board)):
			if i!=j:
				if (board[i] == board[j]) or (abs(board[i] - board[j]) == abs(i-j)):
					isSafe = False
					break
		if(isSafe==True):
			fitness += 1
	return fitness

def mutation(board):
	print('mutation')
	print(board)
	index = random.randint(0,board_size-2)
	print('index',index)
	newBoard = copy.copy(board)
	t = newBoard[index]
	newBoard[index] = newBoard[index+1]
	newBoard[index+1] = t
	return newBoard

def crossover(board1,board2):
	print('crossover')
	c = random.randint(1,board_size-2)
	print(c)
	newIndividual1 = board1[:c]
	for i in board2:
		if i not in newIndividual1:
			newIndividual1.append(i)
	newIndividual2 = board2[:c]
	for i in board1:
		if i not in newIndividual2:
			newIndividual2.append(i)
	return (newIndividual1,newIndividual2)

def printBoard(chromosome):
	for i in chromosome:
		for x in range(i):
			print("-",end=' ') 
		print('Q', end=' ')
		for x in range(board_size-i-1):
			print("-",end=' ') 
		print()
init()

generation = 1

# run genetic algorithm
while True:
    print("Generation: " + str(generation))
    scores = []
    goodBoards = []
    for i in range(len(boards)):
    	print(boards[i])
        scores.append((fitness(boards[i]), i))
    scores.sort(reverse=True)
    print(scores)
    bestScore = scores[0][0]
    print("Best Score: " + str(bestScore))
    if(bestScore==board_size):
    	print(bestScore)
    	print(boards[scores[0][1]])
    	printBoard(boards[scores[0][1]])
    	break
    sum = 0
    for i in range(population/2):
        goodBoards.append(boards[scores[i][1]])
    boards = copy.copy(goodBoards)
    print(boards)
    for i in range(len(goodBoards)):
    	if(random.random()<mutation_rate):
        	boards.append(mutation(goodBoards[i]))
        if(random.random()<crossover_rate and i != len(goodBoards)-1):
        	print(i)
        	crossover_results = crossover(goodBoards[i],goodBoards[i+1])
        	print(crossover_results)
        	boards.append(crossover_results[0])
        	boards.append(crossover_results[1])
    print(len(boards))
    generation += 1
    if(generation>max_iter):	
    	break

