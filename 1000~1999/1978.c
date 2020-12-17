#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void find_su(int a, int *cnt)
{
	int i = 2;

	if (a == 1)
		return;
	else
	{
		while (i <= a - 1)
		{
			if (a % i == 0)
				return;
			i++;
		}
		(*cnt)++;
	}
}

int main1978()
{
	int N, S;
	int i = 0;
	int cnt = 0;

	scanf("%d", &N);

	while (i < N)
	{
		scanf("%d", &S);
		find_su(S, &cnt);
		i++;
	}
	printf("%d\n", cnt);

	return 0;
}
