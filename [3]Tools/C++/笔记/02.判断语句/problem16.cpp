// Acwing 661. 平均数3
/*
读取 4 个数字 N1,N2,N3,N4，这 4 个数字都是保留 1 位小数的浮点数，对应于学生获得的 4 个分数。

这 4 个分数的权重分别为 2,3,4,1，请你计算学生成绩的平均值 X 并输出 Media: X。

接下来分为以下三种情况：

如果平均值为 7.0 或更高，则输出 Aluno aprovado.。
如果平均值小于 5.0，则输出 Aluno reprovado.。
如果平均值大于等于 5.0 并且小于 7.0，则输出 Aluno em exame.，并再读取一个数字 Y，然后输出 Nota do exame: Y。接下来重新计算平均值 Z=(X+Y)/2，如果 Z 大于或等于 5.0，则输出 Aluno aprovado.，否则输出 Aluno reprovado.。最后输出 Media final: Z，表示学生的最终成绩。

输入格式
输入中包含四个浮点数，表示学生的四个成绩。

也有部分满足情况 3 的数据，多包含一个浮点数。

输出格式
输出的结果，具体形式参照题目描述和输出样例。

只要输出结果与答案的绝对误差不超过 0.1 即视为正确。

数据范围
0≤输入数据≤10.0
输入样例1：
2.0 4.0 7.5 8.0
6.4
输出样例1：
Media: 5.4
Aluno em exame.
Nota do exame: 6.4
Aluno aprovado.
Media final: 5.9
输入样例2：
2.0 6.6 4.0 9.0
输出样例2：
Media: 4.9
Aluno reprovado.
输入样例3：
9.0 4.0 8.5 9.0
输出样例3：
Media: 7.3
Aluno aprovado.
*/

#include<iostream>
#include<iomanip>
using namespace std;

int main(){
    double n1, n2, n3, n4, n5;
    cin >> n1 >> n2 >> n3 >> n4;
    double media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10;

    if (media >= 7)
    {
        cout << "Media: " << fixed << setprecision(1) << media << endl;
        cout << "Aluno aprovado." ;
    }
    else if (media < 5)
    {
        cout << "Media: " << fixed << setprecision(1) << media << endl;
        cout << "Aluno reprovado.";
    }
    else
    {
        cout << "Media: " << fixed << setprecision(1) << media << endl;
        cout << "Aluno em exame." << endl; 
        cin >> n5;
        cout << "Nota do exame: " << n5 << endl;
        media = (media + n5) / 2;
        if (media >= 5){
            cout << "Aluno aprovado." << endl;
        }
        else
        {
            cout << "Aluno reprovado." << endl;
        }
        cout << "Media final: " << fixed << setprecision(1) << media;
    }
    
    return 0;
}