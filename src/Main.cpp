#include <iostream>
#include <opencv2/opencv.hpp>

int main(int argc, char** argv ) {
    cv::Mat image;
    image = cv::imread( argv[1], 1 );

    int width = image.cols;
    int height = image.rows;

    if( width < 120 || height < 120){
        std::cout << "Image height/withd is under 120." << std::endl;
        return 0;
    }
    return 0;
}

