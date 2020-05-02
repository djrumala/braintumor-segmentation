# braintumor-masking
Steps to get Brain Tumor images and its masks automatically from niftii data of TCGA and BraTS datasets-like. 

Requirements:
Nibabel
Nilearn

So, we will face 3D data right here, which we also call voxel (volume pixel). More about voxel is well explained in http://nipy.org/nipy/devel/code_discussions/understanding_affines.html

As explained from the link above, in 3D MRI images, we use Real World Coordinates. Real-world coordinates are coordinates where the values refer to real-world axes. 

Here we’ll use the usual neuroimaging convention, and that is to label our axes relative to the subject’s head:
•x has negative values for left and positive values for right <br>
•y has negative values for posterior (back of head) and positive values for anterior (front of head) <br>
•z has negative values for the inferior (towards the neck) and postive values for superior (towards the highest point of the head, when standing)
