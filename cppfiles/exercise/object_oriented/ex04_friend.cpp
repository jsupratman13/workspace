//friend function allow access to class outside class. Even private is ok

#include <iostream>
using namespace std;

class Box{
	public:
		friend void printWidth(Box box); //friend function
		void setWidth(double wid);
	private:
		double width;
};

void Box::setWidth(double wid){
	width = wid;
}

//friend of class Box
void printWidth(Box box)
{
	cout << "width of box from function: "<< box.width << endl;
}

int main(){
	Box box1;

	box1.setWidth(12.0);
	Box2 box2;

	printWidth(box1);
	box2.printWidth();
}


