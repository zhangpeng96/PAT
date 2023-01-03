#include <stdio.h>

int main(void) {
	int input, count;
	count = 0;
	
	scanf("%d", &input);
	
	while (input > 1) {
		if (input % 2) {
//			printf("odd: %d\n", input);
			input = (3 * input + 1) / 2;
		} else {
			input = input / 2;
//			printf("even: %d\n", input);
		}
		count ++;
	}
	
	printf("%d", count);
}

