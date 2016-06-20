//array allows variable that combine data items of same kind but strucutre allows combination of data items of different kinds

#include <iostream>
using namespace std;

//structure
struct Books{
	string title;
	int book_id;
};

//pass struc to function
void printBook(struct Books book){
	cout << "Book title: " << book.title << endl;
	cout << "Book id: " << book.book_id << endl;
}

//pointer to struct
void printBook_pointer(struct Books *book){
	cout <<"Book title: " << book->title << endl;
	cout << "Book id: " << book->book_id << endl;
};

int main(){
	struct Books book1;
	struct Books book2;
	
	//book1 specification
	book1.title = "learn c++";
	book1.book_id = 12445;

	//book2 specification
	book2.title = "sherlock holmes";
	book2.book_id = 5242;

	cout << "book1 title: " << book1.title;
	cout <<" id: " << book1.book_id << endl;
	cout << "book2 title: " << book2.title << endl;

	printBook(book1);
	printBook_pointer(&book2);

	return 0;
}

