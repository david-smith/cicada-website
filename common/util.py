import os
from django.conf import settings

def carousel_file_list_processor(request):
    path = os.path.join(settings.STATIC_ROOT, 'img', 'carousel')
    return {'carousel_images' : os.listdir(path)}