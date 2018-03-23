#include <stdio.h>

int main(){
	int T, N[100], M[100], S[100], i, poisonReceiver, loops, remainder;
	scanf("%d", &T);
	for(i=0;i<T;i++)
	{
		scanf("%d %d %d", &N[i], &M[i], &S[i]);
	}
	poisonReceiver = 0;
	for(i=0;i<T;i++)
	{
		poisonReceiver = ((M[i] + S[i] -1)%N[i]);
		if(poisonReceiver == 0)
		{
			poisonReceiver = N[i];
		}
		printf("%d\n", poisonReceiver);	
	}
	return 0;
}
