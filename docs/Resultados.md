# Planeamiento  y Resultados 

En esta sección se mostraran el planteamiento y los resultados obtenidos de MODELO DE TIGHT BINDING DE OCUPACIÓN SIMPLE CON POTENCIAL DEFINIDO: DINÁMICA.    


## Las dos metodologías que son mejores para implementar la solución numérica.

####  Formal a la ecuación de schrodinger


> **Nota:** La idea del método RK2 es utilizar el punto medio para evaluar el método de Euler.

#### Método de Runge-Kutta 4 Orden (RK4)
> **Nota:** Mejor compromiso entre complejidad y error de aproximación. Este método es el más utilizado comúnmente para resolver ODEs.

## Visualizar su dinámica
###### Probabilidad de encontrar el fermion en una evolución cuántica temporal dentro de una grilla unidimensional.


simulación de la evolución temporal de un sistema cuántico utilizando el método de Runge-Kutta de cuarto orden

![Animación1](1.gif)

> En la animación, observamos cómo la densidad de probabilidad cambia con el tiempo. Además, cómo un fermión puede propagarse a través de la grilla, esto es mostrado por la dispersión de la función de onda. 

![Animación2](gif2.gif)

## Paralelización 
En el gráfico presentado a continuación, observamos cómo la paralelización debería acelerar el proceso de ejecución, ya que el código se divide en múltiples tareas. Sin embargo, en este caso particular, la versión paralelizada fue más lenta. Esto puede deberse a varios factores, como sobrecarga de procesos, problemas de sincronización, o limitaciones de recursos en la computadora.    
<div>
<img src="paralelizacion.jpeg"/>
</div>
