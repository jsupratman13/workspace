#include <GL/glut.h>

//define square length
GLdouble s = 0.5;

//display function
void display(){
	//fill screen with specified color
	glClear(GL_COLOR_BUFFER_BIT);

	//set draw color(red)
	glColor3d(1.0,0.0,0.0);
	
	//set draw type
	glBegin(GL_LINE_LOOP);

	//draw to specified points
	glVertex2d(-s,-s);
	glVertex2d(-s, s);
	glVertex2d( s, s);
	glVertex2d( s,-s);

	//finish drawing
	glEnd();

	//execute commands that are not yet executed
	glFlush();
}

int main(int argc, char ** argv){
	//initialize
	glutInit(&argc, argv);

	//define window size and position
	glutInitWindowPosition(100,100);
	glutInitWindowSize(400,400);

	//create window
	glutCreateWindow("test");

	//define background color
	glutInitDisplayMode(GLUT_RGBA);
	glClearColor(1.0,1.0,1.0,1.0);

	//specify function to execute when screen is redrawn
	glutDisplayFunc(display);

	//let glut takeover
	glutMainLoop();
	return 0;
}
