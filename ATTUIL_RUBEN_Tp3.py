# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:49:40 2019

@author: ATTUIL RUBEN 
@studentid:3672225
@email:ruben-attuil@outlook.fr
"""

import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

N = 12
k = 1
m = 1

# Création de la matrice d'inertie M
M = (2*np.eye(N) - np.eye(N, k=-1) - np.eye(N, k=1))*k/m
print("Matrix M is :")
print(M)

#Affichage des valeurs et vecteurs propres

e_val,e_vec=la.eig(M)
print("Eigenvalues are :")
print(e_val)

print("Eigenvectors are :")
print(e_vec)


time_sample = np.linspace(0,40,100)
W=np.zeros(len(e_val))#creation d'un tableau qui va contenir les pulsations propres
F=np.zeros(len(e_val))#creation d'un tableau qui va contenir les fréquences propres associées
for i in range(len(e_val)):
    w=np.sqrt(e_val[i])
    W[i]=w #remplissage du tableau des pulsations propres
    
for i in range(3):
    #E represente le déplacement de chaque masse ici 3 masses étudiées
    E1=e_vec[0,i]*np.cos(w*time_sample)
    E2=e_vec[1,i]*np.cos(w*time_sample)
    E3=e_vec[2,i]*np.cos(w*time_sample)
    # x représente la position de chaquze masse ici 3 masses étudiées
    x1=1+E1
    x2=2*(1+E2)
    x3=3*(1+E3)
    #tracé des graphes représentant la position de chaque masse en fonction du temps
    plt.figure()
    plt.plot(time_sample,x1, c='b', label='x1')
    plt.plot(time_sample,x2, c='r', label='x2')
    plt.plot(time_sample,x3, c='g', label='x3')
    
    plt.title("mode normal"+ str(i+1))
    plt.xlabel("t")
    plt.ylabel("mouvement de chaque masse")
    plt.legend(loc='upper left')
    
    plt.show()
    plt.savefig('./mode_'+str(i+1)+'.png')


for i in range (len(W)):
    F[i]=W[i]/(2*np.pi)#remplissage du tableau contenant les fréquences propres
mode=[0,1,2,3,4,5,6,7,8,9,10,11]
#Tracé du graphe répresentant les fréquences naturelles en fonction du numero de leur mode
plt.figure()
plt.scatter(mode,F)
plt.title("Natural fresquencies versus mode number")
plt.xlabel("mode number")
plt.ylabel("F")
plt.show()

print("naturals frequencies")
print(F)

