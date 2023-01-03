#include <stdio.h>

int main() {
	int number, aim;
	int table[254];
	scanf("%d", &number);
	for (int i = 0; i < number; i++) {
		scanf("%d", &table[i]);
	}
	scanf("%d", &aim);
	int count;
	for (count = 0; count < number; count++) {
		//printf(" %d,%d\n", table[count], aim);
		if (table[count] == aim) {
			printf("%d\n", count);
			break;
		}
	}
	if (count == number) {
		printf("-1\n");
	}
	return 0;
}
