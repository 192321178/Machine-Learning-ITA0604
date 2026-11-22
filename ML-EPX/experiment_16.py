from itertools import product

P_RAIN = 0.20
P_SPRINKLER = 0.40

# P(Wet=True | Rain, Sprinkler)
p_wet = {
    (True, True): 0.99,
    (True, False): 0.90,
    (False, True): 0.90,
    (False, False): 0.01,
}

joint_wet = []
for rain, sprinkler in product([False, True], repeat=2):
    p_rain = P_RAIN if rain else 1 - P_RAIN
    p_sprinkler = P_SPRINKLER if sprinkler else 1 - P_SPRINKLER
    joint = p_rain * p_sprinkler * p_wet[(rain, sprinkler)]
    joint_wet.append((rain, joint))

p_wet_total = sum(probability for _, probability in joint_wet)
p_rain_and_wet = sum(probability for rain, probability in joint_wet if rain)
posterior = p_rain_and_wet / p_wet_total
print(f'P(Rain=True | Wet=True) = {posterior:.4f}')
