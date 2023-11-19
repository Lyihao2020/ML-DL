// Acwing 671. DDD

#include <cstdio>
#include <iostream>

using namespace std;

int main() {

    int DDD[8] = {61, 71, 11, 21, 32, 19, 27, 31};
    string Destination[8] = {"Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"};
    int n;

    cin >> n;

    int i;
    for(i = 0; i < 8; i++) {
        if(n == DDD[i]) {
            cout << Destination[i];
            break;
        }
    } 
    if(i == 8)  cout << "DDD nao cadastrado";

    return 0;

}

/*
#include <iostream>
using namespace std;
int main()
{
    int x;
    cin>>x;
    if (x==61)   cout<< "Brasilia" <<endl;
    else if(x==71) cout<< "Salvador" <<endl;
    else if(x==11) cout<< "Sao Paulo" <<endl;
    else if(x==21) cout<< "Rio de Janeiro" <<endl;
    else if(x==32) cout<< "Juiz de Fora" <<endl;
    else if(x==19) cout<< "Campinas" <<endl;
    else if(x==27) cout<< "Vitoria" <<endl;
    else if(x==31) cout<< "Belo Horizonte" <<endl;
    else cout << "DDD nao cadastrado" <<endl;
    return 0;
}
*/