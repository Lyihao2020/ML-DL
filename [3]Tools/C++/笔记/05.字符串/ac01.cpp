// 常用ASCII值：’A’-‘Z’ 是65~90，’a’-‘z’是97-122，’0’-‘9’是48-57。
// 字符可以参与运算，运算时会将其当做整数

#include<iostream>
using namespace std;

int main(){
    /*
    int a = 'B' - 'A';
    int b = 'A' * 'B';
    char c = 'A' + 2;

    cout << a << endl;
    cout << b << endl;
    cout << c << endl;

    */
    // 输入一行字符，统计出其中数字字符的个数，以及字母字符的个数。
    char sym;
    int cnta = 0, cntb =0;
    while(cin >> sym, ((sym >= 65 && sym <= 90) || (sym >= 48 && sym <= 57)) || (sym >= 97 && sym <= 122))
    {
        if((sym >= 65 && sym <= 90) || (sym >= 97 && sym <= 122))
        {
            cnta++;
        }
        else
        {
            cntb++;
        }
    }

    cout << "Alpha: " << cnta << endl;
    cout << "Number: " << cntb << endl;

    return 0;

}