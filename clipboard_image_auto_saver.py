import os
from datetime import datetime
from time import sleep

NOTIFICATION_DURATION_SECONDS = 1
MAX_DELAY_SECONDS = 30
IMAGE_SAVE_DIRECTORY_LINUX = '/home/siriak/Pictures/'
IMAGE_SAVE_DIRECTORY_WINDOWS = 'E:\\OneDrive\\Images\\'

if os.name == 'posix':
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk, Gdk
    cb = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
elif os.name == 'nt':
    from win32clipboard import IsClipboardFormatAvailable
    from PIL.ImageGrab import grabclipboard
    import win10toast
    toaster = win10toast.ToastNotifier()
else:
    pass


def run_loop(is_image_in_clipboard, get_image_from_clipboard, get_pixels_from_image, save_image, show_notification):
    old_hash = 0
    delay = MAX_DELAY_SECONDS
    while True:  # The event loop that checks every <delay> seconds for new image
        sleep(delay)
        delay = min(delay + 1, MAX_DELAY_SECONDS)
        try:
            if not is_image_in_clipboard():
                continue
            image = get_image_from_clipboard()
            new_hash = hash(tuple(get_pixels_from_image(image)))
            if new_hash == old_hash:
                continue
            delay //= 2
            old_hash = new_hash
            timestamp = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
            save_image(image, timestamp)
            show_notification('Image saved')
        except Exception as e:
            show_notification('Error occurred: ' + e.args[0])


def is_image_in_clipboard_linux():
    return cb.wait_is_image_available()


def is_image_in_clipboard_windows():
    return IsClipboardFormatAvailable(8)


def get_image_from_clipboard_linux():
    return cb.wait_for_image()


def get_image_from_clipboard_windows():
    return grabclipboard()


def get_pixels_from_image_linux(image):
    return image.get_pixels()


def get_pixels_from_image_windows(image):
    return image.getdata()


def save_image_linux(image, timestamp):
    image.savev(IMAGE_SAVE_DIRECTORY_LINUX + timestamp + '.jpg', 'jpeg', ['quality'], ['100'])


def save_image_windows(image, timestamp):
    image.save(IMAGE_SAVE_DIRECTORY_WINDOWS + timestamp + '.png', 'PNG')


def show_notification_linux(msg):
    os.system(F'notify-send -t {NOTIFICATION_DURATION_SECONDS}000 "{msg}"')


def show_notification_windows(msg):
    toaster.show_toast('Clipboard image saver', msg, duration=NOTIFICATION_DURATION_SECONDS)


is_image_in_clipboard_map = {
    'posix': is_image_in_clipboard_linux,
    'nt': is_image_in_clipboard_windows,
}
get_image_from_clipboard_map = {
    'posix': get_image_from_clipboard_linux,
    'nt': get_image_from_clipboard_windows,
}
get_pixels_from_image_map = {
    'posix': get_pixels_from_image_linux,
    'nt': get_pixels_from_image_windows,
}
save_image_map = {
    'posix': save_image_linux,
    'nt': save_image_windows,
}
show_notification_map = {
    'posix': show_notification_linux,
    'nt': show_notification_windows,
}

is_image_in_clipboard = is_image_in_clipboard_map[os.name]
get_image_from_clipboard = get_image_from_clipboard_map[os.name]
get_pixels_from_image = get_pixels_from_image_map[os.name]
save_image = save_image_map[os.name]
show_notification = show_notification_map[os.name]

run_loop(is_image_in_clipboard, get_image_from_clipboard, get_pixels_from_image, save_image, show_notification)
