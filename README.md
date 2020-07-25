Clipboard Image Saver is a set of Python scripts which monitor OS's clipboard and automatically save images from there.

## Usage on Windows
#### 1. Install required packages using package manager [pip](https://pip.pypa.io/en/stable/).
First, run console as an administrator. Then just copy the following string into the console.
```bash
python -m pip install pillow pywin32 win10toast
```
#### 2. Customize your save location in config.py.
Open config.py in your text editor of choise and edit IMAGE_SAVE_DIRECTORY_WINDOWS constant.
#### 3. Run the clipboard_image_auto_saver.bat file by double clicking it.
The batch file is provided to launch the python script in background.
#### 4. Add shortcut to clipboard_image_auto_saver.bat to startup
Create shortcut first by right clicking on the clipboard-image-saver.bat file and choose 'Create shortcut' from context menu. After that move brand new shotcut to C:\Users\<your user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup folder. Windows will start script automatically on Windows load.

## Usage on Linux
#### 1. Customize your save location in config.py.
Open config.py in your text editor of choise and edit IMAGE_SAVE_DIRECTORY_LINUX constant.
#### 2. Add the script to startup.

## Contributing
Please open an issue first to discuss what you would like to change.
