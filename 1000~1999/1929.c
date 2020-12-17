#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void find_num1(int M, int N)
{
	while (M <= N)
	{
		if (M == 1)
		{
			M++;
			continue;
		}
		int i = 2;
		int check = 1;
		while (i * i <= M)
		{
			if (M % i == 0)
			{
				check = 0;
				break;
			}
			i++;
		}
		if (check == 1)
			printf("%d\n", M);
		M++;
	}
}

int main1929()
{
	int M, N;

	scanf("%d %d", &M, &N);

	if (M > N)
		return 0;
	find_num1(M, N);

	return 0;
}
