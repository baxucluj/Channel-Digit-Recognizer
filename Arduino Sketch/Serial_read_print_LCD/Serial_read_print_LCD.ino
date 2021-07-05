// Arduino with PCF8574T I2C LCD example
 
#include <Wire.h>                  // Include Wire library (required for I2C devices)
#include <LiquidCrystal_I2C.h>     // Include LiquidCrystal_I2C library 
#define ARRAY_MAX 15
#define SEARCH_MAX 100
int arr[ARRAY_MAX];
int search[SEARCH_MAX];
unsigned int arr_length = 0;
unsigned int search_length = 0;
LiquidCrystal_I2C lcd(0x27, 16, 2);  // Configure LiquidCrystal_I2C library with 0x27 address, 16 columns and 2 rows

//const int MaxChars = 5; // an int string contains up to 5 digits and
                        // is terminated by a 0 to indicate end of string
char input; // must be big enough for digits and terminating null
int i = 0;         // the index into the array storing the received digits

int a = 48;
void setup() {
  
  lcd.init();                        // Initialize I2C LCD module
 
  lcd.backlight();                   // Turn backlight ON
 
  lcd.setCursor(4, 0);               // Go to column 0, row 0
  lcd.print("ICT 2096");
  Serial.begin(9600);
}

char rx_byte = 0;
String rx_str = "";
String in = "";
String ex = "";
int size_off_arr = 0;
int size_off_search = 0;

//String input = "";
void loop() {
  if (Serial.available() > 0) {    
    rx_byte = Serial.read();       
    
    if (rx_byte != '\f') {
      rx_str += rx_byte;
    }
    else {
      // end of string
      Serial.println(rx_str);
      int num = rx_str.length();
      Serial.print("String length is: ");
      Serial.println(num);
      
      if(rx_str[0] == 'i'){
        //lcd.setCursor(0,1);
        //lcd.print("sunt aici");
        for(int i=1;i<rx_str.length();i++)
        {
          in += rx_str[i];
        }
        
        Serial.println(in);
        lcd.setCursor(0,0);
        lcd.print("                ");  
        lcd.setCursor(0,0);
        lcd.print("INPUT CH:");
        lcd.setCursor(10,0);
        lcd.print(in);
        if (arr_length < ARRAY_MAX) {
          arr[arr_length++] = in.toInt();
          size_off_arr++;
        } else {
          // Handle a full array.
        }
        Serial.println("Inputs arrays is:");  
        for(int j=0;j<sizeof(arr)/sizeof(arr[0]);j++)
        {
          Serial.println(arr[j]);
        }
      
        rx_str = "";  
        in = "";   
        lcd.print("                ");         
        }

      if(rx_str[0] == 's'){
        lcd.setCursor(0,1);
        lcd.print("sunt aici");
        for(int i=1;i<rx_str.length();i++)
        {
          ex += rx_str[i];
        }
        
        Serial.println(ex);
        lcd.setCursor(0,1);
        lcd.print("EXIST CH:");
        lcd.setCursor(10,1);
        lcd.print(ex);
        if (search_length < SEARCH_MAX) {
          search[search_length++] = ex.toInt();
          size_off_search++;
        } else {
          // Handle a full array.
        }
        Serial.println("Search arrays is:");  
        for(int k=0;k<sizeof(search)/sizeof(search[0]);k++)
        {
          Serial.println(search[k]);
        }
        rx_str = "";  
        ex = "";   
        lcd.print("                ");         
        }  
      Serial.println("Lungimea lui arr este:");
      Serial.println(size_off_arr);
      Serial.println("val ultimului el din arr este:");
      Serial.println(arr[size_off_arr-1]);
      if ((arr[size_off_arr-1]) == (search[size_off_search-1]))
      {
        lcd.noBacklight();
        delay(1000);
        lcd.backlight(); 
        delay(1000);
        lcd.noBacklight();
        delay(1000);
        lcd.backlight(); 
        delay(1000);
      }
    }
  }  
}
