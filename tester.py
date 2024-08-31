import math as math
import matplotlib.pyplot as plt
import random as random

#---PANEL---
pob = [10000]
plants = [3000]
animals = [15]
food = [15]
foodProduced = [0]
weaponsProduced = [0]
woodProduced = [0]
wood = [0]
moneyProduced = [0]
money = [0]
pibpercapita = [0]
days = 1000000
#---Tile---
capacityPlants = 5000
rateGrowPlants = 0.1
plantsConsumed = 0.001
rateGrowAnimals = 0.04
capacityAnimals = 22
animalsMortality = 0.001
#---City---
foodConsumed = 0.003 #food consumed everyday by one person in tons
foodWorkers = 0.8 #Percent of people working on production of food
foodWorkersSalary = 6 #Salary for food workers
efficiencyFood = 0.01 #tons produced by one person in one day
maxFoodProduced = plants[-1] * 1000 #Maximum of plants producible
armyWorkers = 0.05 #Percent of people working on the army
armyWorkersSalary = 9 #Salary for army workers
woodConsumed = 0.01 #wood consumed everyday by one person in tons
lumberjackWorkers = 0.05 #Percent of people working on wood
lumberjackWorkersSalary = 7 #Salary for lumberjacks
efficiencyWood = 0.3 #tons produced by one person in one day
maxWoodProduced = plants[-1] * 100 #Maximum of wood producible
birthRate = 0.0001 #birth rate per person
deathRate = 0.00006 #death rate per person
pobCapacity = 1000000
valueFood = 500
valueWood = 200
tax = 5 #Taxes for each person in one day
pobSpents = 1 #Spent for each person in one day

while days > 0:
    #---Tile.cycle()---
    #print(f"Plants Equation: {plants[-1]} + {rateGrowPlants * plants[-1]} * {1 - plants[-1] / capacityPlants} - {plantsConsumed * animals[-1]}")
    plants.append(math.ceil(max(1, plants[-1] + (rateGrowPlants * plants[-1]) * (1 - plants[-1] / capacityPlants) - (plantsConsumed * animals[-1]) + random.randint(-10, 10))))
    #print(f"Animals Equation: {animals[-1]} + {rateGrowAnimals * animals[-1]} * {1 - animals[-1] / capacityAnimals} * {plants[-1] / capacityPlants} - {animalsMortality * animals[-1]} - {0.01 * animals[-1] / max(0.1, plants[-1])}")
    animals.append(math.ceil(max(1, animals[-1] + (rateGrowAnimals * animals[-1]) * (1 - animals[-1] / capacityAnimals) * (plants[-1] / capacityPlants) - (animalsMortality * animals[-1]) - (0.01 * animals[-1] / max(0.1, plants[-1])) + random.randint(-2, 2))))

    #--City.cycle()---

    #FOOD
    efficiencyFood = 0.01 * (1 - (pob[-1] / pobCapacity))
    #print(f"Food Produced Equation: {pob[-1] * foodWorkers * efficiencyFood} * {min(1, plants[-1] / capacityPlants)}")
    foodProduced.append(min(maxFoodProduced, math.ceil(pob[-1] * foodWorkers * efficiencyFood * min(1, plants[-1] / capacityPlants))))
    #print(f"Food Equation: {food[-1]} + {foodProduced[-1]} - {pob[-1] * foodConsumed} - {food[-1] * 0.05}") 
    food.append(int(food[-1] + foodProduced[-1] - pob[-1] * foodConsumed - food[-1] * 0.05))
    food[-1] = max(0, food[-1])

    #WEAPON
    #print(f"Weapons Equation: {pob[-1] * armyWorkers}")
    weaponsProduced.append(int(pob[-1] * armyWorkers))
    weaponsProduced[-1] = max(0, weaponsProduced[-1])

    #WOOD
    if days <= 20:
        print(f"Wood Equation: {pob[-1] * lumberjackWorkers * efficiencyWood} * {min(1, plants[-1] / capacityPlants)} - {pob[-1] * woodConsumed}")
    woodProduced.append(min(maxWoodProduced, math.ceil(pob[-1] * lumberjackWorkers * efficiencyWood * min(1, plants[-1] / capacityPlants) - pob[-1] * woodConsumed) // 10))
    woodProduced[-1] = max(0, int(woodProduced[-1]))
    wood.append(wood[-1] + woodProduced[-1])

    #UPDATE PLANTS
    #print(f"Plants Update Equation: ({foodProduced[-1]} + {pob[-1] * lumberjackWorkers * efficiencyWood}) * 0.001")
    plants[-1] -= int((foodProduced[-1] + pob[-1] * lumberjackWorkers * efficiencyWood)*0.001)
    plants[-1] = max(0, plants[-1])

    #POB
    #print(f"Pob Equation: {pob[-1]} + {pob[-1] * birthRate} * {min(1, food[-1] / (pob[-1] * foodConsumed))} - {pob[-1] * deathRate}")
    pob.append(math.ceil((pob[-1] + pob[-1] * birthRate * min(1, food[-1] / (pob[-1] * foodConsumed)) - pob[-1] * deathRate)))
    if pob[-1] == 0:
        break

    #MONEY
    if days <= 20:
        print(f"Money Equation: {money[-1]} + {foodProduced[-1] * valueFood} + {woodProduced[-1] * valueWood} + {pob[-1] * tax} - {pob[-1] * foodWorkers * foodWorkersSalary + weaponsProduced[-1] * armyWorkersSalary + pob[-1] * lumberjackWorkers * lumberjackWorkersSalary} - {pob[-1] * pobSpents}")
    moneyProduced.append(int(foodProduced[-1] * valueFood + woodProduced[-1] * valueWood + pob[-1] * tax - pob[-1] * foodWorkers * foodWorkersSalary - weaponsProduced[-1] * armyWorkersSalary - pob[-1] * lumberjackWorkers * lumberjackWorkersSalary - pob[-1] * pobSpents))
    money.append(money[-1] + moneyProduced[-1])
    money[-1] = max(0, money[-1])
    pibpercapita.append(money[-1] / pob[-1])

    days -= 1

fig, axs = plt.subplots(3, 3, figsize=(7, 7))

axs[0, 0].plot(pob)
axs[0, 0].set_title("Pob")

axs[0, 1].plot(plants)
axs[0, 1].plot(animals)
axs[0, 1].set_title("Tile")

axs[1, 0].plot(foodProduced)
axs[1, 0].set_title("Food Produced")

axs[1, 1].plot(food)
axs[1, 1].set_title("Food")

axs[0, 2].plot(woodProduced)
axs[0, 2].set_title("Wood Produced")

axs[1, 2].plot(wood)
axs[1, 2].set_title("Wood")

axs[2, 2].plot(money)
axs[2, 2].set_title("Money")

axs[2, 1].plot(moneyProduced)
axs[2, 1].set_title("Money Produced")

axs[2, 0].plot(pibpercapita)
axs[2, 0].set_title("Pib per Capita")

plt.tight_layout()
plt.show()

- pob[-1] * foodWorkers * foodWorkersSalary - weaponsProduced[-1] * armyWorkersSalary - pob[-1] * lumberjackWorkers * lumberjackWorkersSalary