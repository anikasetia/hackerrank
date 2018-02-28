#include <stdio.h>

int main(){
	int inputArray[100000];
	int outputArray[100000];
	int n, d, counter;
	scanf("%d", &n);
	scanf("%d", &d);
	for(counter = 0; counter < n; counter++)
	{
		scanf("%d",&inputArray[counter]);
	}

	for(counter = d; counter < n; counter++)
	{
		outputArray[counter - d] = inputArray[counter];
	}
	for(counter = 0; counter < d; counter++){
		outputArray[n- d + counter] = inputArray[counter];
	}

	for(counter = 0; counter < n ; counter++)
	{
		printf("%d ", outputArray[counter]);
	}
	printf("\n");
	return 0;
}
