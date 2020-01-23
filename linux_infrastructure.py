import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

cb = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

IMAGE_SAVE_DIRECTORY = '/home/siriak/Pictures/'


def is_image_in_clipboard():
    return cb.wait_is_image_available()


def get_image_from_clipboard():
    return cb.wait_for_image()


def get_pixels_from_image(image):
    return image.get_pixels()


def save_image(image, timestamp):
    image.savev(IMAGE_SAVE_DIRECTORY + timestamp + '.jpg', 'jpeg', ['quality'], ['100'])


def show_notification(message, duration_seconds):
    os.system(F'notify-send -t {duration_seconds}000 "{message}"')
