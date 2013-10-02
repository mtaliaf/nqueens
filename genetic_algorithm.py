import population
import chromosome
import random

class GeneticAlgorithm:
    def __init__(self, mutation_prob=.001, max_iterations = 1000000):
        self.mutation_prob = mutation_prob
        self.max_iterations = max_iterations
        
    def find_solution(self, population):
        print "Starting Algorithm - Mutation Probability: {} Max Iterations: {}".format(self.mutation_prob, self.max_iterations)
        
        for i in range(self.max_iterations):
            population = population.breed(self.mutation_prob)
            if(population[0].cost == 0):
                print "Found in {} iterations".format(i)
                return population[0]
        print "No solution found"
        return population[0]
            
if __name__ == "__main__":
    population =  population.Population(8)
    g = GeneticAlgorithm()
    print g.find_solution(population)
