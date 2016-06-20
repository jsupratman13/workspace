//static in class means that no many how many object of the class is made, they share one copy
//static function becomes independent of object

#include <iostream>
using namespace std;

class Box
{
	public:
		static int objectCount;
		Box(double l=2.0, double w=2.0, double h=2.0);
		double Volume();
		static int getCount();
	
	private:
		double length;
		double width;
		double height;
};

int Box::objectCount = 0;

Box::Box(double l, double w, double h){
	cout << "constructor called" << endl;
	length = l;
	width = w;
	height = h;
	// increase each time object is called
	objectCount++;
}

double Box::Volume(){
	return length*width*height;
}

int Box::getCount(){
	return objectCount;
}

int main(){
	Box box1(3.3, 1.2, 1.5);
	Box box2(8.5, 6.0, 2.0);

	cout << "Total Objects: " <<  Box::objectCount << endl;
	cout << "total object from function view: " << Box::getCount() << endl;
}
