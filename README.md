# Ethernet Chat Room

## Table of Contents

1. [Chat Server](#Server)
   - [Listening for Clients]
   - [Recieving from Clients]
   - [Broadcasting messages to group chat]
   - [Speed Limit Control](#speed-limit-control)
2. [Clients](#Clients)
   - [User Authentication]
   - [Chat GUI]
3. [Layered Architecture](#Layered-Architecture)
4. [Team Members](#Team-Members)



## 1. Chat Server <a name="Server"></a>

Chat Server accepts the clients' connection requests after authenticating

### LCD Interface <a name="lcd-interface"></a>

- **Main Display:** The LCD continuously updates and displays the current speed and gear (P, R, N, D).
- **Speed Limit Display:** Indicates whether the speed limit is turned on (display "ON") or off (display "OFF").

### Potentiometer Interface <a name="potentiometer-interface"></a>

- **Speed Control:** ECU 1 reads the potentiometer's analog input to determine the desired speed in "D" mode.

### Keypad Interface <a name="keypad-interface"></a>

- **Gear Control:** The keypad is scanned for user input. When a gear is selected, ECU 1 updates the gear display on the LCD.
- **Speed Limit Control:** ECU 1 provides a menu option for the driver to enable or disable the speed limit feature in "D" mode.

### Speed Limit Control <a name="speed-limit-control"></a>

- When the speed limit is enabled, ECU 1 initiates communication with ECU 2 to retrieve the speed limit value from EEPROM.

## 2. Clients <a name="Clients"></a>

The client code allows users to connect to the chat room server and send/receive messages. It is implemented in Python and uses the Tkinter library for the graphical user interface.

To run the client code, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory containing the client code.
3. Run the following command: `python client.py`
4. Enter your username and password when prompted.
5. Start chatting with other users in the chat room!
   
## 3. Layered Architecture <a name="Layered-Architecture"></a>
![image](https://github.com/mohameddmahmoudd/Vehicle-Control-System/assets/52659572/5ee5af2a-0fe5-4222-ae07-aca344d18887)

## 4.Team Members <a name="Team-Members"></a>
![image](https://github.com/mohameddmahmoudd/Vehicle-Control-System/assets/52659572/0425376f-92c2-487d-b221-fd2c9848f0c1)

## For project test video please [click here](https://drive.google.com/drive/folders/1Ld8JO0gpLGcbVaCOjtVTvjn_wL4lZBCQ?usp=sharing) 
