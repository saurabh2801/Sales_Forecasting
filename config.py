import os 
current_directory = os.getcwd()
model_path =os.path.join(current_directory, 'RF_model.pkl')
json_path = os.path.join(current_directory,"project_data.json")
PORT_NUMBER = 8080