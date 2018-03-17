# Use this file to store configuration values that might change in the future.

# Resolution to capture from the camera, as a tuple of (width, height)
CAMERA_RESOLUTION = (1920//4, 1080//4)  # TODO: Adjust to a good resolution

# True if this code is being run on the Raspberry Pi
# (Currently used only for image processing debugging)
# TODO: Remove this. It should always be True in production
RASPBERRY_PI = False


# Serial port for the arduino. Find out on Linux or Mac by running the command 'ls /dev/tty.*'
SERIAL_PORT = "/dev/tty.usbmodem1421"

############################################################
### MAKE SURE THESE MATCH THE VALUES IN THE ARDUINO CODE ###
############################################################
# Baud rate for communicating with the arduino.
SERIAL_BAUD_RATE = 115200
# Number of PPM channels for controlling the drone. Make sr
PPM_CHANNELS = 4
THROTTLE_CHANNEL = 2
ROLL_CHANNEL = 0
PITCH_CHANNEL = 1
YAW_CHANNEL = 3
