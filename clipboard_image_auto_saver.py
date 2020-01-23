import os
from datetime import datetime
from time import sleep

NOTIFICATION_DURATION_SECONDS = 1
MAX_DELAY_SECONDS = 30

if os.name == 'posix':
    from linux_infrastructure import\
        is_image_in_clipboard, get_image_from_clipboard,\
        get_pixels_from_image, save_image, show_notification
elif os.name == 'nt':
    from windows_infrastructure import\
        is_image_in_clipboard, get_image_from_clipboard,\
        get_pixels_from_image, save_image, show_notification
else:
    print('Java runtime not supported')
    exit(1)

old_hash = 0
delay = MAX_DELAY_SECONDS
show_notification('Clipboard Image Auto Saver is running', NOTIFICATION_DURATION_SECONDS)
while True:  # The event loop that checks every <delay> seconds for new image
    sleep(delay)
    delay = min(delay + 1, MAX_DELAY_SECONDS)
    try:
        if not is_image_in_clipboard():
            continue
        image = get_image_from_clipboard()
        if image is None:
            continue
        new_hash = hash(tuple(get_pixels_from_image(image)))
        if new_hash == old_hash:
            continue
        delay //= 2
        old_hash = new_hash
        timestamp = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
        save_image(image, timestamp)
        show_notification('Image saved', NOTIFICATION_DURATION_SECONDS)
    except Exception as e:
        show_notification('Error occurred: ' + e.args[0], NOTIFICATION_DURATION_SECONDS)
