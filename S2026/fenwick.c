#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n, q;
    if (scanf("%d %d", &n, &q) != 2) return 0;

    long long *bit = (long long*)calloc((size_t)n + 1, sizeof(long long));
    if (!bit) return 0;

    for (int t = 0; t < q; t++) {
        char op;
        scanf(" %c", &op);

        if (op == '+') {
            int i;
            long long x;
            scanf("%d %lld", &i, &x);

            // Fenwick add at index i (
            int idx = i + 1;
            while (idx <= n) {
                bit[idx] += x;
                idx += idx & -idx;
            }
        } else { // '?'
            int len;
            scanf("%d", &len);

            // Query the prefix sum
            long long s = 0;
            int idx = len;
            while (idx > 0) {
                s += bit[idx];
                idx -= idx & -idx;
            }
            printf("%lld\n", s);
        }
    }

    free(bit);
    return 0;
}
