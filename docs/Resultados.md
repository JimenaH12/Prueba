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
> En la presente animación se se grafíca la norma del operador de destrucción al cuadrado vs el sitio de la grilla i. Para el modelo que trabajamos que fue el tight binding esta gráfica estaría dándonos la estructura de las bandas electrónicas del material. Los picos de la gráfica nos indican un nivel de energía que si está permitido para las partículas en la red. Mientras que los puntos más bajos o mínimos locales en la curva de la gráfica nos indican que hay presencia de bandas prohibidas en el material, es decir donde no hay niveles de energía permitidos. Los cambios abruptos en la gráfica nos podrían indicar transiciones de fase, es decir, donde la estructura de bandas electrónicas cambia significativamente debido a que ocurre variación en ciertos parámetros. Esta animación fue esencial para caracterizar la estructura electrónica de un material en el modelo de tight binding, ya que nos da una representación visual de cómo se distribuyen los estados electrónicos a lo largo de la red.

## Paralelización 
En el gráfico presentado a continuación, observamos cómo la paralelización debería acelerar el proceso de ejecución, ya que el código se divide en múltiples tareas. Sin embargo, en este caso particular, la versión paralelizada fue más lenta. Esto puede deberse a varios factores, como sobrecarga de procesos, problemas de sincronización, o limitaciones de recursos en la computadora.    
<div>
<img src="paralelizacion.jpeg"/>
</div>
