import chromosome

class Population:

    def __init__(self, num_queens=8, population_size=10):
        self.num_queens = num_queens
        self.population_size = population_size
        self.population = self.generatePopulation()
        print "Population - Num Queens: " + str(self.num_queens) + " Population Size: " + str(self.population_size)

    def generatePopulation(self):
        population = []
        for index in range(self.population_size):
            population.append(chromosome.Chromosome.random(self.num_queens))
        population.sort()
        return population
    
    def replaceChromosome(self, new_c, old_c):
        self.population.append(new_c)
        self.population.remove(old_c)
        self.population.sort()
        
    def sort(self):
        self.population.sort()
        
    def __str__(self):
        return "\n".join([str(chromosome) for chromosome in self.population])
    
    def __len__(self):
        return len(self.population)
    
    def __getitem__(self, index):
        return self.population[index]
    
if __name__ == "__main__":
    print Population()
