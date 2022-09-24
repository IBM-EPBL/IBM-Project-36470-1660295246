#include <simpleDHT.h>
int pinDHTll = 2;
simpleDHT11 dhtll(pinDHTll);
void setup() {
    serial.begin(115200);
}
void loop() {
    byte temperature = 0;
    byte humidity = 0;
    int err = simpleDHTrrsuccess;
    if ((err = dhtll.read(&temperature, &humoidity, NULL)) |=SimpleDHTErrsuccess) {
      Serial.print("read DHTll failed, err=");
      Serial.print(SimpleDHTErrSuccess) {
          Serial.print(",");
          Serial.println(SimpleDHTErrDuration(err));
          delay(1000);
          return;
        }

        Serial.print("Sample OK: ");
        Serial.print((int)temperature);
        Serial.print(" ^c, ");
        Serial.print((int)humidity);
        Serial.print(" H");
        delay(1500);
        }
