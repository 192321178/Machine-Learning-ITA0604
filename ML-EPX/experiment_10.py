import random

random.seed(7)

def decode(chromosome):
    return int(chromosome, 2)

def fitness(chromosome):
    return decode(chromosome) ** 2

# Include one valid high-fitness chromosome and fill the rest randomly.
population = ['11111'] + [
    ''.join(random.choice('01') for _ in range(5)) for _ in range(5)
]

for _ in range(20):
    scores = [fitness(chromosome) for chromosome in population]
    new_population = [max(population, key=fitness)]  # elitism
    while len(new_population) < 6:
        parent1, parent2 = random.choices(population, weights=scores, k=2)
        point = random.randint(1, 4)
        child = parent1[:point] + parent2[point:]
        child = ''.join(bit if random.random() > 0.05 else str(1 - int(bit))
                        for bit in child)
        new_population.append(child)
    population = new_population

best = max(population, key=fitness)
print('Best x =', decode(best))
print('Maximum f(x) =', fitness(best))
