#include<bitset>
#include<iostream>
#include<cstdio>
using namespace std;

int main(){

	bitset<5> b("11");	//5表示5个二进制位
	// 初始化⽅式：
 	// bitset<5> b; 都为0
 	// bitset<5> b(u); u为unsigned int，如果u = 1,则被初始化为10000
 	// bitset<5> b(s); s为字符串，如"1101" -> "10110"
 	// bitset<5> b(s, pos, n); 从字符串的s[pos]开始，n位⻓度
 	for (int i = 0; i < 5; ++i)
 	{
 		cout << b[i];
 	}
 	cout << endl << b.any();	//b中是否存在1的二进制位
 	cout << endl << b.none();	//b中不存在1吗？
 	cout << endl << b.count();	//b中1的二进制位的个数
 	cout << endl << b.size();	//b中二进制位的个数
 	cout << endl << b.test(2);	//测试下标为2处是否二进制位为1
 	b.set(4);	//把b的下标为4处置1
 	b.reset();	//把所有位归零
 	b.reset(3);	//把b下标为3处置0
 	b.flip();	//b的所有二进制位逐步取反
 	unsigned long a = b.to_ulong();	//b转化为 unsigned long 类型

	return 0;

}