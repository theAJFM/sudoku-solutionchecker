sudoku-solutionchecker
======================
A program to check whether a sudoku puzzle is correctly solved or otherwise.<br>
For more information on how to solve sudoku check <a href="http://en.wikipedia.org/wiki/Sudoku">this link</a>
<br><br>The solution is done without a complex graph-searching algorithm. Instead, I used <a href = "http://en.wikibooks.org/wiki/Python_Programming/Sets#Set_Difference">set difference</a> (a unique feature of Python) to determine whether a row, a column, or a sub-grid of 3x3 dimension really satisfies the condition of having the number 1-9 within the given section of the 9x9 grid.
<br><br>There are two solutions available. The first one has a straightforward 'YES' or 'NO' output. In addition to the first solution's answer, the second one also holds the explanation of why the grid was not properly filled, with the expense of longer running time (Worst case, every section of the grid will be assessed)
