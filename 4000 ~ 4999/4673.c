#include <stdio.h>

int recursive(int n)
{
	int cal = 0;

	if (n >= 10)
		cal += recursive(n / 10);
	cal += (n % 10);

	return (cal);
}

int main4673()
{
	int i = 1;
	int sum = 0;
	int arr[10001] = { 0, };

	while (i <= 10000)
	{
		sum = recursive(i) + i;
		if (sum > 10000)
		{
			i++;
			continue;
		}
		arr[sum] = 1;
		i++;
	}
	i = 1;
	while (i <= 10000)
	{
		if (!arr[i])
			printf("%d\n", i);
		i++;
	}
	return 0;
}
