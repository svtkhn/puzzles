#include <iostream>    

int max(int a, int b) {
  return (a > b)? a : b;
} 

int knapSack(int n, int maxMass, int masses[], int prices[]) { 
  if (n == 0 || maxMass == 0) {
    return 0; 
  }

  if (masses[n-1] > maxMass) {
    return knapSack(n-1, maxMass, masses, prices);
  } else {
    return max(
        prices[n-1] + knapSack(n-1, maxMass-masses[n-1], masses, prices),
        knapSack(n-1, maxMass, masses, prices)
        );
  }
}

int main() { 
  int prices[] = {60, 100, 120}; 
  int masses[] = {10, 20, 30}; 
  int maxMass = 50; 
  int n = sizeof(prices)/sizeof(prices[0]); 
  std::cout << knapSack(n, maxMass, masses, prices);
}
