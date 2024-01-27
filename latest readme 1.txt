								MLOPS Assignment Set - 2


*************************************************Guidelines****************************************************
The Objective of the assignment is to evaluate your model finetuning and Dockerization skills.
 
You have a total of 6 tasks given to you (tasks 0-5) . You have to complete atleast 3 task (which are inline with the below points) 
to full extent inorder to complete the assigment 

1. Task 0 and 1 are mandatory for everyone. 
2. You need to mandatorily take any one task on the Dockerization skills (Task 3, 4, 5).
3. Additional tasks will fetch you extra points.

Example scenario:
	 Task 0, Task 1, Task 2, Task 5
	 Task 0, Task 1,  Task 3
	 Task 0, Task 1, Task 4
	 Task 0, Task 1, Task 2, Task 4
*******************************************************************************************************************
Task 0, 1 & 2
	Open the Jupyter notebook attached along with this notebook and follow the instructions present there. Finish the task and submit the notebook back through git or zip for evaluation.
-----------------------------------------------------------
Task 3 ,4 ,5 all involve dockerization of the model from any last attempted stage(0, 1 or 2) and another task . And your image should be pushed to Dockerhub and source code in either git or through zip
For evaulation. 
-----------------------------------------------------------
Task 3:
	The objective of this task is to  Dockerize the model file from any of your last done task and add a POST endpoint through REST api using any python webserver
in the port 8080. The endpoint should return the summary of a conversation present in a json file. 
------------------------------------------------------------
Task 4 :
	Use Kafka to implement the above endpoint and write a docker-compose file to run the broker as well as your image together in the same network.
------------------------------------------------------------
Task 5 :
	Use Gradio / streamlit to create simple frontend for your Docker image. ( NOTE: The input will still be a json file upload)

------------------------------------------------------------
Refer test.json for the jsom schema of the json file during evaluation.

For queries regarding the assignment reach out to ashwin.kumar@uniphore.com




My Additional Goals to complete:

Basic Goals to clear the selection assigment:
- Fine Tune a model
- Tweek the Model
- Create Classes & Objects
- Modularize the code
- Package Pyton code
- REST API Wraper
- Dockerize, with Docker Compose
- Streamlit UI

Additional Goals to fetch extra points:
- Model Optimization
- Pytest for unit testing
- GitHub Actions
- Kafka