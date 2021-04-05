import numpy as np
import matplotlib.pyplot as plt


x = np.array([1,2,3,4,2,1])


h = np.zeros(len(x))
for i in range(len(x)):
	temp = 0
	if i >= 0:
		temp += pow(-0.5,i)
		if i>= 2:
			temp += pow(-0.5,i-2)
	h[i] = temp



def dft(x):
	n = len(x)
	W = np.zeros((n,n),dtype=np.complex128)
	for i in range(n):
		for j in range(n):
				W[i][j] = np.exp(-2j*np.pi*i*j/n)
	return np.matmul(W,x)


X = dft(x)
H = dft(h)
Y = X*H


plt.figure(figsize=(9,15))
plt.subplot(3,2,1)
plt.stem(np.abs(X),use_line_collection=True)
plt.title('$|X(k)|$')
plt.grid()

plt.subplot(3,2,2)
plt.stem(np.angle(X),use_line_collection=True)
plt.title(r'$\angle{X(k)}$')
plt.grid()

plt.subplot(3,2,3)
plt.stem(np.abs(H),use_line_collection=True)
plt.title('$|H(k)|$')
plt.grid()

plt.subplot(3,2,4)
plt.stem(np.angle(H),use_line_collection=True)
plt.title(r'$\angle{H(k)}$')
plt.grid()

plt.subplot(3,2,5)
plt.stem(np.abs(Y),use_line_collection=True)
plt.title('$|Y(k)|$')
plt.grid()

plt.subplot(3,2,6)
plt.stem(np.angle(Y),use_line_collection=True)
plt.title(r'$\angle{Y(k)}$')
plt.grid()
plt.savefig('../fig/ee18btech11019_1.eps')

plt.subplots_adjust(hspace=0.4)
plt.show()
