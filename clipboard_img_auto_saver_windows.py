from datetime import datetime
from PIL.Image import new
from time import sleep
from win32clipboard import IsClipboardFormatAvailable
from win10toast import ToastNotifier
from PIL.ImageGrab import grabclipboard
toaster = ToastNotifier()

def run_loop():
    new_hash = old_hash = 0
    while True:  # The event loop that checks every 10 seconds for new image
        try:
            new_hash = process_clipboard(old_hash)
            if new_hash != old_hash:
                old_hash = new_hash
                send_message('Image saved', 3)
        except Exception as e:
            send_message('Error occured: ' + e.args[0], 3600)
        sleep(10)

def process_clipboard(old_hash):
    if not img_in_clipboard():
        return old_hash
    new_img = grabclipboard()
    new_hash = hash(tuple(new_img.getdata()))
    if new_hash == old_hash:
        return old_hash
    save_img(new_img)
    return new_hash

def img_in_clipboard():
    return IsClipboardFormatAvailable(8)

def save_img(im):
    file_timestamp = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    im.save('E:\\OneDrive\\Images\\' + file_timestamp + '.png', 'PNG')

def send_message(msg, dur):
    toaster.show_toast('Clipboard image saver', msg, duration=dur)

if __name__ == '__main__':
    run_loop()
