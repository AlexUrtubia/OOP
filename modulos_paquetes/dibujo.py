# Realizar un dibujo indicando las coordenadas
from turtle import *
setup(400, 200, 0, 0)

# Definir tamaño de la pantalla
screensize()
color(243)
goto(100,80)
dot(10,255,0,0)
goto(100,-50)
dot(10,0,255,0)


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

# https://www.mclibre.org/consultar/python/lecciones/python-turtle-1.html
