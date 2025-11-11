# -----------------------------------------------
# Gradient Descent to Find Local Minima
# Function: f(x) = (x + 3)^2
# -----------------------------------------------

import matplotlib.pyplot as plt

# Function definition
def func(x):
    return (x + 3) ** 2

# Derivative of the function (gradient)
def grad(x):
    return 2 * (x + 3)

# Parameters for Gradient Descent
x = 2                # Initial guess
learning_rate = 0.1  # Step size (alpha)
epochs = 50          # Number of iterations

# Lists for plotting
x_vals = [x]
y_vals = [func(x)]

# Gradient Descent Loop
print("Iteration\t x\t\t f(x)")
for i in range(epochs):
    dx = grad(x)                        # Compute gradient
    x = x - learning_rate * dx          # Update step
    x_vals.append(x)                    # Store values for plotting
    y_vals.append(func(x))

    print(f"{i+1:3d}\t\t {x:.5f}\t {func(x):.5f}")

# Final result
print(f"\nLocal minimum found near: x = {x:.5f}, f(x) = {func(x):.5f}")


x_plot = [i for i in range(-10, 5)]
y_plot = [func(i) for i in x_plot]

plt.figure(figsize=(8,5))
plt.plot(x_plot, y_plot, label="f(x) = (x + 3)^2", color="blue")
plt.scatter(x_vals, y_vals, color='red', label="Gradient Descent Steps", zorder=5)
plt.plot(x_vals, y_vals, linestyle='--', color='gray', alpha=0.6)
plt.title("Gradient Descent to Find Local Minima", fontsize=14)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()




