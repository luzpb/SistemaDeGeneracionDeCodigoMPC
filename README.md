# Sistema de generación de código para la implementación de algoritmos de control predictivos en sistema embebidos de tiempo real

La implementación exitosa de algoritmos de control predictivo en sistemas embebidos requiere una etapa crucial: la generación de código eficiente y específico para la plataforma. Este proceso se logra mediante el empleo de un generador de código automático, cuyo papel es transformar la lógica de alto nivel en código ejecutable, adaptado a las particularidades del sistema embebido.

El generador de código presentado en el anexo se ha diseñado con el propósito de facilitar esta transformación. Este código base utiliza la biblioteca "jinja2" y opera mediante una serie de interacciones con el usuario para determinar aspectos clave del proceso de generación de código, como el lenguaje de destino (Python o MicroPython) y el tipo de problema (QP o MPC).

El generador de código hace uso de un archivo llamado "Datos" que contiene los parámetros y variables necesarios para la implementación de los algoritmos de control predictivo. La importación de este archivo mediante la instrucción [ import Datos] asegura que los valores relevantes sean fácilmente accesibles durante la generación del código.

En el contexto del lenguaje de destino, el generador de código proporciona la opción de seleccionar entre diferentes librerías relevantes para el control predictivo, como "cvxpy" y "pyomo", según sea necesario. La interacción con el usuario permite configurar detalles específicos, como la presencia de restricciones y la elección de plantillas correspondientes.
7.1 Problemas que aborda el sistema codificador

# Clasificación de Problemas de Programación Cuadrática
Los problemas de programación cuadrática abarcan diversos escenarios en función de las restricciones que los caracterizan. A continuación, se detallan los distintos tipos de problemas de programación cuadrática y sus características:
1.	*Problemas Cuadráticos de Minimización sin Restricciones*: En esta categoría, se busca minimizar una función cuadrática en todo el espacio de variables posibles. No existen restricciones adicionales que limiten las variables de decisión.
2.	*Problemas Cuadráticos de Minimización Sujetos a Restricciones de Igualdad*: Estos problemas involucran la minimización de la función objetivo bajo restricciones lineales de igualdad. Es decir, se persigue el mínimo valor de la función cuadrática considerando las ecuaciones lineales que las variables de decisión deben cumplir.
3.*Problemas Cuadráticos de Minimización Sujetos a Restricciones Lineales de Desigualdad*: Aquí, el objetivo es minimizar la función objetivo sujetándola a restricciones lineales de desigualdad. Estas restricciones establecen límites o rangos permitidos para las variables de decisión.
4.	*Problemas Cuadráticos de Minimización Sujetos a Restricciones de Igualdad y Restricciones Lineales de Desigualdad*: Esta categoría combina restricciones de igualdad y restricciones lineales de desigualdad. El propósito es minimizar la función cuadrática considerando estas restricciones mixtas.
Cada tipo de problema de programación cuadrática presenta retos específicos y requiere enfoques de resolución adecuados. Un análisis detenido de las restricciones y la función objetivo facilita la selección de la formulación más idónea para afrontar el problema en cuestión. La comprensión de estas categorías provee una base sólida para desarrollar soluciones óptimas y eficientes en diversos dominios de aplicación.

# Clasificación de Problemas de MPC
El control predictivo Model Predictive Control (MPC) se subdivide en diferentes tipos según su objetivo. A continuación, se describen los dos tipos principales de controladores de MPC:
1.	*Controlador MPC de Regulación*: Este enfoque tiene como objetivo principal mantener el sistema en un estado deseado y estable a lo largo del tiempo. El controlador calcula las acciones de control de manera que las variables de estado converjan hacia valores específicos, logrando así la regulación precisa del sistema.
2.	*Controlador MPC de Tracking*: En este caso, el controlador busca seguir una trayectoria o referencia predefinida en las variables de estado. El objetivo es que el sistema emulado siga una evolución deseada, adaptándose a cambios en la referencia mientras mantiene el sistema dentro de límites predefinidos.


