#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int su(int num)
{
	int sum = 0;
	int one = 0, two = 0, thr = 0;
	
	if (num < 100)
		sum++;
	else
	{
		one = num / 100;
		two = (num / 10) % 10;
		thr = num % 10;
		if ((two - one) == (thr - two))
			sum++;
	}

	return (sum);
}

int main1065()
{
	int n;
	int i = 1;
	int sum = 0;

	scanf_s("%d", &n);

	while (i <= n)
	{
		sum += su(i);
		i++;
	}
	printf("%d", sum);
	return 0;
}
