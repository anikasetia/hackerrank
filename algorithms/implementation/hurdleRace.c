#include <stdio.h>

int main(){
	int n, k, i;
	int currentHeight, drinksNeeded;
	int maxHeight = 0;
	scanf("%d %d", &n, &k);
	for(i=0;i<n;i++)
	{
		scanf("%d", &currentHeight);
		if(currentHeight > maxHeight)
		{
			maxHeight = currentHeight;
		}
	}
	drinksNeeded = maxHeight - k;
	if(drinksNeeded <= 0)
	{
		printf("0\n");
	}
	else{
		printf("%d\n", drinksNeeded);
	}
	return 0;
}
