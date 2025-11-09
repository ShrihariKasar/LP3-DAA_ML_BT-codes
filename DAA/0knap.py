# 0-1 Knapsack (DP, bottom-up, 1-D space) with user input

def knapsack_dp(weights, values, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)
    # To reconstruct chosen items, track picks per capacity
    choose = [[False]* (capacity + 1) for _ in range(n)]

    for i in range(n):
        w, v = weights[i], values[i]
        # iterate backward to respect 0-1 constraint
        for cap in range(capacity, w - 1, -1):
            if dp[cap - w] + v > dp[cap]:
                dp[cap] = dp[cap - w] + v
                choose[i][cap] = True

    # Reconstruct items picked
    picked = []
    cap = capacity
    for i in range(n - 1, -1, -1):
        if choose[i][cap]:
            picked.append(i)
            cap -= weights[i]
    picked.reverse()
    return dp[capacity], picked

# ---- User input ----
if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    weights, values = [], []
    for i in range(n):
        values.append(int(input(f"Value of item {i+1}: ")))
        weights.append(int(input(f"Weight of item {i+1}: ")))
    capacity = int(input("Enter knapsack capacity: "))

    best_value, picked = knapsack_dp(weights, values, capacity)

    print(f"\nMaximum value = {best_value}")
    print("Items taken (1-based index):", [i+1 for i in picked])
    print("Total weight:", sum(weights[i] for i in picked))

    

# ## 🧾 **Definition:**

# **0/1 Knapsack Problem** is a popular **Dynamic Programming problem** in which we have a **bag (knapsack)** that can carry a **limited weight**, and we have **n items** — each with a **value (profit)** and **weight**.

# The aim is to **select a set of items** to put into the knapsack so that:
# ✅ The **total value (profit)** is **maximum**, and
# ✅ The **total weight** does **not exceed** the given capacity.

# In the **0/1 version**, each item can be taken **only once** — either **included (1)** or **not included (0)**.
# That’s why it is called the **0/1 Knapsack Problem**.

# ---

# ## 💡 **Simple Example:**

# Suppose we have:

# | Item | Value | Weight |
# | ---- | ----- | ------ |
# | 1    | 60    | 10     |
# | 2    | 100   | 20     |
# | 3    | 120   | 30     |

# Capacity of bag = 50

# If we take Item 2 and Item 3 →
# Total weight = 20 + 30 = 50
# Total value = 100 + 120 = **220** (maximum possible)

# So, the **optimal solution** is to take **items 2 and 3**.

# ---

# ## 🧠 **Key Points / Important Notes:**

# 1. **Type:** Dynamic Programming problem.
# 2. **Decision:** Each item can be taken (1) or not taken (0).
# 3. **Goal:** Maximize total profit while staying within weight capacity.
# 4. **Input:**

#    * List of item values (profits)
#    * List of item weights
#    * Knapsack capacity
# 5. **Output:**

#    * Maximum total profit
#    * Items that give this profit
# 6. **Approach:**

#    * Build a DP table to store results of subproblems.
#    * Use previous results to avoid recalculation.
# 7. **Time Complexity:** O(n × W)
#    (n = number of items, W = capacity of knapsack)
# 8. **Space Complexity:** O(W) in optimized version (1D DP array).
# 9. **Difference from Fractional Knapsack:**

#    * **0/1 Knapsack:** Items cannot be broken (whole only).
#    * **Fractional Knapsack:** Items can be taken in parts.

# ---

# ## 🪶 **Simple Definition to Write in Exam:**

# > The **0/1 Knapsack Problem** is a dynamic programming problem where each item can either be included or excluded from the knapsack.
# > The objective is to **maximize the total profit/value** without exceeding the **maximum capacity** of the knapsack.