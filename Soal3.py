import numpy as np
import matplotlib.pyplot as plt

# Fungsi performa aerodinamis
def P(x1, x2):
    return - (x1 - 10) ** 2 - (x2 - 5) ** 2 + 50

# Fungsi untuk menghitung gradient dari P
def gradient(x1, x2):
    dP_dx1 = -2 * (x1 - 10)
    dP_dx2 = -2 * (x2 - 5)
    return np.array([dP_dx1, dP_dx2])

# Parameter Gradient Descent
learning_rate = 0.1
x1, x2 = 8, 4  # Tebakan awal
tolerance = 0.001
max_iterations = 1000

# Menyimpan jalur iterasi untuk plotting
x1_values = [x1]
x2_values = [x2]
P_values = [P(x1, x2)]

# Algoritma Gradient Descent
for iteration in range(max_iterations):
    grad = gradient(x1, x2)
    x1_new = x1 - learning_rate * grad[0]
    x2_new = x2 - learning_rate * grad[1]

    # Simpan nilai-nilai untuk plotting
    x1_values.append(x1_new)
    x2_values.append(x2_new)
    P_values.append(P(x1_new, x2_new))

    # Mengecek konvergensi
    if np.linalg.norm([x1_new - x1, x2_new - x2]) < tolerance:
        break

    x1, x2 = x1_new, x2_new

# Hasil optimal
optimal_x1, optimal_x2, max_performance = x1, x2, P(x1, x2)

print(f"Nilai optimal x1 (panjang sayap): {optimal_x1}")
print(f"Nilai optimal x2 (sudut serang): {optimal_x2}")
print(f"Performa maksimum: {max_performance}")

# Visualisasi hasil
x1_range = np.linspace(0, 20, 100)
x2_range = np.linspace(0, 10, 100)
X1, X2 = np.meshgrid(x1_range, x2_range)
Z = P(X1, X2)

# Plot kontur performa dan jalur Gradient Descent
plt.figure(figsize=(10, 6))
contour = plt.contour(X1, X2, Z, levels=50, cmap='viridis')
plt.clabel(contour, inline=True, fontsize=8)
plt.plot(x1_values, x2_values, 'ro-', label="Jalur Gradient Descent")
plt.scatter([optimal_x1], [optimal_x2], color='blue', label=f"Optimal: ({optimal_x1:.2f}, {optimal_x2:.2f})", zorder=5)
plt.title("Optimasi Performa Pesawat dengan Gradient Descent")
plt.xlabel("Panjang Sayap (x1)")
plt.ylabel("Sudut Serang (x2)")
plt.colorbar(contour)
plt.legend()
plt.show()