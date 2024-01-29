#%%
import json
import os
import shutil

#%%

def save_to_json(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)

semester2code = { "sp":"01", "spr":"01", "spring":"01", "su":"02", "sum":"02", "summer":"02", "fa":"03", "fall":"03"}
thisfilename = os.path.basename(__file__) # should match _ver for version, ideally 3-digit string starting as "000", up to "999"

data_to_save = \
    {
        # -----------------------------------------------------------------------------------------------------------------------
        "Version":
            """000""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2024""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Spring""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Mapping and Analyzing Biopsy Lesions for Prostate Cancer""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The goal of this project is to develop a methodology to predict if a particular biopsied lesion of the prostate is 
            benign or malignant. This will allow doctors and other clinicians to better understand how to interpret specific, 
            suspicious Regions of Interest (ROIs) in a medical scan. It can also help doctors conduct biopsies in the future as if 
            certain localizations of prostate lesions lead to higher chances of malignant tumors. Identifying areas with higher 
            chances of malignancy could optimize biopsy procedures and remove discomfort for patients, as unnecessary biopsies 
            could be avoided. Accurately identifying malignant lesions can lead to earlier treatment and better patient outcomes.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            This dataset is publicly available. 

            The dataset being used is part of a publicly available TCIA (The Cancer Imaging Archive) which contains thousands of 
            patients and their corresponding medical imaging data. This prostate cancer dataset contains 1151 patients with Prostate 
            MRI and Ultrasound with Pathology and Coordinates of Tracked Biopsies. For each of these patients, a set of anywhere from 
            30-60 images are provided as each patient has a slice of many MRI/Ultrasound images, in which the tracked biopsy is 
            contained within one of them. Ground truth cancer values, as well as cancer severity values are given in a target dataset. 

            We want to extrapolate the Region of Interest of the individual patient images using the biopsy coordinates and segment 
            the necessary images that contain regions where biopsies occurred. From there, I would like to feed those segmented images 
            into various different image classifications models to identify which produces the most optimal prediction accuracies on a 
            split training and testing dataset. Such focus on the relevant regions of the image will allow the model to concentrate on 
            the ROIs and therefore perform better. 
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            This project is going to help doctors make more informed decisions about how to biopsy and diagnose prostate cancer.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps.  

            1. Loading Image Data and Separating Images for Individual Patients
            2. Mapping Biopsy Coordinates onto the Corresponding Patient Images 
            3. Create Classification Deep Learning Model to Predict Biopsy Diagnosis
            4. Evaluate and Improve Model 
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  

            - (2 Weeks) Data Loading.  
            - (2 Weeks) Image Segmentation Using Biopsy Coordinates
            - (5 Weeks) Classification Model Creation  
            - (2 Weeks) Evaluate and Improve Model Training
            - (1 Weeks) Compiling Results  
            - (1 Weeks) Writing Up a paper and submission
            - (1 Weeks) Final Presentation  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Expected Number Students":
            """
            For this project, the expected number of students on this project is one.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
            The challenge will be on the segmentation and data analysis part to ensure proper mapping, and if not, to still 
            maintain that the model will predict well on the patient images.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "Arjun Moorthy",
        "Proposed by email": "arjunkmoorthy@gwu.edu",
        "instructor": "Edwin Lo",
        "instructor_email": "edwinlo@gwu.edu",
        "github_repo": "https://github.com/arjunkmoorthy1/24Spr_AMoorthy_healthai.git ",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(
    os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}',
    exist_ok=True)
output_file_path = os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy(thisfilename, output_file_path)
print(f"Data saved to {output_file_path}")
