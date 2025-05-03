# Final Project

1.Problem Statement:-
Detailed Problem Statement for Port Scanner

1. Background
In today's interconnected digital world, network security is a critical aspect of both organizational and personal infrastructure. A major component of securing networks involves identifying open ports on servers, devices, and systems.
Open ports can serve as potential entry points for attackers if not monitored and secured properly. Therefore, port scanning is a fundamental step in network auditing, vulnerability assessment, and security monitoring.
Manual port scanning (e.g., trying to connect to each port individually) is:
Extremely time-consuming
Inefficient, especially over large ranges
Prone to human errors
Thus, an automated, efficient, and user-friendly port scanning tool is necessary.

2. Problem Definition
Network administrators, ethical hackers, and cybersecurity practitioners often face challenges such as:
Lack of simple, customizable port scanning tools
The need to quickly scan large port ranges
Difficulty in identifying running services on open ports
Wasting time on slow, single-threaded scanners
Insufficient logging and reporting during scans
An effective solution must:
Allow scanning a specified range of ports
Identify and list open ports accurately
Display the service names (e.g., HTTP, FTP) associated with open ports
Support fast scanning by handling multiple ports simultaneously
Provide readable, real-time feedback and logs to the user
Be easy to use, even for beginners

3. Objective
The objective is to develop a Python-based multithreaded port scanner that:
Accepts a target IP address, start port, end port, and timeout from the user
Efficiently scans all ports in the given range
Detects and lists open ports along with their service names
Utilizes multithreading to perform faster scanning
Logs important scanning events (open ports, errors, time taken) for transparency
Handles errors gracefully without crashing

4. Scope
Target Systems: IPv4 addresses on local networks or the internet
Port Range: User-defined (e.g., 20-80, 1-1000, etc.)
Services Identification: Based on known IANA registered ports (using socket.getservbyport)
Performance: Optimized using Python's ThreadPoolExecutor with multiple worker threads
User Interaction: Command-line input/output

5. Expected Outcomes
A fast and reliable port scanner that:

Successfully identifies open ports on a target IP
Associates known service names with detected ports
Reports results clearly to the user
Logs the scanning progress and errors for troubleshooting
Enhanced understanding of basic networking, socket programming, and multithreading

[2.Setup Instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories)

3.Images:-
![Image](https://github.com/user-attachments/assets/5a4687a6-ffbc-44f4-a47e-a258566b0b51)

Video References:-
[1](https://www.youtube.com/watch?v=6hnoc0h9Lsg)
#[2](https://www.youtube.com/watch?v=EF6fqnnl3Uk)
#[3](https://www.youtube.com/watch?v=Ez8F0nW6S-w)
