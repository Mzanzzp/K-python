"""
iot/device.py powinien zawierać interfejs opisujący urządzenie (Device). Powinien zawierać
następujące abstrakcyjne metody:
connect
nie przyjmuje nic, zwraca None
disconnect
nie przyjmuje nic, zwraca None
send_message
przyjmuje message_type który jest klasy MessageType oraz data - napis
def status_update(self) -> str:
nie przyjmuje nic zwraca napis
"""