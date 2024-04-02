# R-PI-and-Docker
To make this small project, I used a Raspberry Pi 4 and a hdc 2010 temperature sensor. 

The python code run on R-PI, using API, would show in a web page the temperature in the room at every refresh.

On a VM, I had a container which run python code to access the web page. The VM could access the web page only if it was in the same network as the boar, so to enable that I used a network bridge between them.
