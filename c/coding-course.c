#include <time.h>
#include <stdio.h>
#include <stdlib.h> 

// es: 9 - calcola il fattorale n!
int fattoriale() {
	int n; int i; 

	scanf("%d", &n); 
	for (i=n-1; i > 0; i--) {
		n = n*i;
	};

	printf("%d", n);
	return 0; 

};

// es: 7 - dati due interi calcola il loro MDC (consiglio l’algoritmo di Euclide)
int mcd() {

	// inserisci 2 numeri > 1 e a > b
	int a; int b; int r;
	scanf("%d", &a); scanf("%d", &b);
	if (a > b && a > 1 && b > 1) {
		r = a%b;
		if (r != 0) {
			while (r != 0) {
				if (b%r == 0) {
					printf("\n%d",r);
					return 0;
				};
				r = b%r; 
			};
		} else {
			printf("\n%d", a/b);
		} 
	};
	return 0;
}; 


// es: 8 - genera casualmente 10 interi stampali e calcola il loro massimo e il loro minimo.
int max_min() {

	int n[10+1]; int i; int min; int max; srand(time(NULL));
	for (i=0; i<10; i++) {
		n[i] = rand()%100 + 1;
		printf("%d ", n[i]);
	};
	
	min = n[0]; max = n[0];

	for (i=1; i<10; i++) {
		if (n[i] <= min) {
			min = n[i];
		} else if (n[i] >= max) {
			max = n[i];
		};
	};

	printf("\n%d  %d", min, max);
	return 0;

}

// es: 10 - date due stringhe determinare quale fra queste viene prima in ordine alfabetico.
int ordine_alfabetico() {
	char a[15]; char b[15]; 
	int i;int j; int c_uno; int c_due;
	
	char alphabet[] = "abcdefghijklmnopqrstuvwxyzw";
	scanf("%s", a); scanf("%s", b);
	
	for (i=0; i<15; i++){
		if (a[i] != b[i]) {
			for (j=0; j<27; j++) {
				if (alphabet[j] == a[i]) {
					c_uno = j; 
				}else if (alphabet[j] == b[i]) {
					c_due = j;
				}; if (c_due > c_uno) {
					printf("%s %s", a,b);	
					break;
				} else if (c_uno > c_due) {
					printf("%s %s", b,a);
					break;
				};
			}

		} else if (a[i] == b[i]) {
			continue; 
		}
	}	
		
	return 0;

};


// - LEZIONE 2 - 




//APPROFONDIMENTO N.1
int determinante_matrici_2_per_2() {
	//int n; scanf("%d", &n); int m; scanf("%d", %m); int p; scanf("%d", &p); 
	int a[2][2] = {{1,2},{3,4}}; int D = (a[0][0]*a[1][1])-(a[1][0]*a[0][1]);
	printf("%d", D); 

	
}; 
// APPROFONDIMENTO N.2
int prodotto_matrici_n_per_m_per_m_per_p(){
	//int n; scanf("%d", &n); int m; scanf("%d", %m); int p; scanf("%d", &p);
	int n = 3; int m = 2; int p = 3; int sum;
	int a[3][2] = {{1,2},{3,4}, {5,6}}; int b[2][3] = {{1,2,3},{3,4,5}}; 

	for (int i=0; i<n; i++){
		for (int j=0; j<p; j++){
			sum = 0;
			for (int y=0; y<m; y++){
				sum = sum+a[i][y]*b[y][j];
			};	printf("%d ", sum);
		};
	};  
}; 


//APPROFONDIMENTO N.3
int somma_matrici_n_per_m() {
	int n = 2; int m = 3;
	int a[2][3] = {{2,3,4},{1,2,3}}; int b[2][3] = {{3,4,5},{6,7,8}};
	for (int i=0; i<n; i++){
		for (int j=0; j<m; j++){
			printf("%d ",a[i][j]+b[i][j]);
		}
	}
}


//APPROFONDIMENTO N.4
int determinante_n_per_n(){
	int k = 2; int m[2][2] = {{1,2},{3,4}}; 
	int d; int a; d=1; a=1;
	for (int i=-1; i<k-1;i++){
		for (int j=-1;j<k-1;j++){
			d = d*m[i][j];
			a = a*m[i][j-1];
		}
	} printf("%d",d - a); 
}



//metodo montercarlo 
float f(float x){
	return x-1;
}
int montecarlo_area(){
	srand((unsigned int)time(NULL));

	float a;scanf("%f",&a);
	float b;scanf("%f",&b);
	float ym;scanf("%f",&ym);
	
	float n=10000;float ni;
	for (int i=0;i<n;i++){
		float y=((float)rand())/((float)RAND_MAX)*(ym-0)+0;
		float x=((float)rand())/((float)RAND_MAX)*(b-a)+a;
		
		if (y<=f(x)){
			ni++;
		}
	
	} float A = (ym*(b-a)*ni)/n; printf("%f",A);
}




int bubble_sort(){
	float a[5] = {5,68,3,5,2};
	int size = sizeof a / sizeof *a; 
	for (int i=0;i<size;i++){
		for (int j=0;j<size-1;j++){
			if (a[j] >= a[j+1]){
				float k = a[j]; a[j]=a[j+1]; a[j+1]=k;
			}
		}
	} for (int y=0; y<5; y++){
		printf("%f ", a[y]);
	}
}




int crypt_cesare() {


	char string[30]; int s;
	char alphabet[] = "abcdefghijklmnopqrstuvwxyzw "; s = 3;
	scanf("%s", string);

	for (int i=0;i<30;i++) {
		for (int j=0; j<26; j++) {
			if (alphabet[j] == string[i]) {
				printf("%c", alphabet[(j+s)%26]);

			}
		}
	}

	return 0;

}



int main() 
{
	determinante_n_per_n();
	return 0;
	
}