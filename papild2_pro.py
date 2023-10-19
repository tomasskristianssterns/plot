import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

def f(x, a, v0, g):
   return v0*np.sin(a*np.pi/180)*x - 0.5*g*x**2

id = input("Ievadiet savu studenta apliecības numuru: ")
try:
    id = int(id[len(id)-3:])  # pēdējie 3 cipari no apliecības numura
except:
    print("Nepareizs apliecības numurs!")
    exit()

parametrs = id%100  # pēdējie 2 cipari no apliecības numura, ko izmanto dotai tabulai
saraksts = [ 
             [ 0, 9.81, 'A', 0, 30, 0.05],
             [ 1, 1.62, 'A', 0, 25, 0.1 ],
             [ 2, 3.86, 'A', 0, 30, 0.1 ],
             [ 3, 8.88, 'A', 0, 35, 0.05 ],
             [ 4, 3.72, 'A', 0, 35, 0.1 ],
             [ 5, 10.44, 'A', 0, 35, 0.05 ],
             [ 6, 23.95, 'A', 0, 45, 0.05 ],
             [ 7, 8.86, 'A', 0, 40, 0.05 ],
             [ 8, 11.09, 'A', 0, 45, 0.05 ],
             [ 9, 0.61, 'A', 0, 25, 0.15 ],
             [ 10, 9.81, 'B', 0, 35, 0.05 ],
             [ 11, 1.62, 'B', 0, 25, 0.1 ],
             [ 12, 3.86, 'B', 0, 40, 0.1 ],
             [ 13, 8.88, 'B', 0, 35, 0.05 ],
             [ 14, 3.72, 'B', 0, 35, 0.1 ],
             [ 15, 10.44, 'B', 0, 45, 0.05 ],
             [ 16, 23.95, 'B', 0, 50, 0.05 ],
             [ 17, 8.86, 'B', 0, 40, 0.05 ],
             [ 18, 11.09, 'B', 0, 25, 0.05 ],
             [ 19, 0.61, 'B', 0, 30, 0.2 ],
             [ 20, 9.81, 'C', 0, 50, 0.05 ],
             [ 21, 1.62, 'C', 0, 45, 0.15 ],
             [ 22, 3.86, 'C', 0, 45, 0.1 ],
             [ 23, 8.88, 'C', 0, 45, 0.05 ],
             [ 24, 3.72, 'C', 0, 50, 0.1 ],
             [ 25, 10.44, 'C', 0, 50, 0.05 ],
             [ 26, 23.95, 'C', 0, 50, 0.05 ],
             [ 27, 8.86, 'C', 0, 45, 0.05 ],
             [ 28, 11.09, 'C', 0, 50, 0.05 ],
             [ 29, 0.61, 'C', 0, 45, 0.2 ],
             [ 30, 9.81, 'D', 0, 40, 0.05 ],
             [ 31, 1.62, 'D', 0, 50, 0.15 ],
             [ 32, 3.86, 'D', 0, 40, 0.1 ],
             [ 33, 8.88, 'D', 0, 45, 0.05 ],
             [ 34, 3.72, 'D', 0, 45, 0.1 ],
             [ 35, 10.44, 'D', 0, 45, 0.05 ],
             [ 36, 23.95, 'D', 0, 40, 0.05 ],
             [ 37, 8.86, 'D', 0, 40, 0.05 ],
             [ 38, 11.09, 'D', 0, 50, 0.05 ],
             [ 39, 0.61, 'D', 0, 50, 0.2 ],
             [ 40, 9.81, 'E', 0, 50, 0.05 ],
             [ 41, 1.62, 'E', 0, 45, 0.1 ],
             [ 42, 3.86, 'E', 0, 50, 0.1 ],
             [ 43, 8.88, 'E', 0, 55, 0.05 ],
             [ 44, 3.72, 'E', 0, 50, 0.1 ],
             [ 45, 10.44, 'E', 0, 55, 0.05 ],
             [ 46, 23.95, 'E', 0, 50, 0.05 ],
             [ 47, 8.86, 'E', 0, 45, 0.05 ],
             [ 48, 11.09, 'E', 0, 55, 0.05 ],
             [ 49, 0.61, 'E', 0, 45, 0.15 ],
             [ 50, 9.81, 'A', 11, 0, 0.05 ],
             [ 51, 1.62, 'A', 5, 0, 0.1 ],
             [ 52, 3.86, 'A', 8, 0, 0.1 ],
             [ 53, 8.88, 'A', 10, 0, 0.05 ],
             [ 54, 3.72, 'A', 7, 0, 0.01 ],
             [ 55, 10.44, 'A', 12, 0, 0.05 ],
             [ 56, 23.95, 'A', 17, 0, 0.05 ],
             [ 57, 8.86, 'A', 11, 0, 0.05 ],
             [ 58, 11.09, 'A', 12, 0, 0.05 ],
             [ 59, 0.61, 'A', 3, 0, 0.15 ],
             [ 60, 9.81, 'B', 12, 0, 0.05 ],
             [ 61, 1.62, 'B', 5, 0, 0.1 ],
             [ 62, 3.86, 'B', 7.5, 0, 0.1 ],
             [ 63, 8.88, 'B', 12, 0, 0.05 ],
             [ 64, 3.72, 'B', 7.5, 0, 0.1 ],
             [ 65, 10.44, 'B', 13, 0, 0.05 ],
             [ 66, 23.95, 'B', 20, 0, 0.05 ],
             [ 67, 8.86, 'B', 12, 0, 0.05 ],
             [ 68, 11.09, 'B', 14, 0, 0.05 ],
             [ 69, 0.61, 'B', 3, 0, 0.2 ],
             [ 70, 9.81, 'C', 14, 0, 0.05 ],
             [ 71, 1.62, 'C', 5.5, 0, 0.15 ],
             [ 72, 3.86, 'C', 9, 0, 0.1 ],
             [ 73, 8.88, 'C', 13.5, 0, 0.05 ],
             [ 74, 3.72, 'C', 8.5, 0, 0.1 ],
             [ 75, 10.44, 'C', 15, 0, 0.05 ],
             [ 76, 23.95, 'C', 22, 0, 0.05 ],
             [ 77, 8.86, 'C', 14, 0, 0.05 ],
             [ 78, 11.09, 'C', 15, 0, 0.05 ],
             [ 79, 0.61, 'C', 3.5, 0, 0.2 ],
             [ 80, 9.81, 'D', 16, 0, 0.05 ],
             [ 81, 1.62, 'D', 6, 0, 0.15 ],
             [ 82, 3.86, 'D', 10, 0, 0.1 ],
             [ 83, 8.88, 'D', 14.5, 0, 0.05 ],
             [ 84, 3.72, 'D', 9.5, 0, 0.1 ],
             [ 85, 10.44, 'D', 16, 0, 0.05 ],
             [ 86, 23.95, 'D', 25, 0, 0.05 ],
             [ 87, 8.86, 'D', 15, 0, 0.05 ],
             [ 88, 11.09, 'D', 16, 0, 0.05 ],
             [ 89, 0.61, 'D', 3.7, 0, 0.2 ],
             [ 90, 9.81, 'E', 17, 0, 0.05 ],
             [ 91, 1.62, 'E', 8, 0, 0.1 ],
             [ 92, 3.86, 'E', 11, 0, 0.1 ],
             [ 93, 8.88, 'E', 16, 0, 0.05 ],
             [ 94, 3.72, 'E', 11, 0, 0.1 ],
             [ 95, 10.44, 'E', 17.5, 0, 0.05 ],
             [ 96, 23.95, 'E', 27, 0, 0.05 ],
             [ 97, 8.86, 'E', 19, 0, 0.05 ],
             [ 98, 11.09, 'E', 18, 0, 0.05 ],
             [ 99, 0.61, 'E', 5, 0, 0.15]]

