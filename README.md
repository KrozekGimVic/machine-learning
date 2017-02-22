#Machine Learning
Learning machine learning.

## Project Structure
- ```Learning``` directory has mostly usless stuff, that was written to learn the concepts behind the logistic regression.
- ```digit_recognizer``` is a package for linear digit classification using logistic regression.
	- ```skynet.py``` is the backend code for digit classification. It's written as a library that is used by other files in this package.
	- ```draw.py``` is a frontend application based on tkinter in which you write digits that are then recognized by the computer.
	- ```server.py``` is a simple server that trains the digit classifier based on the data uploaded to it.
	- ```utils``` is a subpackage with utility programs that make training the digit recognizer easier.
		- ```convert.py``` converts data that you can download from [kaggle](https://www.kaggle.com/c/digit-recognizer/data) to a strictly binary image set where 0 represents white and 1 represents black. We discovered that recognition is more accurate this way.
		- ```matrix_to_images.py``` displays engine matrix as a series of images. Each image represents one row in the engine matrix. This way you can see where the image has to be colored in and where it mustn't be if you want the image to be recognized as a certain digit.
