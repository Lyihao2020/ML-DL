# 使用C++刷算法题的简明教程

[toc]

## 1.使用C++刷算法的好处

* 在具备C语言的前提下，学习C++并使用它刷算法题的学习成本非常低，只需要几个小时
* C++向下兼容C，C语言里的语法大部分都可以在C++文件中运行，所以学习C++对刷算法时编程语言的表达能力进行扩充有益无害，例如C语言的输入输出( `scanf`和 `printf` )比C++快，那么就可以在使用C++刷算法同时使用 scanf 和 printf 提高代码运行效率
* C++拥有丰富的STL标准库，这也是PAT、LeetCode等题目中经常需要用到的，单纯使用C语言解决问题会比使用C++的STL库解决问题麻烦很多
* C++的string非常好用，比C语言里面得到char数组好用很多
* 在解决一些较为简单的PAT乙级题目的时候( 例如一些时间复杂度限制不严格 )，cin、cout输入输出非常方便

## 2. 名称空间using namespace std的解释

这句话是使用“std”这个名称空间（namespace）的意思，因为有的时候不同⼚商定义的函数名称彼此之间可能会重复，为了避免冲突，就将所有的函数都封装在各⾃的名称空间里面，使⽤这个函数的时候就在main函数前⾯写明⽤了什么名称空间，几乎在C++中使⽤到的⼀些⽅法如 `cin、cout`都是在std名称空间里面的，所以可以看到 `using namespace std;`这句话几乎成了我每段C++代码的标配，就和return 0; ⼀样必须有。其实也可以不写这句话，但是使⽤std里面的方法的时候就会麻烦点，要写成这样：

```cpp
#include<iostream>
int main ()
{
	int n;
	std::cin>>n;
	std::cout<<"hello ,xuyuanzhi"<<n+1<< std::endl;
	return 0;
}
12345678
```

## 3. cin和cout输入输出

就如同 scanf 和 printf 在 stdio.h 头文件中⼀样，cin 和 cout 在头文件 iostream 里面，看名字就知道，io 是输⼊输出 input和 output的首字母，stream是流，所以这个iostream头文件⾥包含的方法就是管理⼀些输⼊输出流的 cin 和 cout 比较⽅便，不⽤像C语言⾥的scanf、printf 那样写得那样繁琐， `cin >> n`; 和 `scanf("%d", &n)`; 是⼀样的意思，注意cin是向右的箭头，表示将内容输⼊到n中，同样， `cout << n;` 和 `printf("%d", n);`⼀样的意思，此时 cout 是向左的两个箭头，注意和 cin 区分开来。⽽且不管n是 double 还是 int 或者是 char 类型，只⽤写 cin >> n; 和 cout << n; 这样简单的语句就好，不用像C语言中需要根据n的类型对应地写%lf、%d、%c这样麻烦，endl 和 “\n” 是⼀个意思，⼀般如果前⾯是个字符串引号的话直接 “\n” 比较⽅便。
例如：

```cpp
cout << "hello, ⼩可爱\n";
cout << n << endl;
12
```

cin 和 cout 虽然使用起来更⽅便，但是输⼊输出的效率不如 scanf 和 printf 快，如果发现有题目超时了，可以换成 scanf 和 printf 再试一下

## 4. 关于C++的头文件

C++的头文件⼀般是没有像C语⾔的.h这样的扩展后缀的，⼀般情况下C语言里面的头文件去掉.h，然后在前面加个c就可以继续在C++⽂件中使用c语言头文件中的函数啦
比如：

```cpp
#include <cmath> // 相当于C语⾔⾥⾯的#include <math.h>
#include <cstdio> // 相当于C语⾔⾥⾯的#include <stdio.h>
#include <cctype> // 相当于C语⾔⾥⾯的#include <ctype.h>
#include <cstring> // 相当于C语⾔⾥⾯的#include <string.h>
1234
```

## 5. C++的变量声明

