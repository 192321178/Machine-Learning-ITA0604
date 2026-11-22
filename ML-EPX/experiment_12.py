import random

random.seed(12)
X = [-5 + i * 10 / 49 for i in range(50)]
y = [x * x + 3 * x + 2 for x in X]

def mean_squared_error(program):
    b, c = program
    predictions = [x * x + b * x + c for x in X]
    return sum((actual - predicted) ** 2
               for actual, predicted in zip(y, predictions)) / len(X)

# Each pair (b, c) describes the expression tree:
# add(add(mul(X, X), mul(b, X)), c)
population = [(random.randint(-5, 5), random.randint(-5, 5))
              for _ in range(30)]
for _ in range(100):
    population.sort(key=mean_squared_error)
    next_generation = population[:4]  # elitism
    while len(next_generation) < 30:
        parent1, parent2 = random.sample(population[:10], 2)
        child = [parent1[0], parent2[1]]  # crossover
        if random.random() < 0.30:
            child[0] = random.randint(-5, 5)
        if random.random() < 0.30:
            child[1] = random.randint(-5, 5)
        next_generation.append(tuple(child))
    population = next_generation

best = min(population, key=mean_squared_error)
b, c = best
print(f'Evolved expression: x^2 + {b}x + {c}')
print(f'Mean squared error: {mean_squared_error(best):.1f}')
