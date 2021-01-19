# -UOBxinchen_EMATM0048
--------------------------------------------------------------------------------------
This is my coursework on the SPDA(EMATM0048) in University of Bristol MSc in Data Science.
The three folders are the contents of the three parts of my homework.
And then I'm going to show you how to run the code separately.

--------------------------------------------------------------------------------------
SDPA_PART1
Brief introduction:
This part is software development. I started using Tkinter Library to design the main page. 
But the teacher advised me not to use Tkinter, so I reimplemented the program, and both methods 
did everything required. 
Here I submit two of my implementation methods, which can be viewed by changing the methods 
in the main function, and the car class is common to both methods.
In addition, in the system without GUI, I changed all the information entered by the user to numbers 
according to the options, so that the user could enter more easily. Of course, if you enter other 
values or incorrect options, the system would prompt you and need to enter again. After successful 
car rental, the system will automatically generate an OrderID. When the car is returned, 
the system will print all car rental conditions. This ID can be used to return the car, 
but if the wrong ID is entered, the car will not be returned.
In the GUI system, users need to enter user and VIP information in the upper left menu bar before 
entering the interface of car rental and car exchange. Since the total number of vehicles is 10, 
I preset 10 users, and each user can only return the car before renting the car.
Operation mode:
File and Introduction:
car_rental.py--Vehicle class and rental record class
carRental_test.py--Unit testing（Because of the user input error value determination I implemented in 
the main function, only the function that calculates the cost is tested here）
main.py--Main function, default is not using GUI programming, remove GUI comments to run methods using GUI
mainterminal.py--Not using the GUI to implement
mainwindow.py--Using GUI to implement

--------------------------------------------------------------------------------------
SDPA_PART2
Brief introduction:
This part of the code is about a sorting algorithm problem. I use Jupyter Notebook file 
to implement and run the sorting algorithm and answer the questions in the markdown cells.
In this part, I thought I could use count statistics, which would make the complexity very low,
but the count table of count statistics is arranged from large to small, which is not what I 
wanted. So I have to borrow the idea here, scan L1, record the number of elements in L2, 
output the corresponding number in L2 order, and then output the rest of the elements in order.

File and Introduction:
SDPA_Part2.ipynb -- Run it using Jupyter（Include all algorithm results and the answer to the question）

--------------------------------------------------------------------------------------
SDPA_PART3
Brief introduction:
This part of the code is about data crawling and preliminary processing analysis. 
This part of the code is about data crawling and preliminary processing analysis
I crawled 10,000 match data using OpenDota API, including match time, match winning and losing, 
hero selection of both sides, average score of players and other information, and made a brief 
analysis of the use of games and heroes and the win rate based on these information.

File and Introduction:
data1.png--picture about the clambled data
hero_list.csv--Clambled hero data
matches_list_ranking.csv--Clambled 100 match data (as an example)
matches_list_ranking2.csv--Clambled 10000 match data (for analysis)
SDPA_Part3.ipynb---- Run it using Jupyter(Include all climbing steps and analysis results)
