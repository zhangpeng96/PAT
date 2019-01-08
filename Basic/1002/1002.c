#include <stdio.h>
char* parseString(int number) {
    char *p;
    switch(number) {
        case 0:
            p = "ling";
            break;
        case 1:
            p = "yi";
            break;
        case 2:
            p = "er";
            break;
        case 3:
            p = "san";
            break;
        case 4:
            p = "si";
            break;
        case 5:
            p = "wu";
            break;
        case 6:
            p = "liu";
            break;
        case 7:
            p = "qi";
            break;
        case 8:
            p = "ba";
            break;
        case 9:
            p = "jiu";
            break;
        default:
            break;
        return p;
    }
}

int main(void) {
	char inputNumber[100], result[32], output[100];
	int i, calcNumber;
	
	calcNumber = 0;
	i = 0;
	scanf("%s", inputNumber);
	while(inputNumber[i]) {
		calcNumber += (inputNumber[i] - 0x30);
		i ++;
	}
	
    sprintf(result, "%d", calcNumber);

    i = 0;

    while(result[i]) {
        char *p = parseString(result[i] -0x30);
        printf("%s", p);
        i ++;
        if(!result[i]) {
        	break;        	
		}
        printf(" ");
    }
	
}

