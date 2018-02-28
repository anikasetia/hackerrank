#include <stdio.h>

int backToFront(int n, int p){
	return (n/2-p/2);
}

int frontToBack(int p){
	return p/2;
}
int main(){
	int n, p, fToB, bToF;
	scanf("%d", &n);
	scanf("%d", &p);
	fToB = frontToBack(p);
	bToF = backToFront(n, p);
	if(fToB < bToF)
	{
		printf("%d\n", fToB);
	} 
	else{
		printf("%d\n", bToF);
	}
}
