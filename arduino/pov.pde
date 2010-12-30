int _bases[] = {1,2,4,8,16,32,64,128}; //ugly hack, fuck it
class Pov {
  public:
    Pov (int *pins, int npins) {
      _pins = pins;
      _npins = npins;
      
      initPins();
    }
    
    void initPins() {
      for (int i = 0; i < _npins; i++) {
        Serial.println(_pins[i]);
        pinMode(_pins[i],OUTPUT);
      }
    }
    
    void setDance (int *dance, int dancesteps) {
      _dance = dance;
      _dancesteps = dancesteps;
      _dancecurstep = 0;
    }
    
    void danceStep () {
      _dancecurstep = (_dancecurstep+1)%_dancesteps;
      for (int i = 0; i < _npins; i++)
        digitalWrite(_pins[i], LOW);
      for (int j = 0 ; j < _npins; j++) {
        if (_dance[_dancecurstep]&(_bases[j]))
          digitalWrite(_pins[j], HIGH);
      }
    }
    
  private:
    int *_pins;
    int _npins;
    int *_dance;
    int _dancesteps;
    int _dancecurstep;
};

int pins[] = {5,6,7,8,9,10,11,12};
Pov mPov(pins,8);
int A[] = {0,0,238,170,170,238,68,68,68,68,68,68,124,};



void setup() {
  Serial.begin(9600);
  mPov.setDance(A, sizeof(A)/sizeof(int));  
}

void loop() {
  mPov.danceStep();
  delayMicroseconds(10000);
}
