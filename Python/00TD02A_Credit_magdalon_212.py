python
   config = {
       "server_name": "webserver1",
       "port": 80,
       "ssl_enabled": True,
       "administrator": "admin@example.com",
   }

   # Accessing dictionary values
   port = config.get("port")
   ssl_status = config.get("ssl_enabled")
   print(f"Server running on port {port}, SSL enabled: {ssl_status}")

   # Modifying dictionary values
   config["port"] = 443
   config["log_level"] = "INFO"

   # Removing a dictionary key
   config.pop("administrator", None)
   print("Updated configuration:", config)