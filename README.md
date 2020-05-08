# braintumor-segmentation

There are two steps that will be done here, they are getting the brain tumor images and masks automatically, and then multi-class segmentation for brain tumor can be done.

# 1. Automatically Saving Brain Tumor 2D Image Slices for Brain Tumor Segmentation and Classification from BraTS Datasets-like

<b>Requirements:</b>
<br>Nibabel<br>
Nilearn

So, we will have 3D data right here. From the 3D image data, we will have three axis coordinate system where for each of them holds three values (RGB). The values will give us a show how that one voxel look like.

To know more about voxel and real world mappings, you can check this here http://nipy.org/nipy/devel/code_discussions/understanding_affines.html

As explained from the link above, in 3D MRI images, we use Real World Coordinates. Real-world coordinates are coordinates where the values refer to real-world axes. 

Here we’ll use the usual neuroimaging convention, and that is to label our axes relative to the subject’s head:

•x has negative values for left and positive values for right <br>
•y has negative values for posterior (back of head) and positive values for anterior (front of head) <br>
•z has negative values for the inferior (towards the neck) and postive values for superior (towards the highest point of the head, when standing)

The code for saving the best tumor image and mask automatically is available on a file:

```src/saveimages.py```

But, if you want to get more explanation about NiBabel and NiLearn and the algorithm to get the image slice of largest brain tumor, it can be seen here:

```src/brain_mask.pynb```

# 2. Brain Tumor Segmentation using U-Net

After getting all the data, split them into train and test. And then, we will have data like '1.jpg' for the brain tumor image, and '1_mask.jpg' is tha mask of it.

The brain tumor segmentation using U-Net is in 

```src/braintumor_multiclass_seg_unet.ipynb ```

From this process, we can get validation accuracy of 87.37% which is not really bad for a multiclass segmentation, but still far from perfect
