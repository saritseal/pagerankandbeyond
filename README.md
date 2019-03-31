#PAGE RANK AND BEYOND

This project is an attempt to implement the algorithms in Google's Page Rank and Beyond. The main objective is to learn and stretch Python. With learning the expectation is to learn 
the algorithms used in a search engine. However in reality these algorithms will be executed from multiple executing nodes in parallel. The same will be simulated by launcing Docker 
containers.

##Coding Guidelines
The **coding guidelines** must follow [PEP8](https://www.python.org/dev/peps/pep-0008/) standard. However the main aspects are:

1. Naming convention
	1.1. Package and Module names should be lower, words must be seperated by underscores
	1.2. Class Names must use Capitialised words
	1.3. Although Python is dynamically typed and we do not intend to change that, however fr better readiability it is better to provide types for input and output parameters to functions
	1.4. Function names must be word seperated by underscores  
	1.5. Use singe _ to identify non-public method or instance variable
	1.6. Use of lambda functions to be restricted, it is better to have naed functions with "def" whih can wrap a lamba expressions.
	1.7. Each public method must have a corresponding test function. Use of doc tests is not advised
	1.8. Tests will be executed using **nose**
 
 
##Running the application

The build targets are defined in the Makefile. The same can be found in the base directory of the project. 
1. Inorder to run the tests use **make test** This will run all the tests in the __test__ directory
1. This project includes Python test coverage. The test coverage can be invoked by running **make test-coverage**
1. To create a deployable package run **make build**. (Please note this fetaure is still not operational)  




Features:
1. implement pagerank matrix
	1.1
1. implement babarabsi networks