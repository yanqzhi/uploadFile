excute command in the directory of uploadFile<br>
web: daphne myproject.asgi:channel_layer --port $PORT --bind 0.0.0.0<br>
worker: python manage.py runworker<br>

