//interface describes the behavior or capabilities of a C++ lcass without committing to a particular implementation of that class
//C++ interface are implemented using abstract class(not the same as data abstraction)
//class is made abstract by declaring at least one one of its functions as pure virtual function
//Abstract class(or ABC) provide base class for other classes to inherit. It only serves as interface, not instantiate
//Concrete class are instantiate objects, meaning there is some thing inside(functions etc)

//abstracl base class is used to provide common and standardized interface appropriate for all the external applications

#include <iostream>
using namespace std;

//Base class (Abstract Class)
class Shape{
	public:
		//pure virtual function providing interface framework
		virtual int getArea() = 0;
	
		void setWidth(int w){
			width = w;
		}
		void setHeight(int h){
			height = h;
		}
	protected:
		int width;
		int height;
};

//Derived class
class Rectangle: public Shape{
	public:
		int getArea(){
			return width*height;
		}
};
class Triangle: public Shape{
	public:
		int getArea(){
			return (width*height)/2;
		}
};

int main(){
	Rectangle rect;
	Triangle tri;

	rect.setWidth(5);
	rect.setHeight(7);
	cout << "area of rectangle: "<< rect.getArea() << endl;

	tri.setWidth(5);
	tri.setHeight(7);
	cout << "area of triangle: " << tri.getArea() << endl;
	
	return 0;
}
