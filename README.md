# MazezamSolvers

MazezamSolvers is a set of solvers for the puzzle game MazezaM. An example version of the game can be played online [here](https://www.puzzlescript.net/play.html?p=7718522).

NOTES:
  There is a main.py file which has a test case for all the functions
except DFS, because it enters a loop and never stops.

  For every function, e.g. BFS, DFS, there is a second function BFS2, DFS2, etc.
The former does not use ranking/unranking, while the latter uses ranking/unranking.

  The file encoding.txt should contain the level encoding, so can be changed
to any level.

  There are test cases for every file, which are easier to test each functions
individually. Just go down to __main__ and change the inputs to whatever.

  For every search function I included a time counter for convenience.

Extra: I included a file BFS3.py, which asks whether to use ranking/unranking.

This project is avaliable through git via:
- SSH: git@src-code.simons-rock.edu:fkastrati13/MazezamSolvers.git
- HTTPS: https://src-code.simons-rock.edu/git/fkastrati13/MazezamSolvers.git
