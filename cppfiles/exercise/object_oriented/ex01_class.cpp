//class act as a template, create blueprint for object
//object is created from a class

#include <iostream>
using namespace std;

class Box{
	//public member can be access from anywhere outside the class
	public:
		double length;	//variable
		double width;
		double height;
		double getVolume(); //function
		double getArea();

		//you can also do the following for function
		double getVolume2(){
			return length*width*height;
		}
	//private member can only be access within the class
	private:
		double area;

	//protected member is similar to private but can also be acess through inheritance
	protected:
		double outerproduct;

//usuallly we define data in private, related function in public
};

double Box::getVolume(){
	return length*width*height;
}

double Box::getArea(){
	area = length * width;
	return area;
}

int main(){
	Box box1;
	Box box2;

	double volume = 0.0;
	double are = 0.0;
	
	box1.height = 5.0;
	box1.length = 6.0;
	box1.width = 7.0;

	box2.height = 10.0;
	box2.length = 12.0;
	box2.width = 13.0;

	volume = box1.height * box1.length * box1.width;
	cout << "volume of box 1: " << volume << endl;

	volume = box2.height * box2.length * box2.width;
	cout << "volume of box 2: " << volume << endl;

	volume = box1.getVolume();
	cout << "volume of box1 using func: "<< volume << endl;

	volume = box2.getVolume2();
	cout << "volume of box2 using func: " << volume << endl;

	are = box1.getArea(); //ok because public
	//are = box1.area //error because area is private
	cout << "area of box1: " << are << endl;
}
