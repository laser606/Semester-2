**Mappen die de coaches kunnen beoordelen zijn:**

Hier staan mijn urdf files geschreven in xacro:


src/my_robot_description/urdf/camera.xacro


src/my_robot_description/urdf/common_properties.xacro


src/my_robot_description/urdf/mobile_base.xacro


src/my_robot_description/urdf/mobile_base_gazebo.xacro


src/my_robot_description/urdf/my_robot.urdf.xacro


De launch file staat in geschreven in xml:
src/my_robot_bringup/launch/my_robot_gazebo.launch.xml 

De ros2 pi x car code staat hier:
src/vision_rpi_bot/vision_rpi_bot/cmd_to_pwm_driver.py

De raspberrypi code staat hier:
src/vision_rpi_bot/scripts/ Motor_pwm.py

**---- Raspberry pi ----**

Zorg dat je ROS2 op je raspberry pi hebt gedownload en git.
Log in via SSH op je Raspberry pi en install git en de pi x car libary’s.
sudo apt update
sudo apt upgrade
sudo apt install git
sudo apt install git python3-pip python3-setuptools python3-smbus
cd ~/
git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
cd robot-hat
sudo python3 setup.py install
cd ~/
git clone -b picamera2 https://github.com/sunfounder/vilib.git
cd vilib
sudo python3 install.py
cd ~/
git clone -b v2.0 https://github.com/sunfounder/picar-x.git
cd picar-x
sudo python3 setup.py install
cd ~/picar-x
sudo bash i2samp.sh
git clone Https://github.com/laser606/semester-2.git

Vul in het volgende commando om de nodes te bouwen en toe te voegen. Voer deze commando’s uit in de map Semester 2
colcon build
source install/setup.bash

Daarna start de Node
ros2 run vision_rpi_bot cmdVel_to_pwm_node

**---- Local Machine ----**

Eerst Runnen we de simulatie. Zorg dat je Ros2 op je computer hebt gedownload en git. Kies een bestand en plak daar het bestand in via git:
git clone Https://github.com/laser606/semester-2.git

Vul in het volgende commando om de nodes te bouwen en toe te voegen. Voer deze commando’s uit in de map Semester 2:
colcon build
source install/setup.bash

Daarna start de launch file:
ros2 launch my_robot_bringup my_robot_gazebo.launch.xml

Open een tweede terminal en voer het commando uit:
ros2 run teleop_twist_keyboard teleop_twist_keyboard

Na het uitvoeren van de commando zou je de simulatie en robot moeten kunnen besturen met de toetsen.
I = Forward
K = Stop
< = Reverse
J = Left
L = Right
