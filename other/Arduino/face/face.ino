#include <Adafruit_GFX.h>    // Core graphics library
#include <MCUFRIEND_kbv.h>   // Hardware-specific library
MCUFRIEND_kbv tft;

#include <Fonts/FreeSerif12pt7b.h>

#include <FreeDefaultFonts.h>

#define BLACK   0x0000
#define RED     0xF800
#define GREEN   0x07E0
#define WHITE   0xFFFF
#define GREY    0x8410

void setup(void)
{
    Serial.begin(9600);
    uint16_t ID = tft.readID();
    if (ID == 0xD3) ID = 0x9481;
    tft.begin(ID);
    tft.setRotation(1);
        tft.fillScreen(BLACK);
    
    showmsgXY(100, 60, 1, &FreeSerif12pt7b, "/\\");
    showmsgXY(200, 60, 1, &FreeSerif12pt7b, "/\\");
    showmsgXY(160, 120, 1, &FreeSerif12pt7b, "|_");
    showmsgXY(50, 175, 1, &FreeSerif12pt7b, " ___________________ ");
    showmsgXY(50, 175, 1, &FreeSerif12pt7b, "/                   \\");

}

void loop(void)
{


}    

void showmsgXY(int x, int y, int sz, const GFXfont *f, const char *msg)
{
    int16_t x1, y1;
    uint16_t wid, ht;
    tft.setFont(f);
    tft.setCursor(x, y);
    tft.setTextColor(WHITE);
    tft.setTextSize(sz);
    tft.print(msg);
}
