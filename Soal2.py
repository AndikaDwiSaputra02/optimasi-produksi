import numpy as np
import matplotlib.pyplot as plt

# Definisikan fungsi dan turunannya
def CL(AR):
    return (2 * np.pi * AR) / (1 + 2 / AR)

def dCL_dAR(AR):
    return (2 * np.pi * (1 + 2 / AR) - (2 * np.pi * AR * (-2 / AR**2))) / (1 + 2 / AR)**2

# Metode Newton-Raphson
def newton_raphson(initial_guess, tolerance):
    AR = initial_guess
    error = float('inf')
    iterations = []
    iter_count = 0
    
    while error > tolerance:
        next_AR = AR - CL(AR) / dCL_dAR(AR)
        error = abs(next_AR - AR)
        AR = next_AR
        iterations.append(AR)
        iter_count += 1
        print(f"Iteration {iter_count}: AR = {AR:.5f}, Error = {error:.5f}")
        
    return AR, iterations

# Inisialisasi parameter
initial_guess = 5
tolerance = 0.001

# Panggil metode Newton-Raphson
optimal_AR, iterations = newton_raphson(initial_guess, tolerance)

# Cetak hasil optimal AR
print(f"\nOptimal Aspect Ratio (AR) = {optimal_AR:.5f}")

# Mempersiapkan plot
AR_values = np.linspace(1, 10, 100)
CL_values = CL(AR_values)

# Plot grafik
plt.figure(figsize=(10, 6))
plt.plot(AR_values, CL_values, label='Koefisien Gaya Angkat (C_L)', color='blue')
plt.axvline(optimal_AR, color='red', linestyle='--', label=f'Optimal AR = {optimal_AR:.3f}')
plt.title('Koefisien Gaya Angkat vs Rasio Aspek Sayap (AR)')
plt.xlabel('Rasio Aspek Sayap (AR)')
plt.ylabel('Koefisien Gaya Angkat (C_L)')
plt.legend()
plt.grid()
plt.show()

optimal_AR
