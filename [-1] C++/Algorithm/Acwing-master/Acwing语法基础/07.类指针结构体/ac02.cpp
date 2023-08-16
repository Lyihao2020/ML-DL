#include<iostream>
using namespace std;

struct Person
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
		
		void setAge(int a)
		{
			age = a;
		}
		
		int getAge()
		{
			return age;
		}
		
		void addMoney(double x)
		{
			money += x;
		}
}personA, personB, persons[100];


