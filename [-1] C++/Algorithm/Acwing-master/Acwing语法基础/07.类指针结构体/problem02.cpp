

class Solution {
public:
    string replaceSpaces(string &str) {
        for(int i = 0; i < str.size(); i++){
        	if(str[i] == ' '){
        		str.erase(str.begin() + i);
        		str.insert(str.begin()) + i, "%20");
			}
		}
		return str;
    }
};



/*

class Solution {
public:
    string replaceSpaces(string &str) {
        string res;
        for (auto x : str)
            if (x == ' ')
                res += "%20";
            else
                res += x;
        return res;
    }
};


class Solution {
public:
    string replaceSpaces(string &str) {

        int len = 0;
        for (auto c : str)
            if (c == ' ')
                len += 3;
            else
                len ++ ;

        int i = str.size() - 1, j = len - 1;

        str.resize(len);

        while (i >= 0)
        {
            if (str[i] == ' ')
            {
                str[j -- ] = '0';
                str[j -- ] = '2';
                str[j -- ] = '%';
            }
            else str[j -- ] = str[i];
            i -- ;
        }
        return str;
    }
};

class Solution {
public:
    string replaceSpaces(string &str) {
        for (int i = 0; i < str.size(); i ++)
        {
            if (str[i] == ' ')
            {
                str.erase(str.begin() + i);
                str.insert(i, "%20");    
            }
        }
        return str;
    }
};

*/
