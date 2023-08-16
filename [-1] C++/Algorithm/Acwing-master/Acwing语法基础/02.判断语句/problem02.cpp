// Acwing 660. 零食
/*
某商店出售 5 种零食，零食编号为 1∼5。

5 种零食的价目表如下所示：

零食种类        价格
零食  1         R$ 4.00
零食  2         R$ 4.50
零食  3         R$ 5.00
零食  4         R$ 2.00
零食  5         R$ 1.50
现在给定某种零食的编号和数量，请你计算总价值是多少。

输入格式
输入包含两个整数 x 和 y，其中 x 为零食编号，y 为零食数量。

输出格式
输出格式为 Total: R$ X，其中 X 为总价值，保留两位小数。

数据范围
1≤x≤5,
1≤y≤100
输入样例：
3 2
输出样例：
Total: R$ 10.00
*/

#include<iostream>
#include<iomanip>
using namespace std;

int main(){
    double ans[] = {4.00, 4.50, 5.00, 2.00, 1.50};
    int no, num;
    cin >> no >> num;

    cout << "Total: R$ " << fixed << setprecision(2) << ans[no - 1] * num << endl;

    return 0;
}