Clipboard Image Auto Saver is a set of Python scripts which monitor OS's clipboard and automatically save images from there. You may want to change save location before using this scripts.

## Usage for Windows
1. Install required packages using package manager [pip](https://pip.pypa.io/en/stable/)
```bash
pip install pillow pywin32 win10toast
```
2. Run the clipboard_img_auto_saver.bat file. The batch file is provided to launch the python script in background.
3. Add shortcut to clipboard_img_auto_saver.bat in C:\Users\\<your user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup. Windows will start script automatically on Windows load.

## Usage for Linux
1. Customize your save location in clipboard_image_auto_saver_linux.py
2. Add the script to startup

## Contributing
Please open an issue first to discuss what you would like to change.
