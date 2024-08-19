# Pytobin

`pytobin` is a Python script that repacks files from a specified directory of unpacked or modified .bin files into a single `.bin` file, excluding the script itself from the repacking process.

## Features

- Repack files from a directory into a `.bin` file.
- Excludes the script file from being packed.
- Provides user feedback with a typing effect.

## Prerequisites

- Python 3.x
- `colorama` library (for colored and styled text output)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/kwatik/Pytobin.git
   cd pytobin
   ```

2. **Install Dependencies**:

   The script requires the `colorama` library. If it's not installed, the script will prompt you to install it.

   ```bash
   pip install colorama
   ```

## Usage

1. **Place the Script**:
   Ensure `pytobin.py` is located in the directory where you have the files to be repacked.

2. **Run the Script**:

   ```bash
   python pytobin.py
   ```

   This will create a new folder named `output` in the same directory as the script and save the repacked `.bin` file there.

## Example

If your script is located in `/path/to/directory`, and the files to be repacked are in this directory, running the script will create an `output` folder in `/path/to/directory` and place the repacked file named `repacked_system.bin` inside it.

## Notes

- The script excludes itself from being repacked.
- The `colorama` library is used for styled terminal output. If it's not installed, the script will display a message with installation instructions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
