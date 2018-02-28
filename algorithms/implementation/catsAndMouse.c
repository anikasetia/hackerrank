#include <stdio.h>

int main()
{
	int q, i, catA[100], catB[100], mouseC[100], distanceA, distanceB;
	scanf("%d", &q);
	for(i=0;i<q;i++)
	{
		scanf("%d %d %d", &catA[i], &catB[i], &mouseC[i]);
	}
	for(i=0;i<q;i++)
	{
		distanceA = mouseC[i] - catA[i];
		if(distanceA < 0)
		{
			distanceA = distanceA * -1;
		}
		distanceB = mouseC[i] - catB[i];
		if(distanceB < 0)
		{
			distanceB = distanceB * -1;
		}
		if(distanceA == distanceB)
		{
			printf("Mouse C\n");
		}
		else if(distanceA < distanceB){
			printf("Cat A\n");
		}
		else
		{
			printf("Cat B\n");
		}
	}
	return 0;
}
