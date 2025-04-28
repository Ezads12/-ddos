PLSSS LOOK VIDEO FIRST HOW U GONNA USE IT https://www.kapwing.com/videos/680faeb76f954b3020cc089d

UDP Load Tester (Python)
This is a UDP load testing tool built with Python. It allows you to simulate network load by sending UDP packets to a target IP and port, helping you test your server's performance and capacity under stress.

⚠️ IMPORTANT: This script should only be used on your own servers or with explicit permission. Unauthorized DDoS testing is illegal and can lead to severe legal consequences.

Features:
Multithreading Support: Run multiple threads simultaneously to simulate high traffic.

Packet Size Customization: Configure the size of each UDP packet.

Test Duration: Set the duration of the test in seconds.

Packet Delay: Add a delay between each packet to reduce the chance of overwhelming the network buffer.

Installation on Windows:
Download the Executable: Download the compiled .py file from the releases section of this repository.

Run the Executable:

Simply double-click the .exe file to launch the application.

A command prompt window will open, prompting you to input the required parameters.

How to Use the Tool:
Once the .exe file is launched, you will be asked to input the following parameters:

Target IP Address: Enter the IP address of the server you want to test.

Port: The target port number to send UDP packets to.

Packet Size (bytes): The size of each UDP packet in bytes (e.g., 1024).

Test Duration (seconds): How long the test should run in seconds.

Number of Threads: The number of threads (parallel processes) to simulate.

Packet Delay: The delay between each packet sent, in seconds (e.g., 0.01).

After entering the parameters, the tool will begin sending UDP packets to the target and provide feedback on the number of packets sent.

Warning:
Use Only on Your Own Servers: This tool should only be used on your own infrastructure or with explicit permission from the network owner. Unauthorized testing may be considered DDoS attacks and is illegal.

Network Slowdown: Running the load test will likely cause network slowdown. Be cautious when performing the test to avoid disrupting other users or services.

TCP/UDP Flooding Risk: Make sure the target server and network can handle the generated load to avoid causing unintentional service outages.


Developer Notes:
This script is a basic implementation of a UDP load tester. For more complex load tests and detailed analysis, consider using other tools like Apache JMeter, Locust, or similar solutions. Always exercise caution when performing load testing to avoid network disruptions or legal issues.
