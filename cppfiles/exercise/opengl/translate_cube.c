#include <GL/glut.h>

//define rotation variable and direction
double d = 0.0;
int dir = 0;

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
	//pull shape, convert and push back to screen
	glPushMatrix();
		glTranslatef(0,0,d);
		glBegin(GL_LINES);
		int i;
		for(i=0; i<12; ++i){
			glVertex3dv(vertex[edge[i][0]]);
			glVertex3dv(vertex[edge[i][1]]);
		}
		glEnd();
	glPopMatrix();

	//create smooth animation
	glutSwapBuffers();
}

//animation function
void idle(){
	//redraw screen
	if(dir) d += 0.001;
	else d -= 0.001;

	if(d > 1) dir = 0;
	if(d < 0) dir = 1;
	glutPostRedisplay();
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

//keyboard function
void keyboard(unsigned char key, int x, int y){
	if(key == 'q' || key == '\033') exit(0);
	if(key == 's') glutIdleFunc(idle); //start
	if(key == 't') glutIdleFunc(0); //stop
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

	//specify function when keyboard input is received
	glutKeyboardFunc(keyboard);

	//let glut takeover
	glutMainLoop();
	return 0;
}
