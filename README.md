# SeeTree Home Assignment
In this assignment I used Flask as requested to construct an HTTP python service with endpoints.<br>
The assignment took me about 7 hours to complete - including design, coding and testing it.<br>
I've wrote a basic unittest file (DataTest.py). In the case I had more time, I would've written a dedicated test for 
the flask app, and move the data into a DB.
----
Files:
---
* <b>objects/Image.py & objects/Polygon.py:</b> classes for the construct of the data. Each class is responsible for storing the data and formatting it.
* <b>data_handler.py:</b> all the methods responsible for parsing and preparing the data to be returned by the service.
* <b>app.py:</b> flask application containing all the necessery endpoints as described in the exercise.
* <b>tests/DataTest.py:</b> a basic unittest testing the data_handler module.
