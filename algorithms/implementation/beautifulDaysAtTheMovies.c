#include <stdio.h>
#include <math.h>
int abs(int num){
	if(num < 0)
	{
		return (num*-1);
	}
	return num;
	
}
int reverse(int x){
	int reversed = 0;	
	
	while(x!=0)
	{
		reversed = reversed*10 + (x%10);
		x = x / 10;
	}	

	return reversed;
}

int main(){
	int i, j, k, start, evenDays;
	scanf("%d %d %d", &i, &j, &k);
	evenDays = 0;
	for(start = i; start <= j; start++)
	{
		if((abs((reverse(start) - start)))%k == 0){
			evenDays++;	
		}
	}
	printf("%d\n", evenDays);
	return 0;
}