C语言的变量声明⼀般都在函数的开头，但是C++在首次使⽤变量之前声明即可（当然也可以都放在函数的开头），而且⼀般C语言里面会在for循环的外⾯定义i变量，但是C++里面可以在for循环内部定义，而且在for循环里面定义的局部变量，在循环外面就失效啦（就是脱离这个局部作⽤域就会查⽆此变量的意思），所以⼀个main函数里面可以定义好多次局部变量i，再也不⽤担心写的循环太多变量名i、j、k不够⽤啦

```cpp
#include<iostream>
using namespace std;
int main(){
	int n;
	cin>>n;
	cout<<"hello,xuyuanzhi"<<n+1<<endl;
	int m;
	cin>>m;
	for(int i=0;i<n;i++){ //这个i只在for循环里面有用，出了这个for循环就失效了
	  cout<<i;	   
	}
	cout<<endl;
	for(int i=0;i<m;i++){
		cout<<i+2;
	}
	return 0;
}
1234567891011121314151617
```

## 6. C++特有的bool变量

bool变量有两个值，false 和 true，以前⽤C语言的时候都是用 int 的0和1表示 false 和 true 的，现在C++里面引⼊了这个叫做 bool（布尔）的变量，⽽且C++把所有非零值解释为 true，零值解释为false，所以直接赋值⼀个数字给bool变量也是可以的，它会自动根据int值是不是零来决定给 bool 变量赋值 true 还是 false。

```cpp
bool flag = true;
bool flag2 = -2; // flag2为true
bool flag3 = 0; // flag3为false
123
```

## 7. C++特有的const定义常量

```cpp
const int a = 99999999;
1
```

## 8. C++里面超好用的string类

以前C语言中⽤char[]的⽅式处理字符串很繁琐，现在有了string类，定义、拼接、输出、处理都更加简单啦。
不过 **string只能⽤ cin 和 cout 处理，无法用 scanf 和 printf 处理** ：

```cpp
string08.cpp
```

```cpp
#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main(){

	string s = "Hello C++"; //赋值C++
	string s1 = s;
	string s2 = s1 + s;
	string s3;
	cin >> s3;	//读入字符串
	cout << s << endl << s1 << endl << s2 << endl << s3;	//输出字符串

	string s4 = s3;	//定义一个空字符串
	//⽤cin读⼊字符串的时候，是以空格为分隔符的
	//getline(cin, s4);	//读取一行字符串，包括空格
	cout << endl << s4 << endl << s4.length();	//输出s4和s4的长度

	string s5 = s4.substr(4);	//表示从下标4到结束
	string s6 = s4.substr(4, 3); 	//表示从下标4开始，3个字符
	cout << endl << s5 << endl << s6;

	return 0;
}
```

