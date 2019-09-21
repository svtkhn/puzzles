#include <iostream>

using namespace std;

void findBestItems(int n, int maxMass, int masses[], int prices[]) {
  int i, j;
  int T[n + 1][maxMass + 1];

  for (i = 0; i <= n; i++) {
    for (j = 0; j <= maxMass; j++) {
      if (i == 0 || j == 0)
        T[i][j] = 0;
      else if (masses[i - 1] <= j)
        T[i][j] = max(T[i - 1][j - masses[i - 1]] + prices[i -1], T[i - 1][j]);
      else
        T[i][j] = T[i - 1][j];
    }
  }

  int usedItems[n];
  int numberOfUsedItems = 0;
  i = n;
  j = maxMass;

  while (i > 0) {
    if (T[i][j] == T[i - 1][j]) {
      i--;
    } else {
      usedItems[numberOfUsedItems++] = i;
      j = j - masses[i];
      i--;
    }
  }

  numberOfUsedItems--;

  while (numberOfUsedItems >= 0)
    cout << usedItems[numberOfUsedItems--] << ' ';
}

int main() {
  int n, maxMass;
  cin >> n >> maxMass;

  int masses[n], prices[n];

  for (int i = 0; i < n; i++)
    cin >> masses[i];

  for (int i = 0; i < n; i++)
    cin >> prices[i];

  findBestItems(n, maxMass, masses, prices);

  return 0;
}
