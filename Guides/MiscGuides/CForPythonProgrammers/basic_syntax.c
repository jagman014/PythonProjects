// uses delimiters for each statement / block
// ending with a ;, and blocks surrounded by {}
/* can also comment on 
multiple lines like sql */
#include <stdio.h>

int main() {
    int x = 0; // declares x to be of type int, and initialised to 0

    if (x == 0) {
        // block of code
        int y = 1; // local code block variable

        printf("x is %d y is %d\n", x, y);
    }

    if (x == 13) 
        printf("x is 13!\n");

    printf("past the if block");

    return 0;
}