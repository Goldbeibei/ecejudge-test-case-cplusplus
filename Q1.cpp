#include <iostream>
#include <string>

using namespace std;

int main() {
    string str1, str2;
    int pos = -1;

    getline(cin, str1);
    getline(cin, str2);

    while ((pos = str1.find(str2, pos+1)) != string::npos) {
        cout << pos+1 << ' ';
    }
    cout << endl;
    return 0;
}
