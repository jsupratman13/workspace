#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/objdetect/objdetect.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include<iostream>
#include <cmath>
using namespace std;
using namespace cv;

float L = 1; //m
float x_width;
float y_height;
float focal_length;
float xi, yi;
float h = 0.17; //m (170mm)

int main(int argc, const char *argv[]){

//Initialization
	string pic = string(argv[1]);
	int key;
	Mat base;
	Mat frame;
	CascadeClassifier haar_cascade;
	vector<Rect_<int> > base_face;
	vector<Rect_<int> > faces;
	haar_cascade.load("C:/opencv/release/install/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml");
	VideoCapture capture(0);

//Obtaining Reference Parameters
	base = imread("standard_1meter.jpg", CV_LOAD_IMAGE_COLOR);
	haar_cascade.detectMultiScale(base, base_face);
	for(int i=0; i< base_face.size(); i++){
		Rect face_i = base_face[i];
		x_width = face_i.width;
		y_height = face_i.height;
	}

//Focal Length Calculation
	focal_length = (x_width*L)/h;
	cout << "focal length: " << focal_length << endl;
	cout << "pixel: " << x_width << endl;
//Activate WebCamera
	if(!capture.isOpened())
		return -1;

	namedWindow("window",1);

	if(capture.isOpened()){
		while(1){
			capture >> frame;
			haar_cascade.detectMultiScale(frame, faces);	

			if(!frame.empty()){
				for(int i=0; i< faces.size(); i++){
					Rect face_i = faces[i];
					rectangle(frame, face_i, CV_RGB(255,0,0),5);
					xi = face_i.width;
					yi = face_i.height;

					//z transform method
					string box_text = format("distance = %.4f m", (focal_length*h)/xi);
					int pos_x = max(face_i.tl().x -10, 0);
					int pos_y = max(face_i.tl().y -10, 0);
					putText(frame, box_text, Point(pos_x, pos_y), FONT_HERSHEY_PLAIN, 1.0, CV_RGB(0,0,255), 2.0);
	
					//geometry method
					string box_text2 = format("distance = %.4f m", (x_width*L)/xi);
					int pos_x2 = max(face_i.tl().x - 10, 0);
					int pos_y2 = max(face_i.br().y + 15, 0);
					putText(frame, box_text2, Point(pos_x2, pos_y2), FONT_HERSHEY_PLAIN, 1.0, CV_RGB(0,255,0), 2.0);
				}
				imshow("window", frame);
			}

			key = waitKey(1);

			//Quit
			if(key == 'q'){
				destroyAllWindows();
				capture.release();
				return 0;
			}

			//Save Image
			if((key == 'c')){
				cout << "captured image "<< xi << endl;
				imshow("window",frame);
				waitKey(0);
				imwrite(pic, frame);
			}
		}
	}else{
		return -1;
	}
}
