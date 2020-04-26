# AI-Art
Reproducing given image using Genetic Algorithm

## Introduction
In this assignment I use genetic algorithm for testing how good evolution theory is in art field. My program tries to reproduce the piece of art and gets something new, beautiful and awesome. This report briefly describes the work and ideas that were applied in the program.

## What is the representation in your algorithm? 
I decompose my future image into square blocks, and the algorithm tries to choose the most appropriate color for that square block in the sense to maximize a fitness score. So, my individual in the algorithm is an inscribed circle into the square block of some color. It is represented as an array of 3 real-valued numbers in range [0, 255], what is exactly description of color in RGB. As a result, the algorithm composes up all those best individuals, so that there is new piece of art. 

## What is the fitness function?
Mean values on each color channel over the square block of the source image are calculated. Then score(3d distance squared) is calculated between chromosome and mean values. The overall fitness score is calculated as ![equation](https://bit.ly/3cJQafi). As a result, we get value between 0 and 1. The closer value to 1, the more appropriate color for future image is selected.

## Which selection mechanism is being used?
Chromosomes with higher fitness score have higher probability to be chosen for next generation. For selection mechanism roulette wheel was picked. 
### Algorithm:
1. We need to calculate total fitness score of population as sum of all fitness scores: ![equation](https://bit.ly/2xOYdsJ), where n is the number of individuals in population, fitness(i) is fitness score of i-th chromosome in population.
2. We need to calculate probability of each chromosome to be selected in new generation: ![equation](https://bit.ly/358O9XO), where i in [0,n].
3. Cumulative probability is need to be calculated: ![equation](https://bit.ly/2VDD6T5), where i in [0,n].
4. Now for applying roulette wheel technique we need to generate random real value for each chromosome: R(i) in [0,1], where i in [0,n].
5. Then we need to determine which section of cumulative probability function includes R(i), and take corresponding chromosome.

## Explain the crossover function.
In my script the number of mate chromosomes is controlled by CROSSOVER_RATE constant, which is equal to 30%.  Mate chromosomes are chosen randomly. For implementing crossover function one-cut point technique is used. In this technique we need randomly chose the position in parent chromosome and exchange all genes of another parent chromosome from that position.

## Explain mutation criteria.
The number of mutations done in chromosome is controlled by MUTATION_RATE constant, which is equal to 50%. This probability is so high, because of the complex RGB scheme production of color. It is really hard to estimate one channel of color, because we have fitness function calculating score over 3 channels. As a result, it’s more efficient to mutate random gene in hope to pick more appropriate color. It works well actually.

## Which image manipulation techniques have you applied?
My algorithm adds padding by reflecting borders to make the image divisible by square blocks with side equal to GRID_SIZE in px.

## What is art for you/How would you define art/What is your perception of art? 
Mathematics is present in every aspect of our life, and especially in art. For me, art is the creation of something new based on a mathematical model. We can see mathematics in most of art creations, such as music, painting, architecture, dance and others. It is the nature of people to like mathematical shapes, dependencies, graphs. Actually, even our body constructed using golden ratio. Also according to Marcus du Sautoy, mathematical ideas are in each piece of art, but they are created by authors unconsciously. As a result, art is all about mathematical models.

## Describe the artistic aspect of your output images/Why do you consider the output image as a piece of art?
My generated image consists of small absolutely identical circles in sense of size, that form groups and achieve maximum similarity with the original image, which is also art object. My output images are pieces of art because all that circles(shapes from geometry again) compose up really nice pictures. Important to mention that all generated pictures were enjoyed by most of my friends, so “output image produced by my algorithm is a piece of art” is an objective opinion in some sense. In addition, there is some similar art in the world known as diamond painting. So, if diamond painting is considered by people over the world to be an art, then generated images are also an art, but need less time for creation. 
