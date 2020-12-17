#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void find_num(int M, int N)
{
	int sum = 0;
	int min = 10000;

	while (M <= N)
	{
		int i = 2;
		int check = 1;
		if (M == 1)
		{
			M++;
			continue;
		}
		while (i < M)
		{
			if (M % i == 0)  // 소수가 아니라면 check = 0
			{
				check = 0;
				break;
			}
			i++;
		}
		if (check == 1)
		{
			sum += M;
			if (M < min)
				min = M;
		}
		M++;
	}
	if (min == 10000)
		printf("-1");
	else
		printf("%d\n%d", sum, min);
}

int main2581()
{
	int M, N;

	scanf("%d %d", &M, &N);

	if (M > N)
		return 0;
	find_num(M, N);

	return 0;
}
