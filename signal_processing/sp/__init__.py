version = 1.0


def iterchannels(img):
    """Convenience routine to allow iteration through the channels of a numpy
    ndarray that represents an image.
    """
    return [img] if img.ndim == 2 else img.transpose(2, 0 , 1)


def channels(img):
    """Convenience routine to return a list of the channels of an numpy ndarray
    that represents an image.
    """
    return [c for c in iterchannels(img)]
