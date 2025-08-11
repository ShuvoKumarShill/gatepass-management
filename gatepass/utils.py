from django.utils.crypto import get_random_string
from io import BytesIO
from django.core.files.base import ContentFile


def generate_qr_code(data):
    # Placeholder implementation; actual QR generation removed to avoid heavy deps
    buffer = BytesIO()
    buffer.write(data.encode('utf-8'))
    return ContentFile(buffer.getvalue(), name=f'qr_{get_random_string(8)}.txt')


def upload_photo(photo):
    return photo