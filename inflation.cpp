#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <set>
#include <iomanip>

using namespace std;

int main() {
  int n;
  int tmp;
  int possible = 1;
  cin >> n;

  vector<int> cans(n);
  vector<int> loons(n);
  set<double> frac;

  for (int i = 0; i < n; i++) {
    cin >> tmp;
    cans[i] = tmp;
    loons[i] = i + 1; // capacities 1..n
  }

  // Sort both descending (largest can ↔ largest balloon)
  sort(cans.begin(), cans.end(), greater<int>());
  sort(loons.begin(), loons.end(), greater<int>());

  for (int i = 0; i < n; i++) {
    if (cans[i] > loons[i]) {
      possible = 0; // would explode
      break;
    }
    double f = static_cast<double>(cans[i]) / static_cast<double>(loons[i]);
    frac.insert(f);
  }

  if (possible) {
    // minimum fraction is the first element in the sorted set
    double ans = *frac.begin();
    cout.setf(std::ios::fixed);
    cout << setprecision(10) << ans << "\n";
  } else {
    cout << "impossible\n";
  }

  return 0;
}

