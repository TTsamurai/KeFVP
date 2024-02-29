import os
import shutil

# Define the directories
source_dir = "/home/m2021ttakayanagi/Documents/ECTSum/codes/ECT-BPS/ectbps_para/results/para/pred_summaries_volatility/"
target_base_dir = "/home/m2021ttakayanagi/Documents/FinancialOpinionGeneration/generation_with_stances_for_volatility_prediction/ACL19_Release/"

# Loop through each file in the source directory
for file_name in os.listdir(source_dir):
    # Construct the full path of the source file
    source_file_path = os.path.join(source_dir, file_name)

    # Construct the target directory path based on the company name and date
    target_dir_path = os.path.join(target_base_dir, file_name)

    # Check if the target directory exists
    if os.path.isdir(target_dir_path):
        # Construct the full path for the target file
        # import ipdb

        # ipdb.set_trace()
        target_file_path = os.path.join(target_dir_path, "ECT.txt")

        # Move and rename the file
        shutil.copy(source_file_path, target_file_path)
        # print(f"Moved and renamed {file_name} to {target_file_path}")
    else:
        print(
            f"Target directory {target_dir_path} does not exist. Skipping {file_name}."
        )
