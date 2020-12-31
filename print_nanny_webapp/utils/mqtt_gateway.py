# from datetime import datetime, timedelta
# import ssl
# import jwt

# import paho.mqtt.client as mqtt

# from print_nanny_webapp.utils.prometheus_metrics import (
#     mqtt_client_connected_metric,
#     mqtt_gateway_connected_metric,
#     mqtt_gateway_retrying_metric
# )
# from django.conf import settings


# @todo
# it's possible to configure a gateway server to relay messages to mqtt
# if pis cannot directly connect to google's mqtt bridge


# https://cloud.google.com/community/tutorials/cloud-iot-rtdp
# def create_jwt(project_id, private_key_file, algorithm, jwt_expires_minutes=settings.JWT_EXPIRES_MINUTES):
#     """Creates a JWT (https://jwt.io) to establish an MQTT connection.
#         Args:
#          project_id: The cloud project ID this device belongs to
#          private_key_file: A path to a file containing either an RSA256 or
#                  ES256 private key.
#          algorithm: The encryption algorithm to use. Either 'RS256' or 'ES256'
#         Returns:
#             A JWT generated from the given project_id and private key, which
#             expires in 20 minutes. After 20 minutes, your client will be
#             disconnected, and a new JWT will have to be generated.
#         Raises:
#             ValueError: If the private_key_file does not contain a known key.
#         """

#     token = {
#             # The time that the token was issued at
#             'iat':datetime.utcnow(),
#             # The time the token expires.
#             'exp': datetime.utcnow() + timedelta(minutes=jwt_expires_minutes),
#             # The audience field should always be set to the GCP project id.
#             'aud': project_id
#     }

#     # Read the private key file.
#     with open(private_key_file, 'r') as f:
#         private_key = f.read()

#     print('Creating JWT using {} from private key file {}'.format(
#             algorithm, private_key_file))

#     return jwt.encode(token, private_key, algorithm=algorithm)

# class MQTTClient:
    

#     def __init__(self, 
#         device_id: str, 
#         private_key_file: str, 

#         algorithm='RS256', 
#         ca_certs=settings.GCP_ROOT_CA,
#         mqtt_bridge_hostname=settings.GCP_MQTT_BRIDGE_HOSTNAME,
#         mqtt_bridge_port=settings.GCP_MQTT_BRIDGE_PORT,
#         on_connect=None,
#         on_disconnect=None,
#         on_log=None,
#         on_message=None,
#         on_publish=None,
#         on_subscribe=None,
#         on_unsubscribe=None,
#         project_id=settings.GCP_PROJECT_ID,
#         region=settings.GCP_CLOUD_IOT_DEVICE_REGISTRY_REGION,
#         registry_id=settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
#         tls_version=ssl.PROTOCOL_TLSv1_2,
#         message_callbacks=[] # see message_callback_add() https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#subscribe-unsubscribe
#         ):

#         self.device_id = device_id
#         client_id = f'projects/{project_id}/locations/{region}/registries/{registry_id}/devices/{device_id}'

#         self.client_id = client_id
#         self.private_key_file = private_key_file
#         self.algorithm = algorithm
#         self.project_id = project_id
#         self.mqtt_bridge_hostname = mqtt_bridge_hostname
#         self.mqtt_bridge_port = mqtt_bridge_port


#         self.client = mqtt.Client(client_id=client_id)

#         # register callback functions
#         if on_connect:
#             self.client.on_connect = on_connect
#         if on_disconnect:
#             self.client.on_disconnect = on_disconnect
#         if on_message:
#             self.client.on_message = on_message
#         if on_publish:
#             self.client.on_publish = on_publish
#         if on_subscribe:
#             self.client.on_subscribe = on_subscribe
#         if on_unsubscribe;
#             self.client.on_unsubscribe = on_unsubscribe


#         # device receives configuration updates on this topic
#         self.mqtt_config_topic = f'/devices/{self.device_id}/config'

#         # device receives commands on this topic
#             # The topic that the device will receive commands on.
#         self.mqtt_command_topic = f'/devices/{self.device_id}/commands/#'

        
#         # configure tls
#         client.tls_set(ca_certs=ca_certs, tls_version=ssl.PROTOCOL_TLSv1_2)
#         # With Google Cloud IoT Core, the username field is ignored, and the
#         # password field is used to transmit a JWT to authorize the device.
#         client.username_pw_set(
#             username='unused',
#             password=create_jwt(
#                     project_id, private_key_file, algorithm))
    
