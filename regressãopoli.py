import random
import math
import matplotlib.pyplot as plt

lista = [(x, 3*x**2 - 2*x + 10 + random.uniform(-30, 30)) for x in [random.uniform(-10, 10) for _ in range(50)]]

def grad(a, b, c):
    grada = sum([-2 * (lista[i][1] - a * lista[i][0]**2 - b * lista[i][0] - c) * (lista[i][0]**2) for i in range(len(lista))])
    gradb = sum([-2 * (lista[i][1] - a * lista[i][0]**2 - b * lista[i][0] - c) * (lista[i][0]) for i in range(len(lista))])
    gradc = sum([-2 * (lista[i][1] - a * lista[i][0]**2 - b * lista[i][0] - c) for i in range(len(lista))])

    return [grada, gradb, gradc]

def dist(anterior, novo):
    zs = zip(anterior, novo)
    acc = 0
    for [p1, p2] in zs:
        acc += (p1 - p2)**2

    return math.sqrt(acc)

def grad_desc(lr, xa, xb, xc, tol):
    d = 99999
    xa1, xb1, xc1 = 1e10, 1e10, 1e10
    k = 0
    max_iter = 1000000  # evitar loop infinito
    while d > tol:
        grads = grad(xa, xb, xc)
        xa1 = xa - lr * grads[0]
        xb1 = xb - lr * grads[1]
        xc1 = xc - lr * grads[2]

        # ver se deu overflow
        if math.isinf(xa1) or math.isinf(xb1) or math.isinf(xc1):
            print("deuoverflowkkkk.")
            break

        d = dist([xa, xb, xc], [xa1, xb1, xc1])
        xa, xb, xc = xa1, xb1, xc1
        k += 1

    return [xa1, xb1, xc1, k]

# ajuste de parametros
z = grad_desc(1e-6, 4, 1, 1, 1e-6)
print(z)

# plotar os pontos e a curva
x = [lista[i][0] for i in range(len(lista))]
y = [lista[i][1] for i in range(len(lista))]

x1 = sorted([random.uniform(-10, 10) for _ in range(100)])  # pontos da curva
y1 = [z[0]*xx**2 + z[1]*xx + z[2] for xx in x1]
plt.scatter(x, y)
plt.plot(x1, y1, color='red')
plt.show()

