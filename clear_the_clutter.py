import os

def rename_folders_in_folder(folder_path):
    # Print the current folders in the folder
    print("Current folders in the folder:")
    for foldername in os.listdir(folder_path):
        print(foldername)

    # Initialize a counter for the new folder names
    counter = 1
    folders_renamed = False  # Flag to track if any folders were renamed

    # Get all items in the specified folder
    for foldername in os.listdir(folder_path):
        # Construct the full path
        old_folder = os.path.join(folder_path, foldername)

        # Check if it is a directory
        if os.path.isdir(old_folder):
            # Construct the new folder name with .png extension
            new_foldername = f"{counter}.png"
            new_folder = os.path.join(folder_path, new_foldername)

            # Print the renaming attempt
            print(f"Attempting to rename '{old_folder}' to '{new_folder}'")

            # Rename the folder if the new name is different
            if old_folder != new_folder:
                try:
                    os.rename(old_folder, new_folder)
                    print(f"Renamed '{foldername}' to '{new_foldername}'")
                    counter += 1
                    folders_renamed = True
                except Exception as e:
                    print(f"Error renaming folder '{old_folder}' to '{new_folder}': {e}")

    # Check if any folders were renamed
    if not folders_renamed:
        print("No new folders were renamed.")

# Example usage
folder_path = r"C:\Users\abulh\OneDrive\Dokumen\CS\Code With Harry\PYTHON\new folder 2"  # Use raw string to avoid escape issues
rename_folders_in_folder(folder_path)
