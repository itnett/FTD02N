#include "contiki.h"
#include "contiki-net.h"
#include "erbium.h"

PROCESS(er_example_server, "Erbium Example Server");
AUTOSTART_PROCESSES(&er_example_server);

RESOURCE(hello, METHOD_GET, "test/hello", "title=\"Hello world\"");

void hello_get_handler(void* request, void* response, uint8_t* buffer, uint16_t preferred_size, int32_t* offset) {
  const char* msg = "Hello, world!";
  memcpy(buffer, msg, strlen(msg));
  REST.set_header_content_type(response, REST.type.TEXT_PLAIN);
  REST.set_response_payload(response, buffer, strlen(msg));
}

PROCESS_THREAD(er_example_server, ev, data) {
  PROCESS_BEGIN();
  rest_init_engine();
  rest_activate_resource(&resource_hello);
  while (1) {
    PROCESS_WAIT_EVENT();
  }
  PROCESS_END();
}