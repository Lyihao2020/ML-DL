// Acwing 725. 完全数
/*
一个整数，除了本身以外的其他所有约数的和如果等于该数，那么我们就称这个整数为完全数。

例如，6 就是一个完全数，因为它的除了本身以外的其他约数的和为 1+2+3=6。

现在，给定你 N 个整数，请你依次判断这些数是否是完全数。

输入格式
第一行包含整数 N，表示共有 N 个测试用例。

接下来 N 行，每行包含一个需要你进行判断的整数 X。

输出格式
每个测试用例输出一个结果，每个结果占一行。

如果测试数据是完全数，则输出 X is perfect，其中 X 是测试数据。

如果测试数据不是完全数，则输出 X is not perfect，其中 X 是测试数据。

数据范围
1≤N≤100,
1≤X≤108
输入样例：
3
6
5
28
输出样例：
6 is perfect
5 is not perfect
28 is perfect
*/

#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        int temp, total = 1;
        cin >> temp;
        if(temp == 1)
        {
            cout << "1 is not perfect" << endl;
            continue;
        }
        for(int j = 2; j < sqrt(temp); j++){
            if(temp % j == 0){
                int num = temp / j;
                if(num == j)
                {
                    total += num;
                }
                else
                {
                    total += (num + j);
                }
            }
        }
        if(total == temp)
        {
            cout << temp << " is perfect" << endl;
        }
        else
        {
            cout << temp << " is not perfect" << endl;
        }
    }

    return 0;
}

/*
Actually
其实 100000000100000000 内的完全数没有几个

Good!
数学部分
100000000100000000 内的完全数有且仅有 6,28,496,8128,335503366,28,496,8128,33550336 这五个.
根据上述内容, 这道题可以直接 O(1)O(1) 解决.

完全数比较重要的几个性质
所有完全数都是三角形数
目前截止发现的所有完全数都以 66 或 2828 结尾
到现在为止,数学家们一共发现了 4848 个完全数,且 4848 个完全数全部是偶数
如果有人们没有找到的奇完全数,则它一定可以写成 12p+112p+1 或 36p+936p+9 的形式,而且 pp 是素数
奇完全数一定大于 1030010300
完全数的约数的倒数之和为调和数
完全数可以表示成连续奇数的立方和
完全数可以表示成 22 的连续自然数的次幂之和,且这些自然数的数量必定是素数
完全数计算法
若 2p−12p−1 是素数(亦称其为梅森素数),则 2p−1∗(2p−1)2p−1∗(2p−1) 是完全数.

同时，逆命题也是成立的：若aa为偶完全数，则存在αα，使得a=2α−1(2α−1)a=2α−1(2α−1)，其中2α−12α−1为素数
这个命题在初等数论中是极其好证的，因此留给读者作为练习

Code
#include <bits/stdc++.h>
using namespace std;

int main() {
    int tt;
    cin >> tt;
    while (tt--) {
        int n;
        cin >> n;
        if (n == 6 || n == 28 || n == 496 || n == 8128 || n == 33550336)  
            cout << n << " is perfect" << endl;
        else cout << n << " is not perfect" << endl;
    }

    return 0;
}
*/

/*
完全数c++解法
暴力解法直接超时 Time Limit Exceeded
下面进行分析优化
嘤嘤嘤,真想不到 在语法基础课里面还需要优化代码…
分析暴力解法时间复杂度===大O表示法
很明显外层n层for循环处理 n行数，内层x层for循环处理这个数的约数判断，那么时间复杂度即O(n^2)在这里就是O(n*x);
由题中数据范围可知，最大测试数据时间可达10的8次方*100 那就是100亿了 肯定超时了
优化着手处
外围的for循环 n 没办法优化了，铁定的循环100次，而且优化这里 对整体意义也不大；应该着手优化于内循环即10的8次方这里。内循环次数，由题意，可以知道是由输入的数值x决定的。暴力解法，最大值可取到10的8次方，看其循环意义，是求其约数，故而需要除以[1,x) 的每个值，判断其是否为约数，之后再将所有的约数给相加判断后续逻辑。但 x本身除以一个约数往往可以得到另外一个约数，如果在这里思考下手并优化，极有可能减少至少开根号的循环量
使用数学函数，sqrt 作为限制循环次数的条件，而另外一个约数则由输入数x除以当前的循环的约数，即可求得另一约数 注：此处需要考虑等于的情况，比如16 开根号是4 4也是约数 优化过后，复杂度为O(10^4*100) 100万 完全hold住
以后遇到此类题，诸如质数、完全数 等定义中带有约数、需要整除，优化方面皆可朝开平方处思考
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n,x,sum=0;
    cin >> n;
    for(int i=0;i<n;i++)
    {
        cin >> x;
        if(x==1) cout << x << " is not perfect" << endl;
        else
        {
            sum+=1;
            for(int j=2;j<=sqrt(x);j++) 
            {
                if(x%j==0)
                {
                    int y=x/j;
                    if(y==j) sum=sum+j;
                    else sum=sum+j+x/j;
                }
            }
            if(sum==x) cout << x << " is perfect" << endl;
            else cout << x << " is not perfect" << endl;
        }
        sum=0;
    }
    return 0;
}
*/