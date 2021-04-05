#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct
{
	double Re; 
	double Im;
} complex;



void fft(complex *X, int n)
{

	if(n <= 1) return;
	
	complex *Xo = (complex *) malloc(n/2*sizeof(complex));
	complex *Xe = (complex *) malloc(n/2*sizeof(complex));
	

	for(int i = 0; i < n/2; i++) 
	{
		Xe[i] = X[2*i];
		Xo[i] = X[2*i+1];
	}
	
	//recursion
	fft(Xe, n/2);	 	
	fft(Xo, n/2);		
	

	for(int i = 0; i < n/2; i++) 
	{

		double cose = cos(2*M_PI*i/n);
		double sine = sin(2*M_PI*i/n);
		
		complex z;
		
		z.Re = cose * Xo[i].Re + sine * Xo[i].Im;	
		z.Im = cose * Xo[i].Im - sine * Xo[i].Re;	

		X[i].Re = Xe[i].Re + z.Re;
		X[i].Im = Xe[i].Im + z.Im;
		X[i+n/2].Re = Xe[i].Re - z.Re;
		X[i+n/2].Im = Xe[i].Im - z.Im;
	}
	
	free(Xo);
	free(Xe);
}

int main()
{	

    int n = 8; 
	double x[] = {1,2,3,4,2,1,2,3};
	
	complex *X = (complex *) malloc(n*sizeof(complex));
	for(int i = 0; i < n; i++) 
	{
		X[i].Re = x[i];
		X[i].Im = 0;
	}
	fft(X, n);
	
	for(int i = 0; i < n; i++) 
		printf("%.5lf,+ j*%.5lf\n", X[i].Re, X[i].Im);
}