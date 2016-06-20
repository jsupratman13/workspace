//overload: for same function name in single class, function will be decided based on its given funcionality

#include <iostream>
using namespace std;

class printData{
	public:
		void print(int a){
			cout << "print number: " << a << endl;
		}
		void print(double a){
			cout << "print char: " << a << endl;
		}
		void print(char* a){
			cout << "print float: " << a << endl;
		}
};

int main(){
	printData pd;

	pd.print(5);
	pd.print("hello");
	pd.print(6.23);
}
