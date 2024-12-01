def initialize_system(N):
    h = [0] * (N + 1)
    h[0] = 10
    h[N] = 5
    return h

def create_linear_system(N, h):
    A = [[0] * (N - 1) for _ in range(N - 1)]
    b = [0] * (N - 1)

    for i in range(1, N):
        A[i - 1][i - 1] = -2
        b[i - 1] = -h[i - 1] + h[i + 1]

    for i in range(1, N - 1):
        A[i][i - 1] = 1
        A[i - 1][i] = 1

    return A, b

def solve_newton_raphson(N, h, tolerance=1e-6, max_iterations=1000):
    iteration = 0
    while iteration < max_iterations:
        A, b = create_linear_system(N, h)
        delta_h = [0] * (N - 1)

        for i in range(N - 1):
            delta_h[i] = b[i]
            for j in range(N - 1):
                delta_h[i] -= A[i][j] * h[j + 1]

        for i in range(1, N):
            h[i] += delta_h[i - 1]

        if max(map(abs, delta_h)) < tolerance:
            break

        iteration += 1
    return h

def solve_tdma(N, h):
    A, b = create_linear_system(N, h)
    c = [0] * (N - 1)
    d = [0] * (N - 1)
    c[0] = A[0][1] / A[0][0]
    d[0] = b[0] / A[0][0]

    for i in range(1, N - 1):
        c[i] = A[i][i + 1] / (A[i][i] - A[i][i - 1] * c[i - 1])
        d[i] = (b[i] - A[i][i - 1] * d[i - 1]) / (A[i][i] - A[i][i - 1] * c[i - 1])

    h[N - 1] = d[N - 2]
    for i in range(N - 2, 0, -1):
        h[i] = d[i - 1] - c[i - 1] * h[i + 1]

    return h

def solve_gauss_seidel(N, h, tolerance=1e-6, max_iterations=1000):
    iteration = 0
    while iteration < max_iterations:
        max_diff = 0
        for i in range(1, N):
            prev_h = h[i]
            h[i] = (h[i - 1] + h[i + 1]) / 2
            diff = abs(h[i] - prev_h)
            if diff > max_diff:
                max_diff = diff

        if max_diff < tolerance:
            break

        iteration += 1
    return h

# Main program
N = int(input("Enter the value of N: "))
h = initialize_system(N)

print("Choose the algorithm:")
print("1. Newton-Raphson")
print("2. TDMA (Thomas Algorithm)")
print("3. Gauss-Seidel")
choice = int(input())

if choice == 1:
    h = solve_newton_raphson(N, h)
elif choice == 2:
    h = solve_tdma(N, h)
elif choice == 3:
    h = solve_gauss_seidel(N, h)
else:
    print("Invalid choice!")

print("Solution:")
print(h)
