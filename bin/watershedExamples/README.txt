Subject: Watershed Segmentation Documentation
Author : Eric Chiang (eric.chiang.m@gmail.com)
Date   : April 9th, 2013

To run watershed segmentation:
  $ ./WatershedSegmentation1 <inputImage> <outputImage> <conductanceTerm> <diffusionIterations> <lowerThreshold> <outputScaleLevel> <gradientMode>

Suggested values (for the last 5 variables):
  2 10 0.001 0.15 0
  2 10 0     0.05 1

Images:
  - Test images in the 'watersheds/images/testImages' folder
  - Use the 'watersheds/out' folder to store the output image

Params:
  - diffusionIterations -- Method to reduce image noise.
  - lowerThreshold -- The threshold at which watershed will create a 
      segment. The lower the threshold, the more splits will be performed,
      and the more segmented the resulting image will become.


