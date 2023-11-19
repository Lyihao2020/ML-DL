#include<iostream>
using namespace std;
const int N =1000010;
 
class Person
{
	private:
		int age, height;
		double money;
		string books[100];
	
	public:
		string name;
	
		void say()
		{
			cout << "I'm " << name << endl;
		} 
		
		int getAge()
		{
			return age;
		}
		
		int setAge(int x)
		{
			age = x; 
		}
		
		void addMoney(double x)
		{
			money += x;
		}
}personA, personB, persons[100];

int main(){
	Person personC;
	
	personC.name = "yxc";
	// personC.age = 18;
	personC.setAge(18);
	personC.addMoney(100);
	
	personC.say();
	cout << personC.getAge() << endl;
	
	return 0;
	
}


