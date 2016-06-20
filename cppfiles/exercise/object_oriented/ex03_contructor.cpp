//constructor is special member that automatically execute when object of that class is made
//USEFUL for initialization
//destructor is special member that automatically execute when object of that class is deleted	
//USEUFL for releasing resource before closing program etc.

#include <iostream>
using namespace std;

class Line
{
	public:
		void setLength(double len);
		double getLength();
		Line(double length); //This is constructor
		~Line(); //This is destructor denoted by ~
	private:
		double length;
};

Line::Line(double len): length(len) //multiple parameter ok width(wid), height(x) etc
{
	cout << "Object is being created initial: "<< len << endl;
	//length = len; //same thing as Line::Line(): length(len)
}

Line::~Line()
{
	cout << "object is destoyed" << endl;
}

void Line::setLength(double len)
{
	length = len;
}

double Line::getLength()
{
	return length;
}

int main()
{
	Line line1(10);
	
	line1.setLength(6.0);
	cout << "Length of line: " << line1.getLength() << endl;
}

