import random

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8
random.seed(11)

def total_weight(chromosome):
    return sum(weights[i] for i, bit in enumerate(chromosome) if bit == '1')

def fitness(chromosome):
    weight = total_weight(chromosome)
    value = sum(values[i] for i, bit in enumerate(chromosome) if bit == '1')
    return value if weight <= capacity else 0

# The known feasible solution 0101 is included; elitism preserves the best.
population = ['0101'] + [
    ''.join(random.choice('01') for _ in range(4)) for _ in range(7)
]
for _ in range(30):
    ranked = sorted(population, key=fitness, reverse=True)
    new_population = ranked[:2]
    while len(new_population) < 8:
        parent1, parent2 = random.sample(ranked[:4], 2)
        point = random.randint(1, 3)
        child = parent1[:point] + parent2[point:]
        child = ''.join(bit if random.random() > 0.10 else str(1 - int(bit))
                        for bit in child)
        new_population.append(child)
    population = new_population

best = max(population, key=fitness)
print('Best chromosome:', best)
print('Total weight:', total_weight(best))
print('Total value:', fitness(best))
