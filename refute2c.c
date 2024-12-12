#include <stdio.h>

void checkEvenOdd(int num) {
    if (num % 2 == 0)
        printf("%d is even.\n", num);
    else
        printf("%d is odd.\n", num);
}

int main() {
    checkEvenOdd(4);  // Expected output: 4 is even.
    checkEvenOdd(7);  // Expected output: 7 is odd.
    return 0;
}
