/*
    @name     : 7-3
    @version  : 21.0209
    @author   : zhangpeng96
    @time     : 
    @accepted : 
    @desc     : p0 right +12
                p1 right +1
                p2 right +2
                p3 right +2
                p4 error
*/

#include <stdio.h>
#include <cmath>

bool judge(int a, int b) {
    if ( (3*a*a - 3*a + 1) == ( (2*b*b - 2*b + 1) * (2*b*b - 2*b + 1) )  )
        return true;
    else
        return false;
}

int main() {
    int start, end;
    bool solution = false;
    scanf("%d %d", &start, &end);
    for (int a=start; a <= end; a++) {
        for (int b=1; b <= pow( (3*a*a - 3*a + 1)/4.0, 0.25)+1; b++) {
            if (judge(a, b)) {
                printf("%d %d\n", a, b);
                solution = true;
            }
        }
    }
    if (!solution)
        printf("No Solution");

    return 0;
}


