#include<iostream>
#include<cctype>
using namespace std;

int main(){

	char c;
	cin >> c;
	/*平时判断一个字符是否是字母
	if(c >= 'A' && c <= 'Z' || c >= 'a' && c <= 'z'){
		cout << " c is a Alpha.";
	}
	*/
	if(isalpha(c)){
		cout << " c is a Alpha." << endl;
	}
	
	if(islower(c)){
		cout << " c is a lower." << endl;
	}
	
	if(isupper(c)){
		cout << " c is a upper." << endl;
	}
	
	if(isalnum(c)){
		cout << " c is a Alnum." << endl;
	}
	
	if(isspace(c)){
		cout << " c is a space." << endl;
	}
	
	if(isblank(c)){
		cout << " c is a blank." << endl;
	}
	
	char t = tolower(c); 
	if(isalpha(c)){
		cout << t << " is a lower." << endl;
	}

	t = toupper(c); 
	if(isalpha(c)){
		cout << t << " is a upper." << endl;
	}

	

	return 0;
}