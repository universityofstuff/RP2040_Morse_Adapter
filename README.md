Connect a RP2040 Zero to your computer, and install any drivers necessary for it to work.

Once the RP2040 Zero shows up as a drive on your computer, if you are using the same waveshare RP2040 Zero
that I used, copy the firmware update file in the circuitpy firmware folder directly to the drive for the rp2040.
OTHERWISE, download the version for your board here https://circuitpython.org/downloads
Once the firmware is updated, the RP2040 will reboot.

The RP2040 Zero drive should now show up as CIRCUITPY.
Copy the following files from the repo to the root folder on the RP2040:
adafruit_hid (folder and contents)
lib (folder and contents)
code.py

Connect a stereo jack to the board using the included connections guide.
Pictures and build parts/links are included to assist you in your build.

I use heatshrink to cover mine so I don't have to worry about it shorting against something conductive,
but this is not a requirement, and it will block your ability to use the boot and reset buttons if you 
ever need them, so keep this in mind. You could easily use something that is easily removable like tape
to accomplish the same goal.

This code has been tweaked to work with the VBand website at 
https://hamradio.solutions/vband/

I have found that once you connect, you may need to send several dits repeatedly by holding the paddle
to get the "lag" out before you can 100% trust it. This is not a problem with the script or RP2040. 
