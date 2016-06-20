#include <iostream>
#include <ctime>
using namespace std;

//two ways to path array to function
//1
void myFunc1(int *param);

//2
void myFunc2(int param[]){
	cout << "array value inside function" << endl;
	for (int i=0; i<5; i++){
		cout << "balance["<<i<<"]: ";
		cout << param[i] << endl;
	}
}

//for function to return array it must be pointer

int *retFunc(){
	//need to be static variable
	static int r[3];
//	srand((unsigned)time(NULL));
	for (int i=0; i<3; i++){
//		r[3] = rand()/1000;
		r[i] = i;
		cout << r[i] << endl;
	}
	return r;
}

int main(){
	int balance[5] = {40, 0 ,3, 11, 5};
	int *p;

	p = balance;
	
	cout << "array value using pointer " << endl;
	for(int i=0; i < 5; i++){
		cout << "*(p+" << i << "): " ;
		cout << *(p+i) << endl;
	}

	cout << "array value using balance address" << endl;
	for(int i=0; i<5; i++){
		cout << "*(balance+" << i << "): ";
		cout << *(balance+i) << endl;
	}

	myFunc2(balance);

	cout << "array value from function" << endl;
	p = retFunc();
	for(int i=0;i<3;i++){
		cout << "*(p+" << i << "): ";
		cout << *(p+i) << endl;
	}

}
