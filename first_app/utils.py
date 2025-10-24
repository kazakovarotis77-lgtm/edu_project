from django.core.exceptions import ValidationError

def rasm_ulchami(img):
    width = img.width
    height = img.height
    if width > 80:
        raise ValidationError(f"Rasmning eni ({width}px) 300px dan katta bo'lmasligi kerak.")
    if height > 80:
        raise ValidationError(f"Rasmning bo'yi ({height}px) 300px dan katta bo'lmasligi kerak.")
