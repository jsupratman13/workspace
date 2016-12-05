#include <opencv2/opencv.hpp>
#include <cstdio>

using namespace cv;
using namespace std;

int main(int argc, char **argv){
	if (argc < 2){
		printf("using: %s image file \n", argv[0]);
		return 1;
	}

	Mat image = imread(argv[1], CV_LOAD_IMAGE_UNCHANGED);

	if(image.data == 0){
		printf("Failed to read image file %s\n", argv[1]);
		return 2;
	}
	namedWindow("dspimg", CV_WINDOW_AUTOSIZE);
	imshow("dspimg", image);
	waitKey(0);
	return 0;
}
