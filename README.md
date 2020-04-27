Document Under Construccion...

# SUDOKU

## About the problem

SUDOKU is a puzzle in which players insert the numbers one to nine into a grid consisting of nine squares subdivided into a further nine smaller squares (9x9) in such a way that every number appears once in each horizontal line, vertical line, and square.

## About the project

This project consists of a Sudoku implementation implemented on two applications named data-provider and app.

The **data-provider** application is designed to provide the sudoku games with a possible answer, the difficulty level and the number of games. **data-provider** also includes a validate sudoku option that will check in sudoku have all his input valid, and a complete option that will check the completion of the game as a valid game.

The **app** application, currently in construction, it's a WEB application that pretends to save the records of a player as win games, incomplete games, and the currently played game, for this implementation the application will work in conjunction with PostgreSQL Database. This application required to log in by user name and password.

## Requirements
- Python 3.8
- Docker-compose.
- WEB browser.

## Executing the program

For execute:

1. run the next command
 ```sh
  $ make
 ```````
 > Note: 
 > `make clear` is available to docker down and clear 
 > `make down` is available to docker down 
 > `make underground` is available for run in background 
 > `make` or `make run` will execute the application(s)
 > `make test` will run Unit test dor data-provider in this version, missing app testing will be release soon.

Done!!! congrats the project is up and running go to **http://0.0.0.0:5000/** in your web browser for WEB use or go to postman for *data-provider* requests 
**(localhost IP work for development, this IP will change in case of release and should be updated here)**

## **Did you want to down the application?**
Press ctrl+c (not needed if you run as `make underground` ) and execute:
```sh
 $ make down
```````
TODO: add a brief explanation
TODO: add clear

## ROUTES for data-provider
### 1. sudoku game 
make a GET request to: `host + /sudoku/game`
> Note: for development the host is set to http://0.0.0.0:8000/
> in this case will be `http://0.0.0.0:8000/sudoku/game`

This will return a sudoku game in a string format as 82 numbers from 1-9, cero is not present you can find a dot (.) for blank space as the next examples below, the response will also include the solution, index of game and difficulty, as we don't specify any specific will return the first game on the easy level.

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

### 2. Specific sudoku game
When requesting specific sudoku you will need to include the level and index as parameters, the route is the same as the last step.

* if you are working from your browser use `host` + `/sudoku/game?level=medium&index=8`
* if you are using post man just use `host` + `/sudoku/game` and add the parameters in the params field, remember to include **level** and **index**.

remember: for development, the host is set to http://0.0.0.0:8000/
in this case, will be `http://0.0.0.0:8000/sudoku/game?level=medium&index=8`

> Note:
> There are only three levels `easy`, `medium` and `hard`
> If your index is bigger than the existing games on that level it will return the first game from the next level, however, there are no more games after hard.

other routes will be added soon** to this document  
**Soon As defined by Blizzard Entertainment.

this document will continue...

###### **End of README**