#     def connect(self):
#         self.client.connect(self.mqtt_bridge_hostname, self.mqtt_bridge_port)

#         # subscribe config topic (qos=1 message guaranteed to be transmitted at least once, with re-sends until message is ack'd)
#         logging.info(f'Subscribing device_id={self.device_id} to topic {self.mqtt_config_topic}')
#         self.client.subscribe(self.mqtt_config_topic, qos=1)
#         # subscribe command topic (qos=2 message delivered exactly once)
#         logging.info(f'Subscribing device_id={self.device_id} to topic {self.mqtt_command_topic}')
#         self.client.subscribe(self.mqtt_command_topic, qos=2)
    
#     def publish(self, topic, payload, retain=False, qos=2):

#         '''
#             topic
#             the topic that the message should be published on
#             payload
#             the actual message to send. If not given, or set to None a zero length message will be used. Passing an int or float will result in the payload being converted to a string representing that number. If you wish to send a true int/float, use struct.pack() to create the payload you require
#             qos
#             the quality of service level to use
#             retain
#             if set to True, the message will be set as the "last known good"/retained message for the topic.
#         '''
#         return self.client.publish(topic, payload, qos=qos, retain=retain)

#
# @todo license
# https://github.com/xavierlesa/channels-asgi-mqtt
# #

async def mqtt_send(future, channel_layer, channel, event):
    result = await channel_layer.send(channel, event)
    future.set_result(result)

async def mqtt_group_send(future, channel_layer, group, event):
    result  = await channel_layer.group_send(group, event)
    future.set_result(result)

# Only for groups
async def mqtt_group_add(future, channel_layer, group):
    channel_layer.channel_name = channel_layer.channel_name or await channel_layer.new_channel()
    result = await channel_layer.group_add(group, channel_layer.channel_name)
    future.set_result(result)

# Only for groups
async def mqtt_group_discard(future, channel_layer, group):
    result = await channel_layer.group_discard(group, channel_layer.channel_name)
    future.set_result(result)

