#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear O(n) runtime. The while loop makes it so it will keep growing (a = a + n * n) at the same rate on every pass through until it meets its limit. the graph will show a straight diagonal line. 


b) Linearithmic O(n log n) runtime. as the input increases, the while loop does more loops to satisify its condition. this slightly increases the runtime as inputs get bigger. 


c) Linear O(n) runtime. same speed and growth the whole way through. 

## Exercise II

n = stories
f = floor that eggs start breaking when dropped
set eggs broken to false

while loop through each story as long as eggs broken is false
  drop an egg off each story.
  if egg breaks then assign f to that story. 
    set eggs broken to True and break loop.
  otherwise keep looping. 

Linear O(n). loop will continue at same rate until condition met. 


