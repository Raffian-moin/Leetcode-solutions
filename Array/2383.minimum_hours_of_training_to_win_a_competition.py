initialEnergy = 5
initialExperience = 3
energy = [1,4,3,2]
experience = [2,6,3,1]

extraEnergy = max((sum(energy) + 1 - initialEnergy), 0)

prefixSum = initialExperience
extraExperience = 0

for i in range(len(experience)):
    extraExperience = max(extraExperience, ((experience[i] + 1) - prefixSum))
    prefixSum += experience[i]

print(extraEnergy + extraExperience)