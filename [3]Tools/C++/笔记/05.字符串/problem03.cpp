// Acwing 763. 循环相克令
/*
循环相克令是一个两人玩的小游戏。

令词为“猎人、狗熊、枪”，两人同时说出令词，同时做出一个动作——猎人的动作是双手叉腰;狗熊的动作是双手搭在胸前;枪的动作是双手举起呈手枪状。

双方以此动作判定输赢，猎人赢枪、枪赢狗熊、狗熊赢猎人，动作相同则视为平局。

现在给定你一系列的动作组合，请你判断游戏结果。

输入格式
第一行包含整数 T，表示共有 T 组测试数据。

接下来 T 行，每行包含两个字符串，表示一局游戏中两人做出的动作，字符串为 Hunter, Bear, Gun 中的一个，这三个单词分别代表猎人，狗熊和枪。

输出格式
如果第一个玩家赢了，则输出 Player1。

如果第二个玩家赢了，则输出 Player2。

如果平局，则输出 Tie。

数据范围
1≤N≤100
输入样例
3
Hunter Gun
Bear Bear
Hunter Bear
输出样例
Player1
Tie
Player2
*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){

    int n;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        string s1, s2;
        cin >> s1 >> s2;
        if(s1 == s2)
        {
            cout << "Tie" << endl;
        }
        else if(s1[0] > s2[0])
        {
            if(s2[0] == 'B' && s1[0] == 'H')
            {
                cout << "Player2" << endl;
            }
            else
            {
                cout << "Player1" << endl;
            }
        }
        else
        {
            if(s1[0] == 'B' && s2[0] == 'H')
            {
                cout << "Player1" << endl;
            }
            else
            {
                cout << "Player2" << endl;
            } 
        }
    }

    return 0;

}

/*

#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;

    string x, y;
    while (n --)
    {
        cin >> x >> y;
        int a = x.size(), b = y.size();
        if (a - b == -1 || a - b == -2 || a - b == 3)
            cout << "Player1" << endl;
        else if (a == b)
            cout << "Tie" << endl;
        else cout << "Player2" << endl;
    }

    return 0;
}

*/