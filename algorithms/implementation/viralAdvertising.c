#include<stdio.h>

int main()
{
	int start, like, dislike, n, i, reach, totalLiked;
	start = 5;
	scanf("%d", &n);
	totalLiked = 0;
	
	like = start/2;	
	
	for(i=0;i<n;i++)
	{
		totalLiked = totalLiked + like;
		reach = like * 3;
		like = reach / 2;
	}

	printf("%d\n", totalLiked);
	
	return 0;
}
