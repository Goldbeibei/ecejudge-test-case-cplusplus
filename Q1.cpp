#include <bits/stdc++.h>
using namespace std;
int main() {
    long long a,b,c;
    cin >> a >> b >> c;
	if (b == 0) {
	    cout << "埃计ぃ 0" << endl;
	} 
	else {
	    long long dividend = a;
	    long long divisor = b;
	    long long quotient = 0;
	    long long remainder = 0;
	    long long temp_dividend = 0;
	    long long temp_quotient = 0;
		
		//璸衡俱计场だ緇计
		cout << dividend/divisor << ".";
		quotient = dividend%divisor;
		//计埃猭 
		for(int i=0;i<c;i++){
			quotient*=10;
			cout << quotient/divisor; 
			quotient%=divisor;
		}
	}
	return 0;
}
