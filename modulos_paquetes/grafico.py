from matplotlib import pyplot as plt
import numpy as np
# preparando datos
x = np.linspace(0,10,100) 
# Graficando los datos
plt.plot(x,x, label = "Linea recta")
# Agregando leyenda
plt.legend()
# Despliega gráfico
plt.show()


# Histograma
grafico = plt.figure(figsize=(10,10))
eje1 = grafico.add_subplot(121)
eje2 = grafico.add_subplot(122)

eje1.bar([1,2,3],[4,5,6])
eje2.barh([4,6,8],[1,2,3])
plt.show()

# https://matplotlib.org/stable/gallery/index.html