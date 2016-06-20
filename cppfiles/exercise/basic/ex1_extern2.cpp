//refer to ex11 for instruction
//compile as g++ ex1_extern.cpp ex1_externb.cpp
#include <iostream>
extern int count;

void write_extern(){
	std::cout << "Count is " << count << std::endl;
}
