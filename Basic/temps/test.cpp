#include <stdio.h>
#include "string.h"

int main(int argc, char *argv[]) {
	int i, len = 0;

	printf("%d\n", argc);
	for (i = 0; i < argc; i++) {
		printf("%s\n", argv[i]);
	}

	for (i = 1; i < argc; i++) {
		len += strlen(argv[i]);
	}
	printf("%d\n", len);
}