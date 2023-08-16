/*
87. 把字符串转换成整数

请你写一个函数 StrToInt，实现把字符串转换成整数这个功能。

当然，不能使用 atoi 或者其他类似的库函数。

数据范围
输入字符串长度 [0,20]。

样例
输入："123"

输出：123
注意:

你的函数应满足下列条件：

忽略所有行首空格，找到第一个非空格字符，可以是 ‘+/−’ 表示是正数或者负数，紧随其后找到最长的一串连续数字，将其解析成一个整数；
整数后可能有任意非数字字符，请将其忽略；
如果整数长度为 0，则返回 0；
如果整数大于 INT_MAX(231−1)，请返回 INT_MAX；如果整数小于INT_MIN(−231) ，请返回 INT_MIN；
*/

class Solution {
public:
    int strToInt(string str) {
        str += '\0';
        int pos = 0;
        long ret = 0;
        bool flag = true;
        while(str[pos] == ' ')  pos++;
        if(str[pos] == '+'){
            pos++;
        }else if(str[pos] == '-'){
            flag = false;
            pos++;
        }
        while(str[pos] >= '0' && str[pos] <= '9'){
            ret = ret * 10 + str[pos] - '0';
            pos++;
            if(flag && ret > INT_MAX)   return INT_MAX;
            else if(!flag && ret > INT_MIN - 1) return INT_MIN;
        }

        return flag? ret: -ret;
    }
};

/*
class Solution {
public:
    int strToInt(string s) {
        s += '\0';
        int i = 0;
        while(s[i] == ' ') ++i;
        long ret = 0;
        bool isPos = false;
        if(s[i] == '-' || s[i] == '+'){
            if(s[i] == '-') isPos = true;
            ++i;
        } 
        while(s[i] >= '0' && s[i] <= '9'){
            ret = ret * 10 + s[i] - '0';
            ++i;
            if(!isPos && ret >= INT32_MAX) return INT32_MAX;
            if(isPos && ret - 1 >= INT32_MAX) return INT32_MIN; 
        }
        return isPos ? -ret : ret;
    }
};

*/

/*
class Solution {
public:
    int strToInt(string str) {

        int k = 0;                                          
        long long f = 1;                             

        while(k < str.size() && str[k] == ' ') k ++;  

        if (k < str.size() && str[k] == '-') 
        {
            k ++;
            f = -1;
        }
        if (k < str.size() && str[k] == '+') k ++;

        long long r = 0;                             
        while (k < str.size() && str[k] <= '9' && str[k] >= '0')
        {
            r = r * 10 + f * (str[k] - '0');         
            if (r < INT_MIN) return INT_MIN;
            if (r > INT_MAX) return INT_MAX;
            k ++;
        }

        return (int)r;

    }
};

*/
