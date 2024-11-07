Here’s an updated description for your DIY digital clock project, now including the WS2812B RGB LED strip and the DS1307 RTC module:

---

**DIGITAL_CLOCK_USING_RASPBERRY_PI_PICO**

The purpose of this project is to create a digital clock using a Raspberry Pi Pico, a WS2812B RGB LED strip, and a DS1307 RTC module for accurate timekeeping and vibrant display.

### REQUIREMENTS
⭐ Raspberry Pi Pico

⭐ WS2812B RGB LED Strip (to display hours and minutes with customizable colors)

⭐ DS1307 RTC Module (for real-time clock functionality)

⭐ Resistors and jumper wires for connections

⭐ Push buttons (for setting the time)

⭐ [3D Printed Clock Case Model](https://www.printables.com/model/251072-7-segment-esp8266-wall-clock/files) (optional, for a professional look)

### SETUP INSTRUCTIONS

1. **Copy the Code**  
   Upload `main.py` to your Raspberry Pi Pico.

2. **Connecting the Components**  
   - **RTC Module (DS1307):** Connect the DS1307 module to the Pico’s I2C pins to keep accurate time.
   - **WS2812B LED Strip:** Connect the data pin of the LED strip to a GPIO pin on the Pico. Use resistors to limit current where needed.

3. **Setting Up the Time**  
   - Use the DS1307 to initialize the correct time.  
   - Connect button 1 to set hours and button 2 to set minutes.

4. **3D Printed Case**  
   Download and print the clock case using the 3D model linked above for a neat finish.

5. **Code Explanation**  
   - **Display Time:** The code uses the RGB LED strip to visually show hours and minutes in color, refreshing every second.
   - **RTC Module (DS1307):** Maintains accurate time, even if the clock is powered off temporarily.
   - **Buttons:** Allow manual adjustments to the hour and minute settings.

6. **Powering the Clock**  
   Use a 5V power adapter to power the Pico, RTC module, and LED strip.

### FINAL NOTES

Once set up, this clock will display time in a vibrant, color-coded format, perfect for a personalized desk setup. Enjoy your smart, colorful clock! 😌
