sudoku-solutionchecker
======================
A program to check whether a sudoku puzzle is correctly solved or otherwise.<br>
For more information on how to solve sudoku check <a href="http://en.wikipedia.org/wiki/Sudoku">this link</a>
The solution is done without a complex graph-searching algorithm. Instead, <a href = "http://en.wikibooks.org/wiki/Python_Programming/Sets#Set_Difference">set difference</a>(a unique feature of Python) is used to determine whether a row, a column, or a sub-square of 3x3 dimension really satisfies the condition of having the number 1-9 within the given area.
