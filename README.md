# braintumor-masking
Steps to get Brain Tumor images and its masks automatically from niftii data of TCGA and BraTS datasets-like. 

Requirements:
Nibabel
Nilearn

So, we will have 3D data right here. From the 3D image, we will have three axis coordinate system where for each of them holds three values (RGB). The values will give us a show how that one voxel look like.

To know more about voxel and real world mappings, you can check this here http://nipy.org/nipy/devel/code_discussions/understanding_affines.html

As explained from the link above, in 3D MRI images, we use Real World Coordinates. Real-world coordinates are coordinates where the values refer to real-world axes. 

Here we’ll use the usual neuroimaging convention, and that is to label our axes relative to the subject’s head:

•x has negative values for left and positive values for right <br>
•y has negative values for posterior (back of head) and positive values for anterior (front of head) <br>
•z has negative values for the inferior (towards the neck) and postive values for superior (towards the highest point of the head, when standing)
