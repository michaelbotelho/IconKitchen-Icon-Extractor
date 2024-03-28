# Usage: python3 ExtractIcons.py [directory]
# directory - the path to the directory containing the compressed icon folders
#
# This script will unzip all zip files in the directory and extract any icon in the ios folder with name 'AppIcon-40@3x.png'
# Built specifically to work will icons design and downloaded from Icon Kitchen

import sys
import os
import zipfile
import shutil


def PromptWarning(dir_name):
    confirmation = input("Are you sure you want to attempt to extract and clean Icons in the current directory: " + dir_name + " [Y/n]: ").lower()
    while confirmation != "y" or confirmation != "n":
        if confirmation == "n":
            exit(0)
        elif confirmation == "y":
            return
        
        print(f"'{confirmation}' not a valid input.")
        confirmation = input("Are you sure you want to attempt to extract and clean Icons in the current directory: " + dir_name + " [Y/n]?").lower()
    
    
def main():           
    try:
        # Get specified directory if exists
        if len(sys.argv) > 1:
            directory = sys.argv[1] 
        else:
            #directory = os.path.dirname(os.path.abspath(__file__))
            directory = os.getcwd()
            # Warning user if directory unspecified
            PromptWarning(directory)
            
    
        # Get a list of all items (files and folders) in the directory
        items = os.listdir(directory)
        
        
        for item in items:
            # Unzip compressed files to root directory
            if item.endswith('.zip'):  
                zip_path = os.path.join(directory, item)
                # Unzip compressed folder into root directory
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(directory)

            # Extract Icon from ios folder and rename with zip name
            tmps = os.listdir(directory)
            for tmp in tmps:
                
                # Check if the item is a folder (ignore .folders)
                if os.path.isdir(tmp) and not tmp.startswith('.'):
                    tmp_path = os.path.join(directory, tmp)
                    if tmp == 'ios':
                        icon_name = item.rsplit()[-1].split('.')[0] + '.png'
                        source_item_path = os.path.join(tmp, 'AppIcon-40@3x.png')
                        destination_item_path = os.path.join(directory, icon_name)
                    
                        # Extract the icon into the specified directory
                        os.rename(source_item_path, destination_item_path)

                    # Remove zip and any associated folder (ios, android, web)
                    if os.path.exists(zip_path): os.remove(zip_path)
                    if os.path.exists(tmp_path): shutil.rmtree(tmp_path)
                    
    except KeyboardInterrupt:
        exit(0)
    except:
        print("ERROR: could not extract icons.")
        
    
if __name__ == '__main__':
    main()
    