import numpy as np
import matplotlib.pyplot as plt


x = np.array([1,2,3,4,2,1,2,3])


h = np.zeros(len(x))
for i in range(len(x)):
	temp = 0
	if i >= 0:
		temp += pow(-0.5,i)
		if i>= 2:
			temp += pow(-0.5,i-2)
	h[i] = temp



def fft(x):	
	n = len(x)
	if(n==1):
		return x
	if(n == 2):
		return np.hstack((x[0]+x[1], x[0]-x[1]))
	
	X1 = fft(x[::2])
	X2 = fft(x[1::2])
	
	D = np.zeros((n//2,), dtype=np.complex128)
	for i in range(n//2):
		D[i] = np.exp(-2j*np.pi*i/n)
	
	X_u = X1 + D*X2
	X_l = X1 - D*X2
	
	return np.hstack((X_u,X_l))


X = fft(x)
H = fft(h)
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
plt.savefig('../fig/ee18btech11019_2.eps')
plt.subplots_adjust(hspace=0.4)
plt.show()
