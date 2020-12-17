#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main1316()
{
	int n;
	int i = 0, j = 0, k = 0;
	int check = 0; 
	int cnt = 0;
	char word[101];
	scanf("%d", &n);

	while (i < n)
	{
		j = 0;
		scanf("%s", word);
		while (word[j])
		{
			if (word[j] != word[j + 1] && word[j+1] != 0)
			{
				for (k = 0; k < j + 1; k++)
				{
					if (word[j + 1] == word[k])
					{
						check = 1;
						break;
					}	
				}
			}
			j++;
		}
		if (!check)
			cnt++;
		check = 0;
		i++;
	}
	printf("%d", cnt);
}
