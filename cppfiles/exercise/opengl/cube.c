#include <GL/glut.h>

//define square vertex
GLdouble vertex[][3] = {
	{0.0, 0.0, 0.0},
	{1.0, 0.0, 0.0},
	{1.0, 1.0, 0.0},
	{0.0, 1.0, 0.0},
	{0.0, 0.0, 1.0},
	{1.0, 0.0, 1.0},
	{1.0, 1.0, 1.0},
	{0.0, 1.0, 1.0}
};

//define edges
int edge[][2] = {
	{0, 1},
	{1, 2},
	{2, 3},
	{3, 0},
	{4, 5},
	{5, 6},
	{6, 7},
	{7, 4},
	{0, 4},
	{1, 5},
	{2, 6},
	{3, 7}
};

//display function
void display(){
	//fill screen with specified color
	glClear(GL_COLOR_BUFFER_BIT);

	//draw axis frame
	glBegin(GL_LINES);
		glColor3d(1.0,0.0,0.0);
		glVertex3f(0.0,0.0,0.0);
		glVertex3f(10.0,0.0,0.0);

		glColor3d(0.0,1.0,0.0);
		glVertex3f(0.0,0.0,0.0);
		glVertex3f(0.0,10.0,0.0);

		glColor3d(0.0,0.0,1.0);
		glVertex3f(0.0,0.0,0.0);
		glVertex3f(0.0,0.0,10.0);
	glEnd();

	//draw cube
	glColor3d(0.0,0.0,0.0);
	glBegin(GL_LINES);
	int i;
	for(i=0; i<12; ++i){
		glVertex3dv(vertex[edge[i][0]]);
		glVertex3dv(vertex[edge[i][1]]);
	}
	glEnd();

	//execute commands that are not yet executed
	glFlush();
}

//screen is proportional to the window even if window size changes
void resize(int w, int h){
	//set windows as viewing port
	glViewport(0,0,w,h);

	//initialize transformation matrix
	glLoadIdentity();

	//set display area as proportional to size of viewport (for 3d)
	gluPerspective(30.0, (double)w/(double)h, 1.0, 100.0);
	gluLookAt(-5.0, 5.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
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

	//spcify function to execute when screen is redrawn
	glutDisplayFunc(display);

	//specify function to resize
	glutReshapeFunc(resize);

	//let glut takeover
	glutMainLoop();
	return 0;
}
