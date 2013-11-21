Easy part -- bash
=========

Imagine that you have two text files.
How would you concatenate them?
----
How would you implement column output:
that is the context of two files side-by-side.

SQL
===

Imagine you have a two-column table. This
table represents events occured in the system.

The first column is event timestamp, the second
is event description.

Your task is to select all event occured last month.

Please provide an SQL code.


Labyrinth
=========

The Task
--------

Find a shortest in the labyrinth.


Data format
-----------

The labyrinth is defined as an array
of orrays of integers.
0 means the path is open, 1 -- blocked.
``@'' means initial position, * -- destination.

int[][] labyrinth = new int[][]{
  { 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 },
  { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
  { 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 },
  { 0, 0, 0, 0, 0, 1, 0, 1, 1, 1 },
  { 0, @, 0, 0, 0, 1, 0, 0, 0, * }
};

Constraints
-----------

You have 1h to build a working prototype.



Questions
---------

1. What is the complexity of the solution?
(in terms of big-oh (O) notation)
2. Any other way to solve the problem?
3. Can you improve the code to output the length
of the shortest path?
