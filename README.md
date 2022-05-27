# Pupil detection

# Objective:
this project is part of a bigger project which is capturing the retina and classifying these images in to healthy,diabetic or glaucomatic in order to do this we need to detect the pupil to track the eye movement so that the camera capturing the retina would be able to track the pupil ,to achieve this we developed this pupil detection algorithm . <br>
 # Challenges  :
 * Eye glints
 * Eye lashes
 * Eye position 
 
 so we developed this algorithm to solve these problems 
 # Algorithm architecture:
 * converting the image to grey scale                 

 * applying gaussian blur (which is a low pass filter for smoothing the image)
 * applying morphological operations like (dilate and opening) was tried but they were removed as they didn't give best results 
 * applying canny edge detection for detecting the edges in the image 
 * applying different thresholding methods like adaptive mean thresholding(AMT), adaptive Gaussian thresholding(AGT),Otsu thresholding , and binary thresholding **(binary thresholding gave the best results)**
 * Anding opretaion between the output of the edge detection and the thresholding to remove the extra details in the image and only important details will remain to make detecting the pupil an easier task
 * finding the contours and sorting them out to take the biggest contour as the pupil
 * applying elipse fitting on the pupil
 * getting the center of the pupil 

 # Results of each stage:
 ![output](https://user-images.githubusercontent.com/103740764/170370921-dfceb19f-95ff-43d1-a324-0bac93a39a26.PNG)
 
 # Instructions:
 * To try the code with the data uploaded in the data folder all you need to do is to download the data at the same folder where you downloaded the code file then you'll insert the image name at line 90 ------> k=start.takepic("") then run the code, first the original image will be displayed press ESC then the blured image will be displayed also press ESC then the image with fitted elipse and center detected will appear .
