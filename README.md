#Create a virtual environment first 
python -m venv gpa 
source gpa/bin/activate #In Linux bash


#Install Dependencies 
pip install -r requirements.txt 

#Create a .env file 
USERNAME=your_studentID
PASSWORD=your_password

#Give execute permission to the script 
chmod +x kgpa 

#run the script 
./kgpa 

