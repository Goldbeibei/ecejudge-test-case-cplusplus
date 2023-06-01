#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
long long a, b; // 使用long long可以支持更大的?字
int N;
cin >> a >> b >> N;
    
double result = 1.0*a/b;

int mult = 1;
for(int i = 0; i < N; i++){
    mult *= 10;
}

result = round(result * mult) / mult;

cout << fixed << setprecision(N) << result << endl;  
return 0;
}
