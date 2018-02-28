#include <stdio.h>

int main(){
	int n, i;
	int array[100];
	int count[100] = {0};
	scanf("%d", &n);
	int max = 0;
	for(i=0;i<n;i++)
	{
		scanf("%d", &array[i]);
		count[array[i]]++;
	}
	for(i=1;i<100;i++)
	{
		if(count[i] != 0)
		{
			if(count[i] > max)
			{
				max = count[i];
			}
		}
		if(count[i] != 0 && count[i-1] != 0)
		{
			if(count[i] + count[i-1] > max)
			{
				max = count[i] + count[i-1];
			}
		}
	}
	printf("%d\n", max);
	return 0;
}
