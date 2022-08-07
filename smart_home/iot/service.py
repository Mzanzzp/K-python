"""
powinien zawierać funkcję do generowania id generate_id, która zwróci losowy ciąg dużych liter
o zadanej długości
powinien zawierać klasę IOTService
Będzie ona przechowywać zarejestrowane urządzenia
Klasa ta powinna mieć metody:
register_device
przyjmuje Device
wywołuje metodę connect dla Device
generuje id: device_id
dodaje urządzenie do listy `devices`
unregister_device
przyjmuje device_id
odłącza urządzenie wywołując metodę disconect dla device o zadanym id
usuwa urządzenie z listy
get_device
przyjmuje device_id
zwraca urzadzenie z listy
run_program
przyjmuje listę zawierającą Message
drukuje: "=====RUNNING PROGRAM======"
dla każdej wiadomości
wywołuje dla wskazane w Message urządzenia metodę send_message z odpowiednimi danymi
drukuje "=====END OF PROGRAM======"
test_devices
nie przyjmuje argumentow
drukuje: Start test devices
dla każdego urządzenia z listy wywołuje funkcję collect_diagnostics
"""