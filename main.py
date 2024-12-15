import random

items = [
    (2, 3),  # item 1: weight=2, value=3
    (1, 2),  # item 2: weight=1, value=2
    (3, 6),  # item 3: weight=3, value=6
    (2, 3),  # item 4: weight=2, value=3
    (1, 1)   # item 5: weight=1, value=1
]
capacity = 7

# parameters
population_size = 100
number_of_items = len(items)
generations = 3000
PC = 0.8  # Probability of crossover
PM = 0.1  # Probability of mutation


def fitness(individual):
    """Calculate the fitness of an individual.
       Fitness = sum of values if total weight <= capacity, else 0."""
    total_weight = 0
    total_value = 0
    for i, bit in enumerate(individual):
        if bit == 1:
            w, v = items[i]
            total_weight += w
            total_value += v
    if total_weight <= capacity:
        return total_value
    else:
        return 0


def create_individual():
    """Create a random individual (binary list)"""
    return [random.randint(0, 1) for _ in range(number_of_items)]


def initial_population():
    """Generate the initial population."""
    return [create_individual() for _ in range(population_size)]


def roulette_wheel_selection(pop, fitnesses):
    """Select one individual from the population using roulette wheel selection."""
    total_fit = sum(fitnesses)
    if total_fit == 0:
        # If all are zero, choose randomly
        return random.choice(pop)
    pick = random.uniform(0, total_fit)
    current = 0
    for ind, fit in zip(pop, fitnesses):
        current += fit
        if current > pick:
            return ind


def crossover(parent1, parent2):
    """One-point crossover."""
    if random.random() < PC:
        point = random.randint(1, number_of_items-1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return [child1, child2]
    else:
        # No crossover, just clone
        return [parent1[:], parent2[:]]


def mutate(individual):
    """Bit-flip mutation."""
    for i in range(number_of_items):
        if random.random() < PM:
            individual[i] = 1 - individual[i]
    return individual


def main():
    # Initialize population
    population = initial_population()

    for gen in range(generations):
        # Evaluate fitness
        fitnesses = [fitness(ind) for ind in population]

        # Track best solution in this generation
        best_fit = max(fitnesses)
        best_ind = population[fitnesses.index(best_fit)]

        print(
            f"Generation {gen} | Best Fitness: {best_fit} | Best Individual: {best_ind}")

        # Create next generation
        new_population = []
        # We'll create pairs and produce children until we have population_size members
        while len(new_population) < population_size:
            # Select parents
            parent1 = roulette_wheel_selection(population, fitnesses)
            parent2 = roulette_wheel_selection(population, fitnesses)

            # Crossover
            children = crossover(parent1, parent2)

            # Mutate children
            for c in children:
                c = mutate(c)
                new_population.append(c)
                if len(new_population) == population_size:
                    break

        population = new_population

    # Final evaluation
    final_fitnesses = [fitness(ind) for ind in population]
    best_fit = max(final_fitnesses)
    best_ind = population[final_fitnesses.index(best_fit)]
    print("=== Final Result ===")
    print(f"Best Fitness: {best_fit}")
    print(f"Best Individual: {best_ind}")

    # Show chosen items
    chosen_items = [items[i] for i, bit in enumerate(best_ind) if bit == 1]
    print("Chosen items (weight, value):", chosen_items)
    total_weight = sum(w for w, v in chosen_items)
    total_value = sum(v for w, v in chosen_items)
    print(f"Total weight: {total_weight}, Total value: {total_value}")


if __name__ == "__main__":
    main()
