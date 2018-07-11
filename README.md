# Genetic-Algorithm
Solving the n-Queens Problem using Genetic Algorithm.

## Prerequisites

* Python2

## Working
### Representation of a Board
* The chromosome used to represent a possible solution to the n-Queens problem is of the form ```[2,3,4,5,6,7,0,1]``` for a board of size 8 to represent the board where the queen in the first row is in the 2th column, the queen in the second row is in the 3th column(0 based indexing) and so on.   
### Initialization of random board population
* A random set of chromosomes are generated initially to serve as the population for the first iteration of the Genetic Algorithm.
### Fitness
* The fitness of a chromosome is defined in terms of the number of good queens present in the board. A good queen is one which does not attack any other queen piece ( not on same row,column or diagonal as another queen).
* Therefore, for a board of size 8, maximum fitness would be 8.
### Crossover
* Chromosomes ```[1, 0, 6, 3, 5, 7, 4, 2]``` and ```[7, 2, 6, 1, 5, 3, 0, 4]``` undergo crossover at some random position say index = 4 to form ```[1,0,6,3,7,2,5,4]``` and  ```[7, 2, 6, 1, 0, 3, 5, 4]```
* This modification of the typical crossover operation is done so as to always create valid chromosomes in terms of column number.(no possibility of same number in a chromosome)
### Mutation 
* Chromosome ```[1, 0, 6, 3, 5, 7, 4, 2]``` undergo mutation at some random position say index = 2 to form ```[1, 0, 3, 6, 5, 7, 4, 2]``` (swap elements at index 2 and 3)
* This modification of the typical mutation operation is done so as to always create valid chromosomes in terms of column number.(no possibility of same number in a chromosome)

## Running

For running with default settings,

    python nQueens.py
    
To run with different settings

    python nQueens.py --h
    usage: nQueens.py [-h] [--mutate MUTATE] [--cross CROSS] [--pop POP] [--n N]
                      [--iter ITER]

    optional arguments:
      -h, --help       show this help message and exit
      --mutate MUTATE  mutation rate
      --cross CROSS    crossover rate
      --pop POP        initial population
      --n N            board size
      --iter ITER      number of iterations

## Example

Running

    python nQueens.py
    
gives output board

    - Q - - - - - - 
    - - - - Q - - - 
    - - - - - - Q - 
    - - - Q - - - - 
    Q - - - - - - - 
    - - - - - - - Q 
    - - - - - Q - - 
    - - Q - - - - - 
    
On running,

    python nQueens.py --n 12
    
No solution is obtained by using the default settings

On tuning the settings,

    python nQueens.py --n 12 --pop 500 --cross 0.7 

We can obtain a solution

    - - - - - Q - - - - - - 
    - - - - - - - Q - - - - 
    Q - - - - - - - - - - - 
    - - - - - - - - - - - Q 
    - - - - - - - - Q - - - 
    - - - - Q - - - - - - - 
    - Q - - - - - - - - - - 
    - - - Q - - - - - - - - 
    - - - - - - - - - Q - - 
    - - - - - - Q - - - - - 
    - - - - - - - - - - Q - 
    - - Q - - - - - - - - - 
