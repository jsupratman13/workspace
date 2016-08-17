#include <GL/glut.h>

//display function
void display(){
	//fill screen with specified color
	glClear(GL_COLOR_BUFFER_BIT);

	//execute commands that are not yet executed
	glFlush();
}

//keyboard function
void keyboard(unsigned char key, int x, int y){
	//if q or esc key, close window
	if(key == 'q'|| key == '\033'){
		exit(0);
	}
}

int main(int argc, char **argv){
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

	//Specify function to execute when screen is redrawn
	glutDisplayFunc(display);

	//specify function when keyboard input is received
	glutKeyboardFunc(keyboard);

	//loop until window closes(let glut takeover)
	glutMainLoop();
	return 0;
}
