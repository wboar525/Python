#Задача 1. Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
#По графику определите, при каких значения x значение функции отрицательно.

import matplotlib.pyplot as mat

x = list(i for i in range(-10,10))
f = list(5*x[i]*x[i] + 10*x[i] - 30 for i in range(len(x)))
mat.ylim(-50,50)
mat.xlabel('x',fontsize=16)
mat.grid(which='major')
mat.plot(f,'r-')
mat.show()
