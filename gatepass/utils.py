from django.utils.crypto import get_random_string
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    return ContentFile(buffer.getvalue(), name=f'qr_{get_random_string(8)}.png')

def upload_photo(photo):
    # This function can be expanded to include any specific processing or validation for the uploaded photo
    return photo