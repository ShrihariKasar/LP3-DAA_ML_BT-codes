# fibonacci

# Program to print Fibonacci series and show step count

def fibonacci_series(n):
    a, b = 0, 1
    steps = 0  # Step counter
    series = []

    for i in range(n):
        series.append(a)
        a, b = b, a + b
        steps += 1  # Count each loop iteration as one step

    return series, steps


# --- Main Program ---
n = int(input("Enter how many terms you want: "))

fib_series, step_count = fibonacci_series(n)

print("\nFibonacci Series:")
for num in fib_series:
    print(num, end=" ")

print(f"\n\nTotal Steps Taken: {step_count}") 


# ###
# ## 🧾 **Definition:**

# The **Fibonacci Series** is a sequence of numbers where each number is the **sum of the two numbers before it**.
# The series starts with **0 and 1**, and continues infinitely.

# The general form is:

# > 0, 1, 1, 2, 3, 5, 8, 13, 21, …

# In this program, we also count the **number of steps (iterations)** taken by the loop to generate the series.

# ---

# ## 💡 **Explanation:**

# 1. The program starts with two numbers → `a = 0`, `b = 1`.
# 2. It runs a loop for `n` terms (as given by the user).
# 3. In each loop:

#    * The current number `a` is added to the Fibonacci series list.
#    * The next number is calculated as `a + b`.
#    * The variables are updated for the next term.
#    * The **step counter** increases by 1 in each loop.
# 4. Finally, it prints all Fibonacci numbers and shows how many **steps** were taken.

# ---

# ## 🧮 **Example:**

# If user input is:

# ```
# Enter how many terms you want: 7
# ```

# Then the output is:

# ```
# Fibonacci Series:
# 0 1 1 2 3 5 8 

# Total Steps Taken: 7
# ```

# ---

# ## 🧠 **Key Points:**

# 1. **Definition:** Fibonacci series is a sequence where each term is the sum of the previous two terms.
# 2. **First two terms:** 0 and 1.
# 3. **Formula:**

#    ```
#    F(n) = F(n-1) + F(n-2)
#    ```
# 4. **Iterative method:** Uses a `for` loop to calculate terms.
# 5. **Step count:**

#    * It tells how many times the loop runs.
#    * For `n` terms, total steps = `n`.
# 6. **Time complexity:** O(n) — because the loop runs `n` times.
# 7. **Type of program:** Iterative (not recursive).
# 8. **Applications:** Used in algorithms, computer graphics, and mathematical analysis.

# ---

# ## ✨ **Simple Definition to Write in Exam:**

# > The Fibonacci Series is a sequence of numbers where each term is the sum of the two preceding ones, starting from 0 and 1.
# > In this program, we generate the Fibonacci series up to ‘n’ terms and count the total number of steps (loop iterations) taken.
# ##