students = saraksts[parametrs] # izvēlas studenta parametrus no tabulas
g = students[1]  # gravitācijas paātrinājums
field = students[2] # laukuma nosaukums
v0 = students[3] # sākotnējais ātrums
a = students[4] # leņķis
step = students[5] # laika solis
x = 0
y = 0
x_gala = 0
t = 0

red = False # vai bumba ir sasniedzis mērķi
green = False # vai bumba ir sasniegusi zaļo zonu

try:
    if v0 == 0:
        v0 = float(input("v0="))
    else:
        a = float(input("a="))
except:
    print("Nepareiza ievade!")
    exit()

fig, ax = plt.subplots()

if field == 'A':
    ax.add_patch(Rectangle((12, -4), 5, 2, color='red'))
    ax.add_patch(Rectangle((0, 0), 10, -4, color='lime'))
    ax.add_patch(Rectangle((0, -4), 23, -2, color='lime'))
elif field == 'B':
    ax.add_patch(Rectangle((17, -7), 3, 5, color='red'))
    ax.add_patch(Rectangle((0, 0), 11, -7, color='lime'))
    ax.add_patch(Rectangle((0, -7), 23, -1, color='lime'))
elif field == 'C':
    ax.add_patch(Rectangle((17, 0), 3, 3, color='red'))
    ax.add_patch(Rectangle((0, 0), 23, -2, color='lime'))
    ax.add_patch(Rectangle((7, 0), 3, 4, color='lime'))
elif field == 'D':
    ax.add_patch(Rectangle((15, 4), 3, 2, color='red'))
    ax.add_patch(Rectangle((10, 0), 13, 4, color='lime'))
    ax.add_patch(Rectangle((0, 0), 23, -2, color='lime'))
elif field == 'E':
    ax.add_patch(Rectangle((14, 8), 3, 2, color='red'))
    ax.add_patch(Rectangle((12, 0), 11, 8, color='lime'))
    ax.add_patch(Rectangle((0, 0), 23, -1, color='lime'))

while (not red and not green and x <= 23):
    t += step
    x = v0 * np.cos(a * np.pi / 180) * t
    y = v0 * np.sin(a * np.pi / 180) * t - g * t * t / 2
    if field == 'A':
        red = x >= 12 and x <= 17 and y >= -4 and y <= -2
        green = (y <= 0 and x <= 10) or (y <= -4 and x >= 10)
    elif field == 'B':
        red = x >= 17 and x <= 20 and y >= -7 and y <= -2
        green = (y <= 0 and x <= 11) or (y <= -7 and x >= 11)
    elif field == 'C':
        red = x >= 17 and x <= 20 and y >= 0 and y <= 3
        green = (y <= 0 and x <= 23) or (y <= 4 and x >= 7 and x <= 10)
    elif field == 'D':
        red = x >= 15 and x <= 18 and y >= 4 and y <= 6
        green = (y <= 0 and x <= 23) or (y <= 4 and x >= 10 and x <= 23)
    elif field == 'E':
        red = x >=14 and x <= 17 and y >= 8 and y <= 10 # mērķa robežas
        green = (y <= 0 and x < 12) or (y <= 8 and x >= 12); # zaļās zonas robežas
    x_gala = t

x = np.linspace(0, x_gala, 50) 
plt.plot(v0*np.cos(a*np.pi/180)*x, f(x, a, v0, g), color='blue')

#display plot
plt.show()