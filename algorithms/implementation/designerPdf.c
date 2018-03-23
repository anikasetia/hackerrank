#include <stdio.h>

int main(){
	int heights[26];
	char word[11];
	int i = 0;
	int maxHeight, wordLength, currentHeight;
	for(i=0;i<26;i++)
	{
		scanf("%d", &heights[i]);
	}
		
	scanf("%s", word);
	
	i=0;
	wordLength = 0;
	maxHeight = 0;
	while(word[i] != '\0'){
		currentHeight = heights[word[i] - 'a'];
		if(maxHeight < currentHeight)
		{
			maxHeight = currentHeight;
		}
		wordLength++;
		i++;
	}
	printf("%d\n", wordLength * maxHeight);
	return 0;
}
