To clone a GitHub repository to your local machine, you use the git clone command followed by the repository's URL. 
git clone https://github.com/aiLearninghub/aiLearninghub.github.io.git

To update your local copy of a GitHub repository with the latest changes from the remote repository:
1- Navigate to the Repository Directory:
cd /Users/stevens/aiLearninghub.github.io
2- Pull the Latest Changes:
git pull origin main

Create a Virtual Environment:
cd /Users/stevens/aiLearninghub.github.io
python -m venv venv
 
Activate the Virtual Environment
source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

pip install flask bcrypt


run:
python app.py

