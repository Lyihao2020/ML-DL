// 判断一个数是否为质数
#include<iostream>
#include<math.h>
using namespace std;

int main(){
    int n;
    cin >> n;

    bool is_prime = true;
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0){
            is_prime = false;
            break;
        }
    }

    if(is_prime) cout << "yes" << endl;
    else cout << "no" << endl;

    return 0;

}