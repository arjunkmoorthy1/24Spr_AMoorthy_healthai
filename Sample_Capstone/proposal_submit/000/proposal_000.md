
# Capstone Proposal
## Mapping and Analyzing Biopsy Lesions for Prostate Cancer
### Proposed by: Arjun Moorthy
#### Email: arjunkmoorthy@gwu.edu
#### Advisor: Edwin Lo
#### The George Washington University, Washington DC  
#### Data Science Program


## 1 Objective:  
 
            The goal of this project is to develop a methodology to predict if a particular biopsied lesion of the prostate is 
            benign or malignant. This will allow doctors and other clinicians to better understand how to interpret specific, 
            suspicious Regions of Interest (ROIs) in a medical scan. It can also help doctors conduct biopsies in the future as if 
            certain localizations of prostate lesions lead to higher chances of malignant tumors. Identifying areas with higher 
            chances of malignancy could optimize biopsy procedures and remove discomfort for patients, as unnecessary biopsies 
            could be avoided. Accurately identifying malignant lesions can lead to earlier treatment and better patient outcomes.
            



## 2 Dataset:  

            This dataset is publicly available. 

            The dataset being used is part of a publicly available TCIA (The Cancer Imaging Archive) which contains thousands of 
            patients and their corresponding medical imaging data. This prostate cancer dataset contains 1151 patients with Prostate 
            MRI and Ultrasound with Pathology and Coordinates of Tracked Biopsies. For each of these patients, a set of anywhere from 
            30-60 images are provided as each patient has a slice of many MRI/Ultrasound images, in which the tracked biopsy is 
            contained within one of them. Ground truth cancer values, as well as cancer severity values are given in a target dataset. 

            We want to extrapolate the Region of Interest of the individual patient images using the biopsy coordinates and segment 
            the necessary images that contain regions where biopsies occurred. From there, I would like to feed those segmented images 
            into various different image classifications models to identify which produces the most optimal prediction accuracies on a 
            split training/testing/validation dataset. Furthermore, with the limited amounts of imaging, I hope to use techniques such 
            as k-fold cross validation to maximize the performance of the model, but limit overfitting problems. Focus on the relevant 
            regions of the image will allow the model to concentrate on the ROIs and therefore perform better. 

            In addition, such segmentation can also occur through the overlay of biospy files that are provided along with the dataset. 
            I will be working with 3D Slicer and in python to either automate the region of interest using the biopsy tracked coordinates,
            or through the biospy overlay files with 3D Slicer + Python code. 
            

## 3 Rationale:  

            This project is going to help doctors make more informed decisions about how to biopsy and diagnose prostate cancer.
            

## 4 Approach:  

            I plan on approaching this capstone through several steps.  

            1. Loading Image Data and Separating Images for Individual Patients
            2. Mapping Biopsy Coordinates onto the Corresponding Patient Images 
            3. Create Classification Deep Learning Model to Predict Biopsy Diagnosis
            4. Evaluate and Improve Model 
            

## 5 Timeline:  

            This a rough time line for this project:  

            - (1 Week) Data Loading
            - (3 Weeks) Image Segmentation Automation Using Biopsy Coordinates and/or Biopsy Overlay Files
            - (3 Weeks) Classification Model Creation  
            - (3 Weeks) Evaluate and Improve Model Training using Train/Test/Validation Split
            - (1 Weeks) Compiling Results  
            - (1 Weeks) Writing Up a paper and submission
            - (1 Weeks) Final Presentation  
            

## 6 Expected Number Students:  

            For this project, the expected number of students on this project is one.  
            

## 7 Possible Issues:  

            The challenge will be on the segmentation and data analysis part to ensure proper mapping, and if not, to still 
            maintain that the model will predict well on the patient images. Furthermore, figuring out how to automate the segmentation
            of the images using either the biopsy coordinates or the biopsy overlay files via 3D slicer, and understanding how to subsequently
            load those segmented files into Python is something I have never done and will take some time.
            


## Contact
- Author: Edwin Lo
- Email: [edwinlo@gwu.edu](Eamil)
- GitHub: [https://github.com/arjunkmoorthy1/24Spr_AMoorthy_healthai.git ](Git Hub rep)
