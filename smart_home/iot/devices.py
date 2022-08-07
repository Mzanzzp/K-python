"""
iot/devices.py powinien zawierać klasy reprezentujące urządzenia. Mają one spełniać in-
terfejs Device.

Np. dla urządzenia Hue Light, metody mają mieć następujące działanie:
connect
drukuje napis "Connecting Hue Light"
disconnect
drukuje napis "Disconnecting Hue Light"
send_message
przyjmuje odpowiedni MessageType i data i drukuje:
Hue light handling message of type {message_type.name} with data [{data}].
status_update
drukuje napis hue_light_status_ok
Oprócz Hue Light, zaimplementuj urządzenia SmartSpeaker i Curtains
"""