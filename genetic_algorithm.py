import population, sys, getopt

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
    
import sys, getopt

def parseCommandLine(argv):
    params = {'mutation_prob':.001,'max_iterations':1000000,'nqueens':8,'population_size':10} 
    
    try:
        opts, args = getopt.getopt(argv,"hm:i:n:p:",["mutation_prob=","max_iterations=","nqueens=","population_size="])
        
    except getopt.GetoptError:
        print 'genetic_algorithm.py -i <max_iterations> -m <mutation_prob> -n <nqueens> -p <population_size>'
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
             print 'genetic_algorithm.py -i <max_iterations> -m <mutation_prob> -n <nqueens> -p <population_size>'
             sys.exit()
        elif opt in ("-i", "--max_iterations"):
            params['max_iterations'] = int(arg)
        elif opt in ("-m", "--mutation_prob"):
            params['mutation_prob'] = float(arg)
        elif opt in ("-n", "--nqueens"):
            params['nqueens'] = int(arg)
        elif opt in ("-p", "--population_size"):
            params['population_size'] = int(arg)
            
    return params
    
            
if __name__ == "__main__":
    parameters = parseCommandLine(sys.argv[1:])
    
    population =  population.Population(parameters['nqueens'], parameters['population_size'])
    g = GeneticAlgorithm(parameters['mutation_prob'],parameters['max_iterations'])
    print g.find_solution(population)
