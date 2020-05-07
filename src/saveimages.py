import os
import nibabel as nib
from nibabel.testing import data_path
import numpy as np
import cv2 
from matplotlib import pyplot as plt 

hgg_path = "D:/JCM ELEKTRO ITS/Disertasi/Datasets/Brain Tumor/Pre-operative_TCGA_GBM_NIfTI_and_Segmentations"
lgg_path = "D:/JCM ELEKTRO ITS/Disertasi/Datasets/Brain Tumor/Pre-operative_TCGA_LGG_NIfTI_and_Segmentations"

tumorGrade = "LGG" #NOTE: Change the path to save images of LGG or HGG
modality = "_t2" #NOTE: Choose, either "t2", "t1", or "flair". DONT ERASE THE UNDERSCORE "_"

if tumorGrade == "HGG":
    path = hgg_path
else:
    path = lgg_path

patient_num = 0
axial_slice = 0

for patient in os.listdir(path):  # iterate over each image per dogs and cats
    print(patient)
    patient_path = os.path.join(path, patient)
    for entry in os.listdir(patient_path):
        if "_Manually" in entry:
            print(entry)
            example_mask = os.path.join(patient_path,entry)
            n1_mask = nib.load(example_mask) #load nifti file
            nii_mask = n1_mask.get_data() #get image data from the niftii file
            maskshape = nii_mask.shape #see the shape of image data
            # print(maskshape)
            largest_area=0
            for k in range(maskshape[2]-1): #change to range(maskshape[2]-1) if you want to analyze all slices
                # print(k) #NOTE: uncomment this to get the index of current image slice
                total = np.sum(nii_mask[:,:,k])
                # print(total) #NOTE: uncomment this to get total of pixel values of the current image slice
            
                if largest_area<total: #we want to get the largets tumor
                    largest_area=total
                    axial_slice=k

        if modality in entry and "extract" not in entry:
            print(entry)
            print(axial_slice)
            example_mask = os.path.join(patient_path,entry)
            n1_mask = nib.load(example_mask) #load nifti file
            nii_mask = n1_mask.get_data() #get image data from the niftii file
            maskshape = nii_mask.shape #see the shape of image data
            # print(maskshape)
            #changing image scale to 0-255
            for i in range (axial_slice-1, axial_slice):
                output = (nii_mask[:,:,axial_slice]/nii_mask.max() * 255).astype(np.uint8) #normalize the image to get original color
                output = np.rot90(np.rot90(np.rot90(output)))
                # plt.imshow(output, cmap='gray')
                # plt.colorbar()
                # plt.show()

                #getting file name of nifti without extension
                file_name = entry
                dir_name = "D:/JCM ELEKTRO ITS/Disertasi/Datasets/Brain Tumor/MadeByMe/"+tumorGrade
                if not os.path.exists(dir_name):
                    os.mkdir(dir_name)
                    print("Directory " , dir_name ,  " Created ")
                else:    
                    print("Directory " , dir_name ,  " already exists")
                
                out_name = "D:/JCM ELEKTRO ITS/Disertasi/Datasets/Brain Tumor/MadeByMe/"+tumorGrade+"/"+tumorGrade+"_"+modality+"_"+str(patient_num)+".jpg"
                print(out_name)
                cv2.imwrite(out_name, output)
    patient_num = patient_num+1
