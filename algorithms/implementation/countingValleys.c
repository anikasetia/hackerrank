#include <stdio.h>

int main()
{
	int N, i;
	char steps[1000000];
	int valleys = 0;
	int currentLevel = 0;
	int lastLevel = 0;
	scanf("%d", &N);
	scanf("%s", steps);

	for(i=0;i<N;i++)
	{
		lastLevel = currentLevel;
		if(steps[i] == 'U')
		{
			currentLevel++;
		}
		else{
			currentLevel--;
		}
		if(currentLevel == 0 && lastLevel < currentLevel)
		{
			valleys++;
		}
	}
	printf("%d\n", valleys);
	return 0;
}
