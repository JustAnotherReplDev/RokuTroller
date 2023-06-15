# RokuTroller

This is something simple and silly that I made; it uses the python-roku module to interact with Roku devices on your local network and will execute whatever commands you would like it to.
I made this in a few minutes, so it's not optimized and probably has a lot of bugs.

# Bugs I've found
### When you use the find_devices function, it sometimes doesn't capture all of the devices or any of them. So! I made a loop that goes until it has at least found one device.
### messes with devices in a sequence and not all at once; this is a very easy fix; just implement threading because I am too lazy too.
