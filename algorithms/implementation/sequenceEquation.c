#include <stdio.h>


int main()
{
	int p[50], n, i, x, j, px, k;
	int foundX;
	scanf("%d", &n);
	printf("Scanned n and n = %d\n", n);
	for(i=0;i<n;i++)
	{
		printf("Enter the %dth number\n", i+1);
		scanf("%d\n", &p[i]);
	}
	printf("Scanned the array p\n");
	for(i=0;i<n;i++)
	{
		foundX = 0;
		for(j=0;j<n;j++)
		{
			printf("looking for value %d\n", i+1);
			if(i+1 == p[j]){
			
				px = i+1;
				printf("px is %d\n", px);
				for(k=0;k<n;k++)
				{
					if(px == p[k]);
					printf("%d", k+1);
					foundX = 1;
					break;	
				}
			}
			if(foundX == 1)
			{
				break;
			}
		}
	}
	return 0;
}
	

