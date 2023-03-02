import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

A = np.array ([[1, 2, 3],
                [4, 5, 6]])
#print(A) #numpy.linspace (numpy.org) for extra documentation
#print(A.shape)

#Save as pickle for advanced use
#np.savetxt("a_out.txt", A)
#b = np.loadtxt("a_out.txt")

B = np.zeros((2,2))
print(B)
B[0,0] = 1
print(B)

f, ax = plt.subplots(1,1, figsize=(5,4))

x = np.linspace(0, 10, 1000)
y = np.power(x, 2)
ax.plot(x, y)
ax.set_xlim((1,5))
ax.set_ylim((0,30))
ax.set_xlabel('my x label')
ax.set_ylabel('my y label')
ax.set_title('plot title, including $\Omega$')

plt.tight_layout()
plt.show()
#plt.savefig('line_plot_plus.pdf')