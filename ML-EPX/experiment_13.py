prior = 0.01
sensitivity = 0.99
false_positive_rate = 0.05

positive_evidence = (sensitivity * prior
                     + false_positive_rate * (1 - prior))
posterior = sensitivity * prior / positive_evidence
print(f'P(Disease | Positive Test) = {posterior:.4f}')
