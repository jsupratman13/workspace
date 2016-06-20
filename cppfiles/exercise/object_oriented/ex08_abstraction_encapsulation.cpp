//Data abstraction: provide only essential information to oustside
//provide two advantages: prevent user leverl, implment may change without changing user-level
//seperate code to interface and implementation

//Data Encapsulation is a mechanism of bundling data and the functions that use them
//data Abstraction is a mechanism of exposing only the interfaces and hiding the implmentation details from the user

#include <iostream>
using namespace std;

class Adder{
	public:
		//constructor
		Adder(int i =0);

		//interface to outside world
		void addNum(int number);
		int getTotal();
	private:
		//hidden data from outside world
		int total;
};

Adder::Adder(int i){
	total = i;
}

void Adder::addNum(int number){
	total += number;
}

int Adder::getTotal(){
	return total;
}

int main(){
	Adder a;

	a.addNum(30);
	a.addNum(10);
	a.addNum(20);
	cout << "Total: "<< a.getTotal() << endl;
}
