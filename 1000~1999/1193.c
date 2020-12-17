#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main1193()
{
	int front = 0, back = 0;
	int X;
	int cnt = 0;      // 몇번째 라인인지
	int total = 0;    // 전체 갯수

	scanf("%d", &X);

	while (X > total)  // 1씩 증가하는 전체 total 구하기
	{
		cnt++;
		total += cnt;
	}
	
	front = cnt;
	back = 1;

	int i = 0;
	while (i < total - X)
	{
		front--;
		back++;
		i++;
	}

	if (cnt % 2 == 0)
		printf("%d/%d", front, back);
	else
		printf("%d/%d", back, front);
	return 0;
}

// 이차원 배열로 풀려고 생각했었는데 이렇게 간단히 푸는 방법이 있어 따라해봤다
