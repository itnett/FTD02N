python
     # Python script to automatically isolate a compromised endpoint using a SOAR platform
     def isolate_endpoint(endpoint_id):
         soar_api.isolate(endpoint_id)
         print(f"Endpoint {endpoint_id} has been isolated.")

     if suspicious_activity_detected:
         isolate_endpoint(compromised_endpoint)