from channels.routing import route
from uploadImage.consumers import create_thumbnail

channel_routing = [
    route('create_thumbnail', create_thumbnail),
]
