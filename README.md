# Solve knapsack with GA

**Course**: Computational Intelligence
**Homework**: #3
**Problem**: #4

## Overview

This repository contains a Python implementation of a Genetic Algorithm (GA) to solve the 0/1 Knapsack problem. The code corresponds to Problem 4 of the third homework for the Computational Intelligence course.

## What is the 0/1 Knapsack Problem?

The 0/1 Knapsack problem is a classic optimization challenge. You have a set of items, each with a weight and a value. The goal is to select a subset of these items to maximize the total value without exceeding the capacity constraint. In the 0/1 version, you cannot choose fractional amounts of an item—each item is either taken whole or not taken at all.

## Why Use a Genetic Algorithm?

A Genetic Algorithm is a type of evolutionary algorithm inspired by the process of natural selection. It works well for NP-hard problems like the Knapsack problem, where traditional exhaustive or exact methods may be too slow for large instances. GAs employ a population of candidate solutions, recombining and mutating them to explore the search space, aiming to converge to a high-quality solution over a number of generations.

## Code Structure

- items: A predefined list of (weight, value) tuples.
- capacity: The maximum carrying capacity for the knapsack.
- Genetic Algorithm Parameters:
     - POP_SIZE: The number of candidate solutions in the population.
     - GENERATIONS: The number of iterations (generations) the GA will run.
     - PC: The probability of performing crossover between two parents.
     - PM: The probability of mutating each gene (bit) in an offspring.
- Key Functions

     - fitness(individual):
       Calculates the total value of the items selected by the individual. If the total weight exceeds capacity, the fitness is zero. Otherwise, the fitness equals the sum of the selected items’ values.

     - initial_population():
       Generates a random initial population of binary strings, each representing a subset of items.

     - roulette_wheel_selection(pop, fitnesses):
       Implements Roulette Wheel selection, choosing individuals probabilistically based on their relative fitness.

     - crossover(parent1, parent2):
       Performs one-point crossover to generate new offspring. With probability PC, a random cut point is chosen and genetic material is swapped between parents.

     - mutate(individual):
       With probability PM, flips each bit of the individual (0→1 or 1→0), introducing new genetic variations.

## Running the Code

To run the code, simply execute:

```bash
Copy code
python main.py
```

This will:

- Generate an initial random population.
- Evaluate their fitness.
- Repeatedly perform selection, crossover, and mutation.
- Print the best solution found per generation.
- After the final generation, print the best solution and its details.

### Example Output

During execution, you might see output like:

```bash
Generation 28 | Best Fitness: 12 | Best Individual: [1, 0, 1, 1, 0]
Generation 29 | Best Fitness: 12 | Best Individual: [0, 1, 1, 1, 1]
=== Final Result ===
Best Fitness: 12
Best Individual: [0, 1, 1, 1, 1]
Chosen items (weight, value): [(1, 2), (3, 6), (2, 3), (1, 1)]
Total weight: 7, Total value: 12
```
