//this pointer is an implicit paramter to all member
//allow access to member inside the object
//pointer is called using ->

#include <iostream>
using namespace std;

class Box{
	public:
		//constructor
		Box(double l=2.0, double w=2.0, double h=2.0){
			cout << "constructor called" << endl;
			length = l;
			width = w;
			height = h;
		}
	
		double Volume(){
			return length*width*height;
		}
		int compare(Box box)
		{
			cout << "Box with pointer " << this->length << endl; //this pointer access
			cout << "Box without pointer: " << length << endl;
			return this->Volume() > box.Volume();
		}
	
	private:
		double length;
		double width;
		double height;
};

int main(){
	Box Box1(3.3, 12., 1.5);
	Box Box2(8.5, 6.0, 2.0);
	Box *ptrBox;		//Declare pointer

	ptrBox = &Box1;		//save address to object

	if (Box1.compare(Box2)){
		cout << "Box2 is smaller than Box1" << endl;
	}
	else{
		cout << "Box2 is equal to or largern than Box1" << endl;
	}
	cout << "Volume of Box1: " << ptrBox->Volume() << endl;
}