⽤cin读⼊字符串的时候，是以空格为分隔符的，如果想要读⼊⼀整⾏的字符串，就需要⽤[getline](https://so.csdn.net/so/search?q=getline&spm=1001.2101.3001.7020)，s的长度可以⽤s.length()获取（有几个字符就是⻓度多少，不存在char[]里面的什么末尾的结束符之类的）

```cpp
   string s;//定义一个空字符串s 
   getline(cin,s);//读取一行的字符串，包括空格 
   cout<<s<<endl;
   cout<<s.length();//输出字符串s的长度 
   return 0;
12345
```

string中还有个很常⽤的函数叫做substr，作⽤是截取某个字符串中的⼦串，用法有两种形式：

```cpp
string s2 = s.substr(4); // 表示从下标4开始⼀直到结束
string s3 = s.substr(5, 3); // 表示从下标5开始，3个字符
12
```

## 9. C++的结构体struct和C语言结构体的区别

定义好结构体stu之后，使⽤这个结构体类型的时候，C语⾔需要写关键字struct，⽽C++⾥⾯可以省略
不写：

```cpp
struct stu {
 int grade;
 float score;
};
struct stu arr1[10]; // C语⾔⾥⾯需要写struct
stu arr2[10];// C++⾥⾯不⽤写
123456
```

这个引⽤符号&要和C语⾔⾥⾯的取地址运算符&区分开来，他们没有什么关系，C++里面的引⽤是指在变量名之前加⼀个&符号，⽐如在函数传⼊的参数中int &a，那么对这个引⽤变量a做的所有操作都是直接对传入的原变量进⾏的操作，并没有像原来int a⼀样只是拷⻉⼀个副本（传值），举两个例子：

```cpp
void func(int &a) { // 传⼊的是n的引⽤，相当于直接对n进⾏了操作，只不过在func函数中换了个名字叫a
 a = 99;
}
int main() {
 int n = 0;
 func(n); // n由0变成了99
}
1234567
```

```cpp
void func(int a) {// 传⼊的是0这个值，并不会改变main函数中n的值
 a = 99;
}
int main() {
 int n = 0;
 func(n);// 并不会改变n的值，n还是0
}
1234567
```

## 10. C++ STL之动态数组vector的使用

之前C语言里面用int arr[][定义数组](https://so.csdn.net/so/search?q=%E5%AE%9A%E4%B9%89%E6%95%B0%E7%BB%84&spm=1001.2101.3001.7020)，它的缺点是数组的长度不能随心所欲的改变，⽽C++⾥⾯有⼀个能完全替代数组的动态数组vector，它能够在运行阶段设置数组的长度、在末尾增加新的数据、在中间插⼊新的值、长度任意被改变，很好用，它在头文件 `# include <vector>`⾥⾯，也在命名空间std⾥⾯，所以使用的时候要引入头文件vector和using namespace std; vector、stack、queue、map、set这些在C++中都叫做容器，这些容器的大小都可以⽤ .size() 取到，就像string s的长度⽤ s.length() 获取⼀样（string其实也可以⽤ s.size() ，不过对于vector、stack、queue、map、set这样的容器我们⼀般讨论它的大小size，字符串⼀般讨论它的长度length，其实string⾥⾯的size和length两者是没有区别、可以互换使⽤的。

```cpp
#include<iostream>
#include<vector>
using namespace std;
int main(){
	vector<int> v1;//定义一个vector v1,定义的时候没有分配大小 
	cout<<v1.size();//输出vector v1的大小，此处应该为0 
	return 0;
}
12345678
```

vector可以⼀开始不定义大小，之后⽤resize分配大小，也可以⼀开始就定义大小，之后还可以对它插入删除动态改变它的大小，⽽且不管在main函数⾥还是在全局中定义，它都能够直接将所有的值初始化为0（不⽤显式地写出来，默认就是所有的元素为0），再也不⽤担心C语⾔⾥⾯出现的那种int arr[10]; 结果忘记初始化为0导致的各种bug啦。

```cpp
vector<int> v(10); // 直接定义⻓度为10的int数组，默认这10个元素值都为0
// 或者
vector<int> v1;
v1.resize(8); //先定义⼀个vector变量v1，然后将⻓度resize为8，默认这8个元素都是0
// 在定义的时候就可以对vector变量进⾏初始化
vector<int> v3(100, 9);// 把100⻓度的数组中所有的值都初始化为9
// 访问的时候像数组⼀样直接⽤[]下标访问即可(也可以⽤迭代器访问，下⾯会讲)
v[1] = 2;
cout << v[0];
123456789
```

不管是vector、stack、queue、map还是set都有很多好用的方法，这些方法都可以在 [官方网站](http://www.cplusplus.com/) 中直接查询官方文档，上面有方法的讲解和代码示例，官方文档是刷题时候必不可少的好伙伴，比如进⼊官网搜索 vector ，就会出现vector拥有的所有方法，点进去⼀个⽅法就能看到这个方法的详细解释和代码示例。当然我们平时写算法用不到那么多方法啦，只有几个是常用的，以下是⼀些常⽤的vector方法：

```cpp
#include <iostream>
#include <vector>
using namespace std;
int main() {
	vector<int> a; // 定义的时候不指定vector的大小
	cout << a.size() << endl; // 这个时候size是0
	for (int i = 0; i < 10; i++) {
		a.push_back(i); // 在vector a的末尾添加元素i
	}
	cout << a.size() << endl; // 此时会发现a的size变成了10
	vector<int> b(15); // 定义的时候指定vector的大小，默认b元素都是0
	cout << b.size() << endl;
	for (int i = 0; i < b.size(); i++) {
		b[i] = 15;
	}
	for (int i = 0; i < b.size(); i++) {
		cout << b[i] << " ";
	}
	cout << endl;
	vector<int> c(20, 2); // 定义的时候指定vector的大小并把所有的元素赋一个指定的值
	for (int i = 0; i < c.size(); i++) {
		cout << c[i] << " ";
	}
	cout << endl;
	for (auto it = c.begin(); it != c.end(); it++) { // 使用迭代器访问vector
		cout << *it << " ";
	}
	return 0;
}
1234567891011121314151617181920212223242526272829
```

容器vector、set、map这些遍历的时候都是使⽤迭代器访问的， **c.begin()是⼀个指针，指向容器的第⼀个元素，c.end()指向容器的最后⼀个元素的后⼀个位置** ，所以迭代器指针it的for循环判断条件是it != c.end() ，访问元素的值要对it指针取值，要在前⾯加星号，所以是cout << *it;  **这⾥的auto相当于 vector::iterator 的简写** ，关于auto下⽂有讲解

## 11. C++ STL之集合set的使用

set是集合，在头文件 `#include<set>`里，⼀个set里面的各元素是各不相同的，而且 **set会按照元素进⾏从⼩到⼤排序** ，以下是set的常用用法：

```cpp
#include<iostream>
#include<set>
using namespace std;
int main(){
	set<int> s;//定义一个空集合s
	s.insert(1);//向集合里面插入一个1； 
	cout<<*(s.begin())<<endl;//输出集合s的第一个元素（前面的星号表示要对指针取值）
    for(int i=0;i<6;i++){
    	s.insert(i);//向集合s里面插入i 
  
	}
	for(auto it=s.begin();it!=s.end();it++){//用迭代器遍历集合s里面的每一个元素
	  cout<<*it<<" "; 

	}
	cout<<endl<<(s.find(2)!=s.end())<<endl;//查找集合s中的值，如果结果等于s.end()表示未找到（因为s.end()表示s的最后一个元素的下一个元素所在的位置）
	cout << (s.find(10) != s.end()) << endl; // s.find(10) != s.end()表示能找到10这个元素
	s.erase(1); // 删除集合s中的1这个元素
    cout << (s.find(1) != s.end()) << endl; // 这时候元素1就应该找不到啦
	return 0; 
}
123456789101112131415161718192021
```

## 12. C++ STL之映射map的使用

map在头文件 `#include<map>`中，map是键值对，比如⼀个人名对应⼀个学号，就可以定义⼀个字符串string类型的人名为“键”，学号int类型为“值”，如 map<string, int> m; 当然键、值也可以是其它变量类型， **map会⾃动将所有的键值对按照键从小到大排序** ，以下是map中常用的方法：

```cpp
#include<iostream>
#include<map>
#include<string>
using namespace std;
int main(){
	map<string,int> m;//定义一个空的map m,键是string类型的,值是int类型的
	m["hello"] = 2; // 将key为"hello", value为2的键值对(key-value)存入map中
	cout << m["hello"] << endl; // 访问map中key为"hello"的value, 如果key不存在，则返回0
	cout << m["world"] << endl;
    m["world"] = 3; // 将"world"键对应的值修改为3
    m[","] = 1; // 设立一组键值对，键为"," 值为1
    //用迭代器遍历，输出map中所有的元素，键：it->first获取，值：it->second获取
    for (auto it = m.begin(); it != m.end(); it++) {
         cout << it->first << " " << it->second << endl;
    }
    // 访问map的第一个元素，输出它的键和值
     cout << m.begin()->first << " " << m.begin()->second << endl;
    // 访问map的最后一个元素，输出它的键和值
     cout << m.rbegin()->first << " " << m.rbegin()->second << endl;
     // 输出map的元素个数
     cout << m.size() << endl;
     return 0;
}
1234567891011121314151617181920212223
```

## 13. C++ STL之stack的使用

栈stack在头⽂件 `#include<stack>`中，是数据结构⾥⾯的栈，以下是常用用法：

```cpp
#include <iostream>
#include <stack>
using namespace std;
int main() {
 stack<int> s; // 定义⼀个空栈s
 for (int i = 0; i < 6; i++) {
 s.push(i); // 入栈 将元素i压⼊栈s中
 }
 cout << s.top() << endl; // 访问s的栈顶元素
 cout << s.size() << endl; // 输出s的元素个数
 s.pop(); // 出栈 移除栈顶元素
 return 0;
}
12345678910111213
```

## 14. C++ STL之队列queue的使用

队列queue在头文件 `#include<queue>`中，是数据结构里⾯的队列，以下是常用用法：

```cpp
#include <iostream>
#include <queue>
using namespace std;
int main() {
 queue<int> q; // 定义⼀个空队列q
 for (int i = 0; i < 6; i++) {
 q.push(i); //入队 将i的值依次压⼊队列q中
 }
 cout << q.front() << " " << q.back() << endl; // 访问队列的队⾸元素和队尾元素
 cout << q.size() << endl; // 输出队列的元素个数
 q.pop(); // 出队 移除队列的队⾸元素
 return 0;
}
12345678910111213
```

## 15. C++ STL之unordered_map和unordered_set的使用

unordered_map在头文件 `#include<unordered_map>` 中，unordered_set在头文件 `#include<unordered_set>`中unordered_map和map（或者unordered_set和set）的区别是：map会按照键值对的键key进行排序（set里面会按照集合中的元素大小进⾏排序，从小到大顺序），而unordered_map（或者 unordered_set）省去了这个排序的过程，如果偶尔刷题时候用map或者set超时了，可以考虑用 unordered_map（或者unordered_set）缩短代码运行时间、提⾼代码效率，至于用法和map、set是⼀样的

## 16. C++的位运算bitset

bitset⽤来处理⼆进制位非常⽅便。头文件是 `#include<bitset>` ，bitset可能在PAT、蓝桥OJ中不常用，但是在LeetCode OJ中经常用到,而且知道bitset能够简化⼀些操作，可能⼀些复杂的问题能够直接用bitset就很轻易地解决，以下是⼀些常用用法：

```cpp
#include <iostream>
#include <bitset>
using namespace std;
int main() {
 bitset<5> b("11"); //5表示5个⼆进位
 // 初始化⽅式：
 // bitset<5> b; 都为0
 // bitset<5> b(u); u为unsigned int，如果u = 1,则被初始化为10000
 // bitset<5> b(s); s为字符串，如"1101" -> "10110"
 // bitset<5> b(s, pos, n); 从字符串的s[pos]开始，n位⻓度
 for(int i = 0; i < 5; i++)
 cout << b[i];
 cout << endl << b.any(); //b中是否存在1的⼆进制位
 cout << endl << b.none(); //b中不存在1吗？
 cout << endl << b.count(); //b中1的⼆进制位的个数
 cout << endl << b.size(); //b中⼆进制位的个数
 cout << endl << b.test(2); //测试下标为2处是否⼆进制位为1
 b.set(4); //把b的下标为4处置1
 b.reset(); //所有位归零
 b.reset(3); //b的下标3处归零
 b.flip(); //b的所有⼆进制位逐位取反
 unsigned long a = b.to_ulong(); //b转换为unsigned long类型
 return 0;
}
123456789101112131415161718192021222324
```

## 17. C++中的sort函数

sort函数在头文件 `#include<algorithm>` ⾥⾯，主要是对数组进行排序（int arr[]数组或者vector数组都行）， **vector是容器，要⽤v.begin()和v.end()表示头尾** ；而int arr[]用**arr表示数组的首地址，arr+n表示尾部**

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
bool cmp(int a, int b) { // cmp函数返回的值是bool类型
 return a > b; // 从⼤到⼩排列
}
int main() {
 vector<int> v(10);
 for (int i = 0; i < 10; i++) {
 cin >> v[i];
 }
 sort(v.begin(), v.end());// 因为这⾥没有传⼊参数cmp，所以按照默认，v从⼩到⼤排列

 int arr[10];
 for (int i = 0; i < 10; i++) {
 cin >> arr[i];
 }
  sort(arr, arr + 10, cmp); // arr从⼤到⼩排列，因为cmp函数排序规则设置了从⼤到⼩
 return 0;
}
123456789101112131415161718192021
```

 **注意** ：sort函数的cmp必须按照规定来写，即必须只是 > 或者 <= ，比如:return a > b;或者return a < b;⽽不能是 <= 或者 >= ，（实际上等于号加了也是毫⽆意义，sort是不稳定的排序），否则可能会出现段错误

## 18. C++中使用sort自定义cmp函数

`sort`默认是从小到⼤排列的，也可以指定第三个参数cmp函数，然后自己定义⼀个cmp函数指定排序规则。cmp最好⽤的还是在结构体中，尤其是很多排序的题⽬，比如⼀个学⽣结构体stu有学号和成绩两个变量，要求如果成绩不同就按照成绩从大到小排列，如果成绩相同就按照学号从小到大排列，那么就可以写⼀个cmp数组实现这个看上去有点复杂的排序过程：

```cpp
#include <iostream>
using namespace std;
struct stu { // 定义⼀个结构体stu，number表示学号，score表示分数
 int number;
 int score;
}
bool cmp(stu a, stu b) { // cmp函数，返回值是bool，传⼊的参数类型应该是结构体stu类型
 if (a.score != b.score) // 如果学⽣分数不同，就按照分数从⼤到⼩排列
 	return a.score > b.score;
 else // 如果学⽣分数相同，就按照学号从⼩到⼤排列
 	return a.number < b.number;
}

bool cmp(stu a, stu b) {
 return a.score != b.score ? a.score > b.score : a.number < b.number;
}
12345678910111213141516
```

## 19. 关于cctype头文件里的一些函数

刚刚在头文件那⼀段中也提到，cctype本质上是C语⾔标准函数库中的头文件 `#include<ctype.h>` ，其实并不属于C++新特性的范畴，在刷PAT⼀些字符串逻辑题的时候也经常⽤到，但是很多⼈似乎不了解这个头文件中的函数，所以在这⾥单独提⼀下，可能平时我们判断⼀个字符是否是字母，可能会写：

```cpp
char c;
cin >> c;
if (c >= 'A' && c <= 'Z' || c >= 'a' && c <= 'z') {
 cout << "c is alpha";
}
12345
```

但是在cctype中已经定义好了判断这些字符应该所属的范围，直接引⼊这个头文件并且使用里面的函数判断即可，无需自己手写（自己手写有时候可能写错或者漏写）

```cpp
#include <iostream>
#include <cctype>
using namespace std;
int main() {
 char c;
 cin >> c;
 if (isalpha(c)) {
 cout << "c is alpha";
 }
 return 0;
}
1234567891011
```

 **常用方法** ：

* isalpha 字母（包括大写、小写）
* islower（小写字母）
* isupper（大写字母）
* isalnum（字母大写小写+数字）
* isblank（space和\t）
* isspace（space、\t、\r、\n）
* cctype中

除了上面所说的用来判断某个字符是否是某种类型，还有两个经常用到的函数：tolower和toupper，作⽤是将某个字符转为小写或者大写，这样就不⽤像原来那样⼿动判断字符c是否是大写，如果是大写字符就 c = c + 32; 的方法将c转为小写字符啦,这在字符串处理的题⽬中也是经常用到：

```cpp
char c = 'A';
char t = tolower(c); // 将c字符转化为⼩写字符赋值给t，如果c本身就是⼩写字符也没有关系
cout << t; // 此处t为'a'
123
```

## 20. 关于C++11的解释

C++11是2011年官⽅为C++语⾔带来的新语法新标准，C++11为C++语⾔带来了很多好⽤的新特性，比如auto、to_string()函数、stoi、stof、unordered_map、unordered_set之类的，现在⼤多数OJ都是⽀持C++11语法的，有些编译器在使用的时候需要进行⼀些设置才能使⽤C++11中的语法，否则可能会导致编译器上编译不通过无法运行，比如我曾经写过⼀篇博客《如何在Dev-Cpp中使⽤C++11中的函数》（在本教程末尾）这个是针对DEV-cpp编译器的，其他的编译器如果发现不支持也可以百度搜索⼀下让编译器支持C++11的⽅法。总之C++11的语法在OJ里面是可以使⽤的，⽽且很多语法很好⽤，以下讲解⼀些C++11⾥⾯常⽤的新特性

## 21. C++11里面很好用的auto声明

C++11里面很好用的auto声明

```cpp
auto x = 100; // x是int变量
auto y = 1.5; // y是double变量
12
```

当然这个在算法里面最主要的用处不是这个，而是 **在STL中使⽤迭代器的时候，auto可以代替一大长串的迭代器类型声明** ：

```cpp
// 本来set的迭代器遍历要这样写：
for(set<int>::iterator it = s.begin(); it != s.end(); it++) {
 cout << *it << " ";
}
// 现在可以直接替换成这样的写法：
for(auto it = s.begin(); it != s.end(); it++) {
 cout << *it << " ";
}
12345678
```

## 22. C++11特性中的to_string

to_string的头文件是 `#include <string>` ，to_string最常用的就是把⼀个int型变量或者⼀个数字转化为string类型的变量，当然也可以转double、float等类型的变量，这在很多PAT字符串处理的题目中很有用处，以下是示例代码：

```cpp
#include <iostream>
#include <string>
using namespace std;
int main() {
 string s1 = to_string(123); // 将123这个数字转成字符串
 cout << s1 << endl;
 string s2 = to_string(4.5); // 将4.5这个数字转成字符串
 cout << s2 << endl;
 cout << s1 + s2 << endl; // 将s1和s2两个字符串拼接起来并输出
 printf("%s\n", (s1 + s2).c_str()); // 如果想⽤printf输出string，得加⼀个.c_str()
 return 0;
}
123456789101112
```

## 23. C++11特性中的stoi、stod

使用stoi(string to int)、stod(string to double)可以将字符串string转化为对应的int型、double型变量，这在字符串处理的很多问题中很有帮助，以下是示例代码和非法输⼊的处理⽅法：

```cpp
#include <iostream>
#include <string>
using namespace std;
int main() {
 string str = "123";
 int a = stoi(str);
 cout << a;
 str = "123.44";
 double b = stod(str);
 cout << b;
 return 0;
}
123456789101112
```

stoi如果遇到的是非法输⼊（⽐如stoi(“123.4”)，123.4不是⼀个int型变量）：

1. 会自动截取最前面的数字，直到遇到不是数字为止(所以说如果是浮点型，会截取前⾯的整数部分)
2. 如果最前面不是数字，会运行时发⽣错误

stod如果遇到的是非法输⼊：

1. 会⾃动截取最前面的浮点数，直到遇到不满足浮点数为止
2. 如果最前面不是数字或者小数点，会运行时发⽣错误
3. 如果最前面是小数点，会自动转化后在前⾯补0

不仅有stoi、stod两种，相应的还有：

* stof (string to float)
* stold (string to long double)
* stol (string to long)
* stoll (string to long long)
* stoul (string to unsigned long)
* stoull (string to unsigned long long)

## 24. 如何在Dev-Cpp中使用C++11中的函数

如果想要在Dev-Cpp⾥⾯使⽤C++11特性的函数，⽐如刷算法中常⽤的stoi、to_string、unordered_map、unordered_set、auto这些，需要在设置里面让dev⽀持c++11，需要这样做：在⼯具-编译选项-编译器-编译时加⼊这个命令“-std=c++11”即可

## 25. Cpp中保留小数的实现

头文件

```cpp
#include<iomanip>
1
```

格式

```cpp
cout<<fixed<<setprecision(3)<<num<<endl;
```
