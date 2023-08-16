#include <iostream>
using namespace std;

// 不需要一个一个去比较，只需要比较首字母即可！！
int main()
{
    string a[3];
    string ss;
    for(int i=0;i<3;i++) cin >> a[i],ss+=a[i][0];


    if(ss=="vac") cout<<"aguia";
    if(ss=="vao") cout<<"pomba";
    if(ss=="vmo") cout<<"homem";
    if(ss=="vmh") cout<<"vaca";
    if(ss=="iih") // 情况特殊
    {
        if(a[2] == "hematofago") cout<<"pulga";
        else cout<<"lagarta";
    }
    if(ss=="iah") cout<<"sanguessuga";
    if(ss=="iao") cout<<"minhoca";

}
