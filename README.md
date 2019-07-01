#motion_detector_simple(type of)
What we did in this motion detector is we clicked 3 images of a same location and then we calculate the difference between first and second image that's d1 and then second nd third image that's d2
Now why we detected in grayscale beacause of the reason that there can be differnce detected when light becomes dim or bright or it becomes dark or their is movement in air to ignore that we used grayscale feature and improved our accuracy
now we can do two thing
we can calculate difference d1 and d2 normally or we can calculate bitwise differnce of BGR of each element of each image 1 and 2
so we used bitwise to improve accuracy as it will tell difference between each pixel
 and all things are basic
