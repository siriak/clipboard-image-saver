from win32clipboard import IsClipboardFormatAvailable
from PIL.ImageGrab import grabclipboard
import win10toast

toaster = win10toast.ToastNotifier()

IMAGE_SAVE_DIRECTORY = 'E:\\OneDrive\\Images\\'

def is_image_in_clipboard():
    return IsClipboardFormatAvailable(8)


def get_image_from_clipboard():
    return grabclipboard()


def get_pixels_from_image(image):
    return image.getdata()


def save_image(image, timestamp):
    image.save(IMAGE_SAVE_DIRECTORY + timestamp + '.png', 'PNG')


def show_notification(message, duration_seconds):
    toaster.show_toast('Clipboard image saver', message, duration=duration_seconds)