class Server(object):
    def __init__(self, channel,
            algorithm='RS256', 
            ca_certs=settings.GCP_ROOT_CA,
            gateway_id=settings.GCP_CLOUD_IOT_GATEWAY, 
            jwt_expires_minutes=settings.JWT_EXPIRES_MINUTES,
            mqtt_bridge_hostname=settings.GCP_MQTT_BRIDGE_HOSTNAME,
            mqtt_bridge_port=settings.GCP_MQTT_BRIDGE_PORT,
            mqtt_channel_name = "mqtt", 
            mqtt_channel_pub="mqtt.sub",
            mqtt_channel_sub="mqtt.pub", 
            gateway_private_key=settings.GCP_GCLOUD_IOT_GATEWAY_PRIVATE_KEY,
            project_id=settings.GCP_PROJECT_ID,
            registry_id=settings.GCP_CLOUD_IOT_DEVICE_REGISTRY,
            tls_version=ssl.PROTOCOL_TLSv1_2,
            topics_subscription=[('#', 2)], 
            
        ):

        self.channel = channel

        self.algorithm = algorithm
        self.ca_certs = ca_certs
        self.gateway_id = gateway_id
        self.jwt_expires_minutes = jwt_expires_minutes
        self.mqtt_bridge_hostname = mqtt_bridge_hostname
        self.mqtt_bridge_port = mqtt_bridge_port
        self.mqtt_channel_name = mqtt_channel_name
        self.mqtt_channel_pub = mqtt_channel_pub
        self.mqtt_channel_sub = mqtt_channel_sub

        self.gateway_private_key = gateway_private_key
        self.project_id = project_id
        self.registry_id = registry_id
        self.tls_version = tls_version
        self.topics_subscription = topics_subscription
        
        # gateway client
        self.client = MQTTClient(
            gateway_id,
            gateway_private_key,
            algorithm=algorithm,
            ca_certs=ca_certs,
            mqtt_bridge_hostname=mqtt_bridge_hostname,
            mqtt_bridge_port=mqtt_bridge_port,
            project_id=project_id,
            region=registry_id,
            registry_id=registry_id,
            tls_version=tls_version,
        )

        self.client.on_connect = self._on_connect
        self.client.on_disconnect = self._on_disconnect
        self.client.on_message = self._on_message

        assert isinstance(self.topics_subscription, list), "Topic subscription must be a list with (topic, qos)"



    def attach_device(self, device_id, auth):
        '''
            Attach device_id subscription to gateway server
        '''

        logging.info(f"Attaching device_id={device_id} to gateway_id={self.gateway_id}")

        attach_topic = '/devices/{}/attach'.format(device_id)
        attach_payload = '{{"authorization" : "{}"}}'.format(auth)
        self.client.publish(attach_topic, attach_payload, qos=1)
        mqtt_client_connected_metric.inc()

    def detach_device(client, device_id):
        """Detach the device from the gateway."""
        
        detach_topic = '/devices/{}/detach'.format(device_id)
        logging.info(f"Detaching device_id={device_id} to gateway_id={self.gateway_id}")
        self.client.publish(detach_topic, '{}', qos=1)
        mqtt_client_connected_metric.dec()
        

    def _on_connect(self, client, userdata, flags, rc):
        logger.info("Gateway device connected to MQTT broker with status {}".format(rc))
        self.client.subscribe(self.topics_subscription)
        mqtt_gateway_connected_metric.inc()

    def _on_disconnect(self, client, userdata, rc):
        logger.warning("Gateway device disconnected from MQTT broker")
        mqtt_gateway_connected_metric.dec()
        if not self.stop:
            mqtt_gateway_retrying_metric.inc()
            j = 10
            for i in range(j):
                logger.info("Gateway attempting to reconnect to MQTT broker (JWT probably expired)")
                try:
                    # client.reconnect() not sure if reconnect supports modifying auth, re-instantiate client for now
                    self.client = MQTTClient(
                        gateway_id,
                        gateway_private_key,
                        algorithm=algorithm,
                        ca_certs=ca_certs,
                        mqtt_bridge_hostname=mqtt_bridge_hostname,
                        mqtt_bridge_port=mqtt_bridge_port,
                        project_id=project_id,
                        region=registry_id,
                        registry_id=registry_id,
                        tls_version=tls_version,
                    )
                    self.client.connect()
                    logger.info("Gateway successfully reconnected to MQTT broker")
                    break
                except Exception as e:
                    if i < j:
                        logger.warn(e)
                        time.sleep(1)
                        continue
                    else:
                        raise
        mqtt_gateway_retrying_metric.dec()


    def _on_message(self, client, userdata, message):
        logger.debug("Received message from topic {}".format(message.topic))
        payload = message.payload.decode("utf-8")

        try:
            payload = json.loads(payload)
        except:
            logger.debug("Payload is nos a JSON Serializable")
            pass
        
        logger.debug("Raw message {}".format(payload))

        # Compose a message for Channel with raw data received from MQTT
        msg = {
            "topic": message.topic,
            "payload": payload,
            "qos": message.qos,
            "host": userdata["host"],
            "port": userdata["port"],
        }

        try:
            # create a coroutine and send
            future = asyncio.Future()
            asyncio.ensure_future(
                    mqtt_send(
                        future, 
                        self.channel, 
                        self.mqtt_channel_name,
                        {
                            "type": self.mqtt_channel_sub,
                            "text": msg
                        })
                )

            # attach callback for logs only
            future.add_done_callback(self._mqtt_send_got_result)

        except Exception as e:
            logger.error("Cannot send message {}".format(msg))
            logger.exception(e)

    def _mqtt_receive(self, msg):
        '''
            Receive a message from Django channel (e.g. client connected to websocket)
            and publish to MQTT broker
        '''

        if msg['type'] == self.mqtt_channel_pub:
            payload = msg['text']
            if not isinstance(payload, dict):
                payload = json.loads(payload)

            logger.info("Receive a menssage with payload:\r\n%s", msg)
            self.client.publish(
                    payload['topic'], 
                    payload['payload'], 
                    qos=payload.get('qos', 2), 
                    retain=False)            


    

if __name__ == '__main__':
    client.loop_forever()
