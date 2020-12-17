#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void find_suu(int n)
{
	int cnt = 0;
	int i = 1;
	if (n == 1)
		printf("1\n");
	else
	{
		while (n + i <= 2 * n)
		{
			int j = 2;
			int check = 0;

			while (j * j <= n + i)
			{
				if ((n + i) % j == 0)
				{
					check = 1;
					j++;
					break;
				}
				j++;
			}
			if (check == 0)
				cnt++;
			i++;
		}
		printf("%d\n", cnt);
	}
}


int main4948()
{
	int n;

	while (1)
	{
		scanf("%d", &n);
		
		if (n == 0)
			break;
		else
			find_suu(n);
	}
	return 0;
}
