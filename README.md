excute command in the directory of uploadFile
web: daphne myproject.asgi:channel_layer --port $PORT --bind 0.0.0.0
worker: python manage.py runworker
