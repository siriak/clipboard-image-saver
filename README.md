Clipboard Image Auto Saver is a Python script which monitor OS's clipboard and automatically saves images from there.

## Usage on Windows
1. Install required packages using package manager [pip](https://pip.pypa.io/en/stable/). First, run console as an administrator. Then just copy the following string into the console.
```bash
python -m pip install pillow pywin32 win10toast
```
2. Customize your save location in clipboard_image_auto_saver.py.
3. Run the clipboard_image_auto_saver.bat file by double clicking it. The batch file is provided to launch the python script in background.
4. Add shortcut to clipboard_image_auto_saver.bat in C:\Users\\<your user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup. Windows will start script automatically on Windows load.

## Usage on Linux
1. Customize your save location in clipboard_image_auto_saver.py.
2. Add the script to startup.

## Contributing
Please open an issue first to discuss what you would like to change.
