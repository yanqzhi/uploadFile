import os
import logging
from channels import Channel
from django.conf import settings
from PIL import Image
from .models import ImageFile


def create_thumbnail(message):
    logger = logging.getLogger('command')
    try:
        image_id = message.content.get('id')
        image_file = ImageFile.objects.get(id=image_id)
    except ImageFile.DoesNotExist:
        logger.info("id:" + str(image_id))

    im = Image.open(image_file.image.file)
    logger.info(image_file.image.file)
    size = 128, 128
    im.thumbnail(size)
    file, ext = os.path.splitext(image_file.image.name)
    thumbnail = 'media/' + file + "_thumbnail.jpeg"
    logger.info(thumbnail)
    im.save(thumbnail)
    image_file.thumbnail = thumbnail
    logger.info(image_file.thumbnail)
    image_file.save()
    logger.info("success id:" + str(image_id))
