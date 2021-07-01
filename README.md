<h1 align="center" id="top">Kafka Notify</h1>
<p align="center">Client gửi event lên kafka</p>

## Cài đặt

Cài đặt sử dụng thông qua**pip**

    pip install git+https://github.com/ducloi3105/kafka_notify.git#egg=bizfly_kafka_notification

hoặc thông qua mã nguồn
    
    git clone https://github.com/ducloi3105/kafka_notify.git
    cd kafka_notify
    python setup.py install 

## Yêu cầu

- Thông tin cấu hình Kafka server.

## Cách sử dụng
- Khởi tạo client

```python  
import pynotify
client = pynotify.BizflyNotificationClient(
    kafka_servers=["10.5.69.6:9092", "10.5.69.106:9092", "10.5.69.195:9092"],
    kafka_retries=2,
    kafka_config={}
)
```

<h3 id="account">Account</h3>
PyNotify hỗ trợ đẩy event thông tin tài khoản BizflyCloud

Ví dụ: Gửi event account.updated.

```python
import pynotify
client = pynotify.BizflyNotificationClient(
    kafka_servers=["10.5.69.6:9092", "10.5.69.106:9092", "10.5.69.195:9092"],
    kafka_retries=2,
    kafka_config={}
)
account_updated = client.notification().account().updated(
    topic='notification-account-stag',
    tenant_id='ajsdlkajsdlxkcvx1',
    payload={
        'value 1': 2,
        'eventId': 'aac8b4cc791a45ff8bf121dac822579b.1624333610@localhost',
        'eventTime': '2021-06-22T03:46:50.939785+00:00'
    }

)

print("send notify kafka: ", account_updated)
```
- Note: Nếu gửi event không thành công sẽ trả về exception

[⬆ Lên đầu](#top)
