#include<iostream>
#include<iomanip>
using namespace std;

int main(){
    int n;
    cin >> n;

    if(n % 100 == 0 && n % 400 == 0){
        cout << "yes" << endl;
    }else if(n % 100 != 0 && n % 4 == 0 ){
        cout << "yes" << endl;
    }else{
        cout << "no" << endl;
    }

    return 0;
}