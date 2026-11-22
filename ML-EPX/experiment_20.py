import math

def sample_complexity(hypothesis_count, epsilon, delta):
    return math.ceil((math.log(hypothesis_count) + math.log(1 / delta)) / epsilon)

for size in [10, 100, 1000]:
    required = sample_complexity(size, epsilon=0.1, delta=0.05)
    print(f'|H|={size}: m >= {required} examples needed')
