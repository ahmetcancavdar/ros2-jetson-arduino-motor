const int enA = 11; // PWM
const int in1 = 6;
const int in2 = 9;

int pwm = 180;

void setup() {
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  Serial.begin(115200);

  // başlangıç stop
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  analogWrite(enA, 0);
}

void forward() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  analogWrite(enA, pwm);
}

void backward() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  analogWrite(enA, pwm);
}

void stopMotor() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  analogWrite(enA, 0);
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();

    if (c >= '0' && c <= '9') {
      int level = c - '0';          // 0..9
      pwm = map(level, 0, 9, 0, 255);
      // hız değiştiyse mevcut yön devam eder, stop ise stop kalır
    } else if (c == 'F') {
      forward();
    } else if (c == 'B') {
      backward();
    } else if (c == 'S') {
      stopMotor();
    }
  }
}
