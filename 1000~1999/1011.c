#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main1011()
{
	int T, x, y;
	int i = 0;
	int share = 0;

	scanf("%d", &T);

	while (i < T)
	{
		int cnt = 0;
		scanf("%d %d", &x, &y);
		if (x > y)
			break ;
		if (((y - 1) - (x + 1)) % 2 == 0)
			share = (y - x - 2) / 2;
		else
			share = (y - x - 2) / 2 + 1;
		cnt += share + 2;
		printf("%d\n", cnt);
		i++;
	}
	return 0;
}

//while (i < T)
//{
//	int cnt = 0;
//	scanf("%d %d", &x, &y);
//	while (x < y)
//	{
//		if (cnt == 0 || y - 1 == x || y - 2 == x)
//			x += 1;
//		else
//			x += 2;
//		cnt++;
//	}
//	i++;
//	printf("%d\n", cnt);
//}
