//extern give reference to global variable that is visible to ALL program files
//extern cannot be initialize as it just point variable name at a storage location that is define
//USEFUL for multiple files and reference global variable/function in other files

#include <iostream>
using namespace std;

int count;
extern void write_extern();

int main(){
	count = 5;
	write_extern();
}
