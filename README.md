# RecordO

The purpose of this project is to generate a series of lotto numbers as a suggestion for Lotto Max and Lotto 649. This is achieved by pulling the winning numbers from olg website, talling the number of times each number has appeared in each position, and then randomly choosing the numbers using the tally as a weight. This project is divided into two separate programs: GetLottoNumbers.py and GenerateReport.py.

GetLottoNumbers.py: Pulls the winning numbers from the olg website. Then it uses regular expression to parse the website data and stores the result in two separate csv files. The program will then tally up the numbers for each position. The number of rows in each csv file is also recorded. The tally and the number of csv rows are recorded in a text file call "tracked_Numbers.txt". This program only works on days when the winning numbers comes out (Thursday and Friday) in order to avoid accidently spaming the 
website. The program will also do nothing if the data has already been pulled.  

GenerateReport.py: Reads the data from tracked_Numbers.txt. Using the tally from the file to generate a bar plot image for each lotto number position. The program will randomly choose numbers using a weight. This weight is generated using the tally which is divided by the number of rows each csv file has to generate a percentage. Finally an html file is created containing the randomly generated numbers and the bar plot images.

## Requirements
Please make sure the following are installed:
* Python 3.9.13
* Chrome Browser
* internet connection
* Libraries:
	*  requests 2.28.2
	*  selenium 4.8.2
	*  sys
	*  os
	*  re
	*  datetime
	*  csv
	*  matplotlib

## To Run
Before running either program, please make sure to give both programs permission to execute.
To run GetLottoNumbers.py move into the main directory and click on the file. This should produced the following files:
*  Lotto_649_Numbers.csv
*  Lotto_Max_Numbers.csv
*  tracked_Numbers.txt

To run GenerateReport.py move into the main directory and click on the file. This should produced the following files:
* MaxFreqPos1.png
* MaxFreqPos2.png
* MaxFreqPos3.png
* MaxFreqPos4.png
* MaxFreqPos5.png
* MaxFreqPos6.png
* MaxFreqPos7.png
* 649FreqPos1.png
* 649FreqPos2.png
* 649FreqPos3.png
* 649FreqPos4.png
* 649FreqPos5.png
* 649FreqPos6.png
* Lotto Report.html

## Notes
These two programs were developed on Windows 10. Both programs should be cross platform as neither programs uses any OS specific functionalities.
A shebang will be required if the user wishes to use the program as an executable on a linux or Mac computer.




