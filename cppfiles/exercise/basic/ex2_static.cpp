//static tells compiler to keep local variable in existance instead of creating/destroying them each time it is called for global variable, it causes variable scope to be restricted to the file in which it is declared
//USEFUL for keeping saving local variable for repeatition etc
// : is inline function

#include <iostream>
using namespace std;

void func(void);
static int count = 10;
int x;
string str;

void func(){
	static int i = 5;
	i++;
	cout << "i is " << i;
	cout << " and count is " << count << endl;
	x = (i > 10) ? 0:1; // z?x:y if z is true use x else y
	cout << "x is " << x << endl;
}

int main(){
	while(count--){
		func();
	}
	str = "string function";
	if (str == "string function"){
		cout << str << endl;
	}
	return 0;
}
