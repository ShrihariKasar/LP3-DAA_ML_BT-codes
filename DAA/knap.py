#fractional knapsack
def fractional_knapsack(profit, weight, capacity):
    n = len(profit)

    # Calculate profit/weight ratio for each item
    ratio = [(profit[i] / weight[i], profit[i], weight[i], i + 1) for i in range(n)]

    # Sort by ratio in descending order
    ratio.sort(reverse=True)

    total_profit = 0
    remaining_capacity = capacity

    print("\nSelected items:")
    for r, p, w, idx in ratio:
        if remaining_capacity == 0:
            break

        if w <= remaining_capacity:
            total_profit += p
            remaining_capacity -= w
            print(f" Take 100% of item {idx} (profit={p}, weight={w})")
        else:
            fraction = remaining_capacity / w
            total_profit += p * fraction
            print(f" Take {fraction * 100:.2f}% of item {idx} (profit={p}, weight={w})")
            remaining_capacity = 0

    return total_profit


# ---------------------------
# 📌 Main: Taking User Inputs
# ---------------------------
n = int(input("Enter number of items: "))
profit = []
weight = []

for i in range(n):
    p = float(input(f"Enter profit of item {i + 1}: "))
    w = float(input(f"Enter weight of item {i + 1}: "))
    profit.append(p)
    weight.append(w)

capacity = float(input("\nEnter maximum capacity of knapsack: "))

# 🧠 Call the function
max_profit = fractional_knapsack(profit, weight, capacity)

print(f"\nMaximum profit = {max_profit:.2f}")

# Enter number of items: 3
# Enter profit of item 1: 60
# Enter weight of item 1: 10
# Enter profit of item 2: 100
# Enter weight of item 2: 20
# Enter profit of item 3: 120
# Enter weight of item 3: 30

# Enter maximum capacity of knapsack: 50
# Selected items:
#  Take 100% of item 1 (profit=60.0, weight=10.0)
#  Take 100% of item 2 (profit=100.0, weight=20.0)
#  Take 66.67% of item 3 (profit=120.0, weight=30.0)

# Maximum profit = 240.0


# ---

# ## 🧾 **Definition:**

# **Fractional Knapsack Problem** is a type of **Greedy Algorithm problem** where we have a **bag (knapsack)** with a limited capacity and a set of **items**, each having a **profit (value)** and a **weight**.

# The aim is to **fill the bag** in such a way that we get the **maximum total profit** possible.
# Unlike the 0/1 Knapsack problem, in the **Fractional Knapsack**, we can take **a fraction (part)** of an item instead of taking it completely.

# ---

# ## 💡 **Simple Explanation:**

# * You have a bag that can hold only a certain weight.
# * You have several items, each with its **weight** and **profit**.
# * You can take **any amount (fraction)** of an item — not just whole items.
# * To get **maximum profit**, always pick items with the **highest profit per weight** ratio first.

# ---

# ## ⚙️ **Example (Simple):**

# Suppose you have:

# | Item | Profit | Weight | Profit/Weight |
# | ---- | ------ | ------ | ------------- |
# | 1    | 60     | 10     | 6.0           |
# | 2    | 100    | 20     | 5.0           |
# | 3    | 120    | 30     | 4.0           |

# Capacity of bag = 50

# So,
# ✅ Take all of Item 1 (10 kg)
# ✅ Take all of Item 2 (20 kg)
# ✅ Take 2/3 of Item 3 (20 kg of 30 kg)

# **Total Profit = 60 + 100 + 80 = 240**

# ---

# ## 🧠 **Key Points:**

# 1. It is a **Greedy algorithm** problem.
# 2. We calculate the **profit-to-weight ratio** for each item.
# 3. Items are arranged in **descending order** of this ratio.
# 4. We pick items with the **highest ratio** until the bag is full.
# 5. We can take **fractions** of items if there is not enough space for the full item.
# 6. This method always gives the **optimal (maximum) profit**.
# 7. The time complexity is **O(n log n)** (due to sorting).

# ---

# ## ✨ **Short Definition to Write in Exam:**

# > The Fractional Knapsack Problem is a **greedy approach** problem in which items are selected based on the **highest profit-to-weight ratio** to fill a bag of limited capacity, allowing **fractions of items** to be taken to **maximize total profit**.