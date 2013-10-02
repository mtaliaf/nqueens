nqueens
=======

genetic algorithm solution to the n queens problem

representation of board state - n-tuple notation; list that is n long. index is the column and value is row with which 
  the queen resides.  Using this notation allows you to ensure no row or column conflicts at chromosome creation time.  

selection - Three chromosomes are chosen randomly from the population. We create a new chromosome from the selected 
  two most fit chromosomes.  We then replace the least fit with the new chromosome.
  
cross over - the new chromosome shares any matching elements from the two parents.  i.e. if index 5 of both parents 
  is 2, then the new child will have a two at index 5.  All other indexes are filled in at random with care not to
  introduce row conflicts

mutation - simply switch two of the positions in the chromosome.  mutation probability is should be low i.e. .001
