import random
print(random.randint(5, 10))        # Line 1

# Question: What did you see on line 1?
# Answer: Numbers between (and including) 5 and 10

# Question: What was the smallest number you could have seen, what was the largest?
# Answer: The smallest would be 5 and the largest would be 10.

print(random.randrange(3, 10, 2))   # line 2

# Question: What did you see on line 2?
# Answer: The output randomly switched between 3, 5, 7 and 9.

# Question: What was the smallest number you could have seen, what was the largest?
# Answer: 3 and 9.

# Question: Could line 2 have produced a 4?
# Answer: No

print(random.uniform(2.5, 5.5))     # line 3

# Question: What did you see on line 3?
# Answer: A random number between 2.5 and 5.5 with 15 decimal places

# Question: What was the smallest number you could have seen, what was the largest?
# Answer: 2.5 and 5.5

print(random.uniform(1, 100.000000000000001))
# ^ Not too sure about this....