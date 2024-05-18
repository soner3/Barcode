from spire.barcode import BarcodeScanner, SpireObject


def scan_barcode(image_path):
    """
    Scans a barcode from an image.
    :param image_path: Path to the image.
    :return: Barcode type and value.
    """
    value = BarcodeScanner.ScanFile(image_path)
    return value
