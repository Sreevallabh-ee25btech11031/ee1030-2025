#include <stdio.h>

void compute_parabola(double *y, double *x, int n) {
    for (int i = 0; i < n; i++) {
        x[i] = (y[i] * y[i]) / 4.0;
    }
}
