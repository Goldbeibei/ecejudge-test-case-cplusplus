#include <bits/stdc++.h>
using namespace std;
int main() {
    long long a,b,c;
    cin >> a >> b >> c;
	if (b == 0) {
	    cout << "���Ƥ��ର 0" << endl;
	} 
	else {
	    long long dividend = a;
	    long long divisor = b;
	    long long quotient = 0;
	    long long remainder = 0;
	    long long temp_dividend = 0;
	    long long temp_quotient = 0;
		
		//�p���Ƴ������l��
		cout << dividend/divisor << ".";
		quotient = dividend%divisor;
		//�p�ƪ����k 
		for(int i=0;i<c;i++){
			quotient*=10;
			cout << quotient/divisor; 
			quotient%=divisor;
		}
	}
	return 0;
}
