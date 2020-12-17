#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main1157()
{
	char arr[1000001] = { 0 };
	int word[26] = { 0 };
	int max = 0;
	int i = 0;
	int check = 0;
	int index = 0;

	scanf("%s", arr);

	while (arr[i])
	{
		if ('a' <= arr[i] && arr[i] <= 'z')
		{
			index = arr[i] - 97;
			word[index]++;
		}
		else
		{
			index = arr[i] - 65;
			word[index]++;
		}
		i++;
	}
	i = 0;
	while (i < 26)
	{
		if (word[i] > max)
			max = word[i];
		i++;
	}
	i = 0;
	while (i < 26)
	{
		if (word[i] == max)
		{
			check++;
			index = i;
		}
		i++;
	}

	if (check > 2)
		printf("?");
	else
	{
		printf("%c", index + 65);
	}
	return (0);
}
