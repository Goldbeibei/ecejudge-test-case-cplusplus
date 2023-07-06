#include<iostream>
using namespace std;
int main(){
    int a,b,c;
    cin>>a>>b>>c;
    if((a&&b)==c){
        cout<<"And"<<endl;
        }
    if(a||b==c){
        cout<<"Or"<<endl;
    }
    if(a^b==c){
        cout<<"Xor"<<endl;
    }
    if((a&&b)!=c and (a||b!=c) and (a^b!=c)){
        cout<<"Impossible"<<endl;
    }
}
