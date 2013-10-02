import population
import chromosome
import random

class GeneticAlgorithm:
    def __init__(self, mutation_prob=.001, max_iterations = 1000000):
        self.mutation_prob = mutation_prob
        self.max_iterations = max_iterations
        
    def iteration(self, population):
        touny = random.sample(population,3)
        touny.sort()
        
        new_c = chromosome.Chromosome.fromParents(touny[0],touny[1])
        new_c.mutate(self.mutation_prob)
        
        population.replaceChromosome(new_c, touny[2])
        return population  
        
    def find_solution(self, population):
        print "Starting Algorithm - Mutation Probability: " + str(self.mutation_prob) + " Max Iterations: " + str(self.max_iterations)
        for i in range(self.max_iterations):
            population = self.iteration(population)
            if(population[0].cost == 0):
                print "Found in " + str(i) + " iterations"
                return population[0]
        print "No solution found"
        return population[0]
            
if __name__ == "__main__":
    population =  population.Population(8)
    g = GeneticAlgorithm()
    print g.find_solution(population)
