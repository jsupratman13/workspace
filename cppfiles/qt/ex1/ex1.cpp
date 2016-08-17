#include <QApplication>
#include <QTextEdit>

int main(int argv, char **args){
	QApplication app(argv, args);  	//manages application and necessary to run any Qt program that has GUI

	QTextEdit textEdit;				//Text edit visual ement on GUI. In Qt we call it widgets ex. ScrollBar, labels etc
	textEdit.show();				//show text edit on screen with its own window frame

	return app.exec(); 				//make QAppilcation enter its event loop
}
