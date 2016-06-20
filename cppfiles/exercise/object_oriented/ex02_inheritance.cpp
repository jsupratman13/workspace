//inheritance

#include <iostream>
using namespace std;

//Base class
class Shape
{
	public:
		void setWidth(int w){
			width = w;
		}
		void setHeight(int h){
			height = h;
		}
		int height;
	protected:
		int width;
//		int height;
};

//Derived class
class Rectangle: public Shape
{
	public:
		int getArea(){
			//width can be access here
			return (width*height);
		}
};

int main(){
	Rectangle Rect;

	Rect.setWidth(5);
	Rect.setHeight(7);
	
	//width cannot be access from outside
	//can access height from outside
	cout << "height: " << Rect.height << endl;
	cout << "Total area: " << Rect.getArea() << endl;
	return 0;
}
