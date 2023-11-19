// 可变长的字符序列，比字符数组更加好用。需要引入头文件：
#include<cstring>
#include<iostream>

using namespace std;

int main(){

    string s1;  // 默认初始化， s1 为一个空字符串
    string s2 = s1;  // s2 是 s1 的副本
    string s3 = "hiya";  // s3 是该字符串字面值的副本
    string s4(10, 'c');  // s4的内容为 cccccccccc

    cin >> s1;
    // 使用getline读取一整行
    getline(cin, s2);
    cout << s2 << endl;
    // 注意：不能用printf直接输出string，需要写成：printf(“%s”, s.c_str());
    cout << s1 << " " << s2 << " " << s3 << " " << s4 << endl; 
    printf("%s\n", s1.c_str());

    // string的empty和size操作（注意size是无符号整数，因此 s.size() <= -1一定成立）

    cout << s2.empty() << endl; // 判断是否为空
    cout << s2.size() << endl;

    /*
        (4)	string 的比较：
            支持 > < >= <= == !=等所有比较操作，按字典序进行比较。

        (5)	为string对象赋值：

            string s1(10, ‘c’), s2;		// s1的内容是 cccccccccc；s2是一个空字符串
            s1 = s2;					// 赋值：用s2的副本替换s1的副本
							            // 此时s1和s2都是空字符串

        (6)	两个string对象相加：

            string s1 = “hello,  ”, s2 = “world\n”;
            string s3 = s1 + s2;					// s3的内容是 hello, world\n
            s1 += s2;								// s1 = s1 + s2

        (7)	字面值和string对象相加：
            做加法运算时，字面值和字符都会被转化成string对象，因此直接相加就是将这些字面值串联起来：

		    string s1 = “hello”, s2 = “world”;		// 在s1和s2中都没有标点符号
		    string s3 = s1 + “, “ + s2 + ‘\n’;
		
            当把string对象和字符字面值及字符串字面值混在一条语句中使用时，必须确保每个加法运算符的两侧的运算对象至少有一个是string：

            string s4 = s1 + “, “;	// 正确：把一个string对象和有一个字面值相加
            string s5 = “hello” +”, “; // 错误：两个运算对象都不是string

            string s6 = s1 + “, “ + “world”;  // 正确，每个加法运算都有一个运算符是string
            string s7 = “hello” + “, “ + s2;  // 错误：不能把字面值直接相加，运算是从左到右进行的

    */

    return 0;

}
