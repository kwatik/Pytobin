import os
import time

# Attempt to import colorama and handle the case where it is not installed
try:
    from colorama import Fore, Style, init
    init()
except ImportError:
    print("Colorama is not installed. Please install it by running:")
    print("pip install colorama")
    exit(1)

def print_with_effects(text, delay=0.05):
    """Print text with a typing effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # New line

def repack_system_bin(output_dir, output_file_name):
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_name = os.path.basename(__file__)
    
    print_with_effects(f"Script is running from: {script_dir}", delay=0.03)
    
    # Use script's directory as the input directory
    input_dir = script_dir
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print_with_effects(f"Created output directory: {output_dir}", delay=0.03)
    else:
        print_with_effects(f"Output directory already exists: {output_dir}", delay=0.03)
    
    # Full path for the output .bin file
    output_file_path = os.path.join(output_dir, output_file_name)
    
    print_with_effects(f"Starting to repack files into: {output_file_path}", delay=0.03)

    repacked_files = []  # List to keep track of processed files

    with open(output_file_path, 'wb') as out_file:
        for root, dirs, files in os.walk(input_dir):
            print_with_effects(f"Processing directory: {root}", delay=0.03)
            for file in sorted(files):  # Sorting to ensure consistent order
                if file == script_name:
                    print_with_effects(f"Skipping script file: {file}", delay=0.03)
                    continue
                
                file_path = os.path.join(root, file)
                print_with_effects(f"Adding file: {file_path}", delay=0.03)
                with open(file_path, 'rb') as f:
                    data = f.read()
                    out_file.write(data)
                
                repacked_files.append(file_path)  # Record the file path

    print_with_effects(f"Repacking complete. Repacked system.bin created at {output_file_path}", delay=0.03)
    
    print_with_effects("Files included in the repacked system.bin:", delay=0.03)
    for file in repacked_files:
        print_with_effects(file, delay=0.02)

# Usage example
output_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
output_bin_file_name = "repacked_system.bin"

repack_system_bin(output_directory, output_bin_file_name)
