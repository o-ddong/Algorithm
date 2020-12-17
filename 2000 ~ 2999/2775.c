#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main2775()
{
	int T;        // ÃÑ ÄÉÀÌ½º
	int i = 0;    // 
	int k, n;     // kÃş nÈ£
	int live[1000] = { 0, };

	scanf("%d", &T);

	while (i < T)
	{
		scanf("%d %d", &k, &n);

		int high = 0;        // ÃşÀÌ¶û ºñ±³ÇÒ º¯¼ö
		while (high <= k)
		{
			if (high == 0)
			{
				for (int j = 1; j <= n; j++)
					live[j] = j;
			}
			else
			{
				for (int j = 1; j <= n; j++)
				{
					if (j == 1)
						live[j] = live[j];
					else
						live[j] += live[j - 1];
				}
			}
			high++;
		}	
		i++;
		printf("%d\n", live[n]);
	}
	
	return 0;
}
