#include <stdio.h>
#define SIZE 26

int main() {
	int num, i, count[SIZE] = { 0 }, flag = 0;
	char name[31];

	scanf("%d", &num);

	for (i = 0; i < num; i++) {
		scanf("%s", name);
		count[name[0] - 'a']++;
	}

	for (i = 0; i < SIZE; i++) {
		if (count[i] >= 5) {
			if (!flag)
				flag = 1;
			printf("%c", 'a' + i);
		}
	}
	if (!flag)
		printf("PREDAJA");

	printf("\n");
}