#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main2869()
{
	int A, B, V;
	int cal = 0;
	int day = 0;

	scanf("%d %d %d", &A, &B, &V);

	if ((V - B) % (A - B) != 0)
		day = (V - B) / (A - B) + 1;
	else
		day = (V - B) / (A - B);
	printf("%d\n", day);
	return 0;
}
