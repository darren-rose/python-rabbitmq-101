# python-rabbitmq-101

#### dependencies

* RabbitMQ

```
docker run --rm --name my-rabbitmq \
--hostname rabbitmq \
-p 5672:5672 -p 15672:15672 \
-e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=password \
rabbitmq:3-management
```

#### installation

```
pip install -r requirements.txt
```

#### running

```
RABBITMQ_HOST=localhost \
RABBITMQ_PORT=5672 \
RABBITMQ_DEFAULT_USER=admin \
RABBITMQ_DEFAULT_PASS=password \
python main.py
```
