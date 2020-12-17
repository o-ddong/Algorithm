#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	char arr[1000001];
	int flag = 1;
	int check = 0;
	int i = 0;

	scanf("%[^\n]s", arr);

	while (arr[i])
	{
		if (flag == 1 && (('a' <= arr[i] && arr[i] <= 'z') || ('A' <= arr[i] && arr[i] <= 'Z')))
		{
			check++;
			flag = 0;
		}
		else if (arr[i] == ' ')
			flag = 1;
		i++;
	}
	printf("%d", check);
	return 0;
}
