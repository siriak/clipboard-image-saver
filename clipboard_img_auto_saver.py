from datetime import datetime
from PIL.ImageGrab import grabclipboard
from PIL.Image import new
from win32clipboard import IsClipboardFormatAvailable
from time import sleep

def run_loop():
    old_img_list = ''
    while True:  # The event loop that checks every 10 seconds for new image
        try:
            if img_in_clipboard():
                new_img = grabclipboard()
                if img_changed(new_img, old_img_list):
                    old_img_list = list(new_img.getdata())
                    process_clipboard(new_img)
        except Exception as e:
            print('An error occured', e)
        sleep(10)

def img_in_clipboard():
    return IsClipboardFormatAvailable(8)

def img_changed(new_img, old_img_list):
    if old_img_list == '':
        return True
    return list(new_img.getdata()) != old_img_list

def process_clipboard(new_img):
    tim = keep_transparency(new_img)
    save_img(tim)

def keep_transparency(im):
    im = im.convert("RGBA")
    tim = new('RGBA', im.size, (255,255,255,0))
    tim.paste(im, (0,0), mask=im.split()[3])
    return tim   

def save_img(im):
    file_timestamp = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    im.save('E:\\OneDrive\\Images\\' + file_timestamp + '.png', 'PNG')

if __name__ == '__main__':
     run_loop()
