#b
import numpy as np
#a

def acceleration(v, x, k, c):
    a = -k*x -c*v
    return a

#b

def euler_step(x_old,v_old,dt,k, c):
    v_new = v_old + acceleration(v_old, x_old, k, c)*dt
    x_new = x_old + v_old*dt
    return x_new, v_new


def euler(k=1,c=0,x0=0,v0=1,dt=.01,t_0=0,t_max=10):
        ts = np.arange(t_0, t_max, dt)
        xs = np.zeros([len(ts)])
        ys = np.ones([len(ts)])
        
        for i in range(len(ts)-1):
            xs[i+1], ys[i+1] = euler_step(xs[i], ys[i], dt=.01, k=1, c=0)
        return ts, xs, ys


import matplotlib.pyplot as plt

ts, ys, xs = euler(k=10,c=0.1,x0=0,v0=1,dt=.01,t_0=0,t_max=10)

fig = plt.figure(1)
plt.subplot(211)
plt.title('Position en fonction du temps')
plt.plot(ts, xs, 'r', label='position')
plt.xlabel('Position')
plt.ylabel('Temps')
plt.legend()

plt.subplot(212)
plt.title('Vitesse en fonction du temps')
plt.plot(ts, ys, 'b', label='vitesse')
plt.xlabel('Temps')
plt.ylabel('Vitesse')
plt.legend()
fig.tight_layout()


plt.show()




