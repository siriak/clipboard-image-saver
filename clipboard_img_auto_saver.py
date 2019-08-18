from datetime import datetime
from PIL.ImageGrab import grabclipboard
from PIL.Image import new
from win32clipboard import IsClipboardFormatAvailable
from time import sleep
from win10toast import ToastNotifier

toaster = ToastNotifier()

def run_loop():
    old_img_list = None
    while True:  # The event loop that checks every 10 seconds for new image
        try:
            if img_in_clipboard():
                new_img = grabclipboard()
                new_img_list = list(new_img.getdata())
                if img_changed(new_img_list, old_img_list):
                    save_img(new_img)
                    old_img_list = new_img_list
                    send_message('Image saved', 3)
        except Exception as e:
            send_message('Error occured: ' + e.args[0], 3600)
        sleep(10)

def img_in_clipboard():
    return IsClipboardFormatAvailable(8)

def img_changed(new_img_list, old_img_list):
    if old_img_list is None:
        return True
    return new_img_list != old_img_list

def save_img(im):
    file_timestamp = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    im.save('E:\\OneDrive\\Images\\' + file_timestamp + '.png', 'PNG')

def send_message(msg, dur):
    toaster.show_toast('Clipboard image saver', msg, duration=dur)

if __name__ == '__main__':
     run_loop()
