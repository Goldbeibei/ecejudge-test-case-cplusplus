#include <iostream>
using namespace std;

int main() {
    char ch;
    cin >> ch;
    for(char i ='A';i<=ch;i++){
        for(char j='A';j<i;j++){
            cout << ' ';
        }
        cout << i <<endl;
    }
    return 0;
}
