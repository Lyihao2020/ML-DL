/*
862. 三元组排序

给定 N 个三元组 (x,y,z)，其中 x 是整数，y 是浮点数，z 是字符串。

请你按照 x 从小到大的顺序将这些三元组打印出来。

数据保证不同三元组的 x 值互不相同。

输入格式
第一行包含整数 N。

接下来 N 行，每行包含一个整数 x，一个浮点数 y，一个字符串 z，表示一个三元组，三者之间用空格隔开。

输出格式
共 N 行，按照 x 从小到大的顺序，每行输出一个三元组。

注意，所有输入和输出的浮点数 y 均保留两位小数。

数据范围
1≤N≤10000,
1≤x,y≤105,
字符串总长度不超过 105。

输入样例：
5
32 1.36 nsyiupnnhc
18 4.53 fmofzwrah
33 4.86 wzuymbm
1 3.93 gtnrwcebt
31 4.53 gcllxioc
输出样例：
1 3.93 gtnrwcebt
18 4.53 fmofzwrah
31 4.53 gcllxioc
32 1.36 nsyiupnnhc
33 4.86 wzuymbm
*/

#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>

using namespace std;

typedef pair<int, pair<double, string>> mp;
vector<mp> array;

int main(){
    int n, temp;
    double f, string str;
    
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> temp >> f >> str;
        array
    }

}

/*
Note:
printf函数输出字符串是针对char *的，即printf只能输出c语言的内置数据类型，而string不是c语言的内置数据类型。如需输出string对象中的字符串，可以使用string的成员函数c_str()，该函数返回字符串的首字符的地址。

map 正向迭代器

map<int, PII>::iterator iter; //迭代器
for (iter = ans.begin(); iter != ans.end(); iter ++ ){}
4. STL:vector 这里用了pair<int, pair<double, string >> 嵌套pair构成三元组
#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>

#define x first
#define y second

using namespace std;

const int N = 10010;

typedef pair<int, pair<double, string >> PII;

vector<PII> ans;
int n, a;
double b;
string s;

int main()
{
    cin >> n;
    for (int i = 0; i < n; i ++ )
    {
        cin >> a >> b >> s;
        ans.push_back({a, {b, s}});
    }

    sort(ans.begin(), ans.end());

    for (auto i: ans)
        printf("%d %.2lf %s\n",i.x, i.y.x, i.y.y.c_str());   

    return 0;
}
3. STL:map
#include<iostream>
#include<cstring>
#include<cstdio>
#include<map>

#define x first
#define y second

using namespace std;

const int N = 10010;

typedef pair<double, string> PII;
map<int, PII> ans;

int n;

int main()
{
    int a;
    double b;
    string c;
    cin >> n;

    for (int i = 0; i < n; i ++ )
    {
        cin >> a >> b >> c;
        ans.insert({a, {b, c}});
    }

    for (auto i : ans)
        printf("%d %.2f %s\n", i.x, i.y.x, i.y.y.c_str());

    return 0;
}

2.stl:map 不用auto的写法 (蓝桥杯不让写auto)
#include<iostream>
#include<cstring>
#include<cstdio>
#include<map>

#define x first
#define y second

using namespace std;

const int N = 10010;

typedef pair<double, string> PII;
map<int, PII> ans;

int n;

int main()
{
    int a;
    double b;
    string c;
    cin >> n;

    for (int i = 0; i < n; i ++ )
    {
        cin >> a >> b >> c;
        ans.insert({a, {b, c}});
    }

    // 不用auto的写法 (蓝桥杯不让写auto)
    // map<int, PII>::iterator iter; 迭代器
    for (map<int, PII>::iterator iter = ans.begin(); iter != ans.end(); iter ++ )
        printf("%d %.2f %s\n", iter->x, iter->y.x, iter->y.y.c_str());  //这里 iter -> x/y 是map ，后面两个是pair ：PII.first/second

    return 0;
}
1.写结构体的普通做法
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>

using namespace std;

const int N = 10010;

int n;

struct three
{
    int a;
    double b;
    string c;
};

three th[N];

bool comp(three x, three y)
{
    return x.a < y.a;
}

int main()
{

    cin >> n;
    for (int i = 0; i < n; i ++ )
        cin >> th[i].a >> th[i].b >> th[i].c;

    sort(th, th + n, comp);

    for (int i = 0; i < n; i ++ )
    {
        printf("%d %.2f %s\n", th[i].a, th[i].b, th[i].c.c_str());
    }

    return 0;
}

*/
/*
算法1
STL pair扩展为三元组

const int N = 10010;
typedef pair <int, pair<double, string> > PII;

PII a[N]; ** //声明pair数组**

int main()
{
    int n;
    scanf("%d",&n);
     for(int i=0;i<n;i++)
     cin>>a[i].first>>a[i].second.first>>a[i].second.second;
     

     sort(a,a+n);  

   for(int i=0;i<n;i++)
   {
   printf("%d %.2lf %s\n",a[i].first,a[i].second.first,a[i].second.second.c_str());

   }
   return 0;

}
算法2
结构体

struct Node
{
    int x;
    double y;
    string z;
}no[N];

bool cmp(Node a ,Node b)
{
    return a.x<b.x;
}     

int main()
{
    int n;
    scanf("%d",&n);
     for(int i=0;i<n;i++)
  cin>>no[i].x>>no[i].y>>no[i].z;
  sort(no,no+n,cmp);
     for(int i=0;i<n;i++)
   {
 printf("%d %.2lf %s\n",no[i].x,no[i].y,no[i].z.c_str());
   }
   return 0;

}
*/