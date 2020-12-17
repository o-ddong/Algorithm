#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main2941()
{
	char arr[101];
	int len = 0;
	int cnt = 0;

	scanf("%s", arr);

	len = strlen(arr);

	for (int i = 0; i < len; i++)
	{
		if (arr[i] == 'c' && (arr[i + 1] == '=' || arr[i + 1] == '-'))
			i++;
		else if (arr[i] == 'd' && (arr[i + 1] == 'z' && arr[i + 2] == '=') || (arr[i + 1] == '-'))
		{
			if (arr[i] == 'd' && (arr[i + 1] == '-'))
				i++;
			else
				i += 2;
		}
		else if ((arr[i] == 'l' || arr[i] == 'n') && arr[i + 1] == 'j')
			i++;
		else if ((arr[i] == 's' || arr[i] == 'z') && arr[i + 1] == '=')
			i++;
		cnt++;
	}

	printf("%d", cnt);
	return 0;
}
