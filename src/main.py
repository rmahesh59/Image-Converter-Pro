# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image
# import os
# import zipfile

# def convert_to_jpeg(file_path):
#     try:
#         img = Image.open(file_path)
#         rgb_img = img.convert('RGB')
#         # Use the same filename but change the extension to .jpeg
#         jpeg_path = os.path.splitext(file_path)[0] + ".jpeg"
#         rgb_img.save(jpeg_path, "JPEG")
#         return jpeg_path
#     except Exception as e:
#         print(f"Failed to convert {file_path}: {e}")
#         return None

# def zip_files(file_paths, output_path):
#     with zipfile.ZipFile(output_path, 'w') as zipf:
#         for file in file_paths:
#             zipf.write(file, os.path.basename(file))

# def on_select_files():
#     files = filedialog.askopenfilenames(title="Select Image Files")
#     if files:
#         process_files(files)

# def process_files(files):
#     output_files = []
#     for file in files:
#         if file.lower().endswith(('.jpg', '.jpeg')):
#             output_files.append(file)
#         else:
#             jpeg_file = convert_to_jpeg(file)
#             if jpeg_file:
#                 output_files.append(jpeg_file)
#     zip_file_path = filedialog.asksaveasfilename(defaultextension=".zip", title="Save Zip File")
#     if zip_file_path:
#         zip_files(output_files, zip_file_path)
#         messagebox.showinfo("Success", f"Files zipped successfully to {zip_file_path}")

# def main():
#     root = tk.Tk()
#     root.title("Image Converter Pro")

#     welcome_label = tk.Label(root, text="Welcome to Image Converter Pro", font=("Arial", 14))
#     welcome_label.pack(pady=20)

#     select_button = tk.Button(root, text="Select Files", command=on_select_files)
#     select_button.pack(pady=10)

#     root.mainloop()

# if __name__ == "__main__":
#     main()



# import tkinter as tk
# from tkinter import filedialog, messagebox
# from PIL import Image
# import os
# import zipfile

# def convert_to_jpeg(file_path):
#     try:
#         img = Image.open(file_path)
#         rgb_img = img.convert('RGB')
#         # Use the same filename but change the extension to .jpeg
#         jpeg_path = os.path.splitext(file_path)[0] + ".jpeg"
#         rgb_img.save(jpeg_path, "JPEG")
#         return jpeg_path
#     except Exception as e:
#         print(f"Failed to convert {file_path}: {e}")
#         return None

# def zip_files(file_paths, output_path):
#     with zipfile.ZipFile(output_path, 'w') as zipf:
#         for file in file_paths:
#             zipf.write(file, os.path.basename(file))

# def on_select_files():
#     files = filedialog.askopenfilenames(title="Select Image Files")
#     if files:
#         process_files(files)

# def on_select_folder():
#     folder = filedialog.askdirectory(title="Select Folder")
#     if folder:
#         # Get all files in the selected folder
#         files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
#         process_files(files)

# def process_files(files):
#     output_files = []
#     for file in files:
#         if file.lower().endswith(('.jpg', '.jpeg')):
#             output_files.append(file)
#         else:
#             jpeg_file = convert_to_jpeg(file)
#             if jpeg_file:
#                 output_files.append(jpeg_file)
#     zip_file_path = filedialog.asksaveasfilename(defaultextension=".zip", title="Save Zip File")
#     if zip_file_path:
#         zip_files(output_files, zip_file_path)
#         messagebox.showinfo("Success", f"Files zipped successfully to {zip_file_path}")

# def main():
#     root = tk.Tk()
#     root.title("Image Converter Pro")

#     # Set the window size to 600x400 pixels
#     root.geometry("600x400")

#     welcome_label = tk.Label(root, text="Welcome to Image Converter Pro", font=("Arial", 16))
#     welcome_label.pack(pady=20)

#     select_files_button = tk.Button(root, text="Select Files", command=on_select_files)
#     select_files_button.pack(pady=10)

#     select_folder_button = tk.Button(root, text="Select Folder", command=on_select_folder)
#     select_folder_button.pack(pady=10)

#     root.mainloop()

# if __name__ == "__main__":
#     main()


import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import zipfile
import tempfile

def convert_to_jpeg(file_path, temp_dir):
    try:
        img = Image.open(file_path)
        rgb_img = img.convert('RGB')
        # Use the same filename but change the extension to .jpeg
        jpeg_filename = os.path.basename(os.path.splitext(file_path)[0]) + ".jpeg"
        jpeg_path = os.path.join(temp_dir, jpeg_filename)
        rgb_img.save(jpeg_path, "JPEG")
        return jpeg_path
    except Exception as e:
        print(f"Failed to convert {file_path}: {e}")
        return None

def zip_files(file_paths, output_path):
    with zipfile.ZipFile(output_path, 'w') as zipf:
        added_filenames = {}
        for file in file_paths:
            base_name = os.path.basename(file)
            if base_name in added_filenames:
                # If a duplicate is found, append a counter to the filename
                count = added_filenames[base_name] + 1
                new_name = f"{os.path.splitext(base_name)[0]}_{count}{os.path.splitext(base_name)[1]}"
                added_filenames[base_name] = count
            else:
                new_name = base_name
                added_filenames[base_name] = 1
            zipf.write(file, new_name)

def on_select_files():
    files = filedialog.askopenfilenames(title="Select Image Files")
    if files:
        process_files(files)

def on_select_folder():
    folder = filedialog.askdirectory(title="Select Folder")
    if folder:
        # Get all files in the selected folder
        files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        process_files(files)

def process_files(files):
    output_files = []
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')  # Add any other image formats you want to support

    # Create a temporary directory for conversions
    with tempfile.TemporaryDirectory() as temp_dir:
        for file in files:
            if os.path.isfile(file) and not file.startswith('.') and file.lower().endswith(valid_extensions):
                if file.lower().endswith(('.jpg', '.jpeg')):
                    output_files.append(file)
                else:
                    jpeg_file = convert_to_jpeg(file, temp_dir)
                    if jpeg_file:
                        output_files.append(jpeg_file)
            else:
                print(f"Skipping non-image or hidden file: {file}")

        if output_files:  # Proceed only if there are valid files to zip
            zip_file_path = filedialog.asksaveasfilename(defaultextension=".zip", title="Save Zip File")
            if zip_file_path:
                zip_files(output_files, zip_file_path)
                messagebox.showinfo("Success", f"Files zipped successfully to {zip_file_path}")
        else:
            messagebox.showwarning("No Valid Files", "No valid image files were found to process.")

def main():
    root = tk.Tk()
    root.title("Image Converter Pro")

    # Set the window size to 600x400 pixels
    root.geometry("600x400")

    welcome_label = tk.Label(root, text="Welcome to Image Converter Pro", font=("Arial", 16))
    welcome_label.pack(pady=20)

    select_files_button = tk.Button(root, text="Select Files", command=on_select_files)
    select_files_button.pack(pady=10)

    select_folder_button = tk.Button(root, text="Select Folder", command=on_select_folder)
    select_folder_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

