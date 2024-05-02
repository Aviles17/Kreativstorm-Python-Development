# Kreativstorm-Python-Development

![Logo](https://www.sortlist.com/_next/image?url=https%3A%2F%2Fsortlist.gumlet.io%2Fsortlist-core-api%2F32i3rycw86564ahq0xkyhn2gdwrd%3Fw%3D150%26q%3D95%26format%3Dgif&w=256&q=75)

## General Description

This repository contains the totality of the projects developed in the Kreativstorm **Python Development Hands on Training Program**. The program focused on providing students with real enterprise problems in order to train the habilities of problem solving in an algorithmic ways and usage of the programming language Python 3. The projects are the following:

### Hangman Game
This project is focused on the implementation of a Hangman Game as the title suggest. The game itself contains the basic logic using data structures, however it implements aditional features like:

- Clear the console when the game starts and finishes, independend of the Operating System
- Use **random-word-api** from herokuapp.com to prompt a word of certain lenght
- Use *os* library to read a *.txt* file, in order to have an alternative with custom words
- Minimalist GUI to play the game

<p align="center">
  <img src="https://github.com/Aviles17/Kreativstorm-Python-Development/assets/110882455/d165a4d9-6c2b-493c-9917-941a3acb0e43" alt="Hangman game initial screen" width="400" />
</p>

### Email Automation
Email automation project is inspired in a real world problem faced by the Kreativstorm team, where they needed sends daily reports to clients via email.The main objective is to create a python script that automate the process.

For this specific project we used **SMTP protocol** and a **gmail recipient**. The project includes:

- Usage of smtplib python library to connect to the email server and send the emails
- Compose email by a configuration *.json* file
- Usage of *os* library to acces the reports or files required for the email
- Usage of *schedule* library to run daily at a specific time

The following features and the overall configuration of the project is shown in this diagram:
![image](https://github.com/Aviles17/Kreativstorm-Python-Development/assets/110882455/9e77d728-88d8-4e42-92d5-a7369263163e)

### Automate File Transfer
This project follows the same principal as the one before it, a real world situation for the Kreativstorm team. Now the problem resambles in the daily data files from external partners that they recieve. These files need to be processed and analyzed, but first, they need to be transferred to the **company's internal network**. The main objective is to create a routine that automates this process, te solution includes:

- Usage of an external FTP server (Provided by https://ftp.debian.org/debian/)

- Usage of *shutil* library to move files from the local repository to the internal network of the company

- Usage of *schedule*  to run daily at a specific time

- Usage of log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process.

The following diagram shows the general flow of the solution:
<p align="center">
   <img src="https://github.com/Aviles17/Kreativstorm-Python-Development/assets/110882455/84b2d1bf-f186-4d4f-910b-9e1b90ad87f7" alt="Proyect Diagram" width="400" />
</p>

### Weather App
Lastly, Weather App is a desktop application with the future of becoming a web of mobile app. This project focuses on the development of a concept proof for an application that retrives the weather at any given time, location or coordanate.

- The application uses *tkinter* library to develop a quick and minimalist GUI for the user to interact with

- It relies on the OpenWeatherMap weather service API version 2.5 to retrieve the current information about the weather in an specific location.

- uses *Pillow* library to display icons to make the GUI more complex and enjoyable to the user

The following is a snapshot of what the app does:
![image](https://github.com/Aviles17/Kreativstorm-Python-Development/assets/110882455/2bff75de-fd3d-49b1-8faf-9ead4bb021a1)
![image](https://github.com/Aviles17/Kreativstorm-Python-Development/assets/110882455/7d777389-da51-43e7-8d41-81b1e0590f04)


## Author


- [Santiago Avilés Tibocha](https://github.com/Aviles17)
