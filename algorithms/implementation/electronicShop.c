#include <stdio.h>

int main(){
	int s, n, m, i, j;
	int keyboardPrice[1000];
	int usbPrice[1000];
	int moneySpent = -1;
	int currentSum;
	
	scanf("%d %d %d", &s, &n, &m);
	
	for(i=0;i<n;i++)
	{
		scanf("%d", &keyboardPrice[i]);
	}
	for(i=0;i<m;i++)
	{
		scanf("%d", &usbPrice[i]);
	}

	for(i=0;i<n;i++)
	{
		for(j=0;j<m;j++)
		{
			currentSum = keyboardPrice[i] + usbPrice[j];
			if(currentSum <= s && currentSum > moneySpent)
			{
				moneySpent = currentSum;
			}	
		}
	}

	printf("%d\n", moneySpent);
	return 0;
}
