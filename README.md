# R-PI-and-Docker
I used a Raspberry Pi 4 and a hdc 2010 temperature sensor. 

The API run on R-PI, provides the temperature readings in JSON format from the HDC2010 sensor via a web page. 

On a VM, I had a container which run python code to access the web page. The VM could access the web page only if it was in the same network as the R PI, so to enable that I used a network bridge between them.
