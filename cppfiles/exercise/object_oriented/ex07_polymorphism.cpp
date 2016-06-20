//polymorphism: call to member function will cause a different function to be executed depending on the type of boject that invokes the function
//have different classes same function name, same paraemter but different implementations

#include <iostream>
using namespace std;

class Shape{
	protected:
		int width, height;
	
	public:
		Shape(int a=0, int b=0){
			width = a;
			height = b;
		}
		//create static linkage-> bind when compiled(early binding)
		//int area(){
		//	cout << "parent class area: " << endl;
		//	return 0;
		//}
		
		//virtual function: prevent static linkage
		//virtual int area(){
		//	cout << "parent class area" << endl;
		//	return 0;
		//}

		//pure virtual function: if there is no body by still use in derived class,
		virtual int area() = 0;
};

class Rectangle: public Shape{
	public:
		Rectangle(int a=0, int b=0):Shape(a,b){}	//means empty
		int area(){
			cout << "rectangle class area: " << endl;
			return (width*height);
		}
};

class Triangle: public Shape{
	public:
		Triangle(int a=0, int b=0):Shape(a,b){}
		int area(){
			cout << "Triangle class area: " << endl;
			return (width*height/2);
		}
};

int main(){
	Shape * shape;
	Rectangle rec(10,7);
	Triangle tri(10,5);
	
	//store the address of rec
	shape = &rec;
	//call rect area
	shape->area();

	//store the address of tri
	shape = &tri;
	//call tri area
	shape->area();

}
