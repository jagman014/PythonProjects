#include <stdio.h>
#include "example_loop_if.h"

int main() {
    for (int i = 0; i < 100; i++)
    {
        int result;
        result = i % 2;
        if (result == 0) {
            printf("%d\n", i);
        }
    };
    return 0;
}
