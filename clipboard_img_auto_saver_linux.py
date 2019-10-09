from datetime import datetime
from time import sleep
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
cb = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
import os

def run_loop():
    new_hash = old_hash = 0
    while True:  # The event loop that checks every 10 seconds for new image
        try:
            new_hash = process_clipboard(old_hash)
            if new_hash != old_hash:
                old_hash = new_hash
                send_message('Image saved')
        except Exception as e:
            send_message('Error occured: ' + e.args[0])
        sleep(10)

def process_clipboard(old_hash):
    if not img_in_clipboard():
        return old_hash
    new_img = cb.wait_for_image()
    new_pixels = new_img.get_pixels()
    new_hash = hash(tuple(new_pixels))
    if new_hash == old_hash:
        return old_hash
    save_img(new_img)
    return new_hash

def img_in_clipboard():
    return cb.wait_is_image_available()

def save_img(im):
    file_timestamp = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    im.savev('/home/siriak/Pictures/' + file_timestamp + '.jpg', 'jpeg', ['quality'], ['100'])

def send_message(msg):
    os.system('notify-send -t 1000 "' + msg + '"')

if __name__ == '__main__':
    run_loop()
