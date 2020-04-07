This document is still in progress ...

# SUDOKU

## About the project

This project consists of a Sudoku implementation

### About the problem

SUDOKU is a puzzle in which players insert the numbers one to nine into a grid consisting of nine squares subdivided into a further nine smaller squares (9x9) in such a way that every number appears once in each horizontal line, vertical line, and square.

## Requirements

TODO

## Executing the program

For execute:

1. run the next command

```bash
```bash
make
```````

note:

make clear is available to docker down and clear
make down is available to docker down
make underground is available for run in background
make or make run will execute the application(s)

2. make a GET request to

host + /sudoku/game

this will return a sudoku game in a string format as 82 numbers from 1-9 , cero is not present you can find a dot (.) for blank space as the next examples:

245981376169273584837564219976125438513498627482736951391657842728349165654812793:

2 4 5 | 9 8 1 | 3 7 6  
1 6 9 | 2 7 3 | 5 8 4  
8 3 7 | 5 6 4 | 2 1 9  
------+-------+------  
9 7 6 | 1 2 5 | 4 3 8  
5 1 3 | 4 9 8 | 6 2 7  
4 8 2 | 7 3 6 | 9 5 1  
------+-------+------  
3 9 1 | 6 5 7 | 8 4 2  
7 2 8 | 3 4 9 | 1 6 5  
6 5 4 | 8 1 2 | 7 9 3  

2...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3:

2 . . | . 8 . | 3 . .  
. 6 . | . 7 . | . 8 4  
. 3 . | 5 . . | 2 . 9  
------+-------+------  
. . . | 1 . 5 | 4 . 8  
. . . | . . . | . . .  
4 . 2 | 7 . 6 | . . .  
------+-------+------  
3 . 1 | . . 7 | . 4 .  
7 2 . | . 4 . | . 6 .  
. . 4 | . 1 . | . . 3  



this will continue...

###### **End of README**

