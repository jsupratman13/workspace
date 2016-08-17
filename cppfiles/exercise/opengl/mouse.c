#include <stdio.h>
#include <GL/glut.h>

//display function
void display(){
	//fill screen with specified color
	glClear(GL_COLOR_BUFFER_BIT);

	//execute commands that are not yet executed
	glFlush();
}

//mouse function
void mouse(int button, int state, int x, int y){
	if(button == GLUT_LEFT_BUTTON)
		printf("left\n");
	if(button == GLUT_RIGHT_BUTTON)
		printf("right\n");
	if(button == GLUT_MIDDLE_BUTTON)
		printf("middle\n");

	printf("button is ");
	if(state == GLUT_UP)
		printf("not pressed\n");
	if(state == GLUT_DOWN)
		printf("pressed \n");
	printf("mousepos is (%d, %d) \n", x,y);
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

	//specify function when mouse input is received
	glutMouseFunc(mouse);

	//loop until window closes(let glut takeover)
	glutMainLoop();
	return 0;
}
