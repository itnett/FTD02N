shell
    event manager applet IoT_Sensor_Response
    event timer watchdog time 10
    action 1.0 cli command "show environment temperature"
    action 2.0 puts "Simulerer respons på sensorhendelse"