import math

hypotheses = list(range(10))  # h_t(x) predicts True when x >= t.
target = lambda x: x >= 4
mistakes = 0

for x in range(10):
    votes = [x >= threshold for threshold in hypotheses]
    majority_prediction = sum(votes) > len(votes) / 2
    true_label = target(x)
    if majority_prediction != true_label:
        mistakes += 1
    hypotheses = [threshold for threshold in hypotheses
                  if (x >= threshold) == true_label]

print('Mistakes made:', mistakes)
print('Theoretical bound log2(|H|):', round(math.log2(10), 2))
