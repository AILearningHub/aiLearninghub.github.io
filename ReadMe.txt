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

==================================
Then on the base terminal type:
>>To copy the folder:
(base) stevenss-MacBook-Pro:~ stevens$ scp -i /Users/stevens/Downloads/LHub.pem -r /Users/stevens/aiLearninghub.github.io ec2-user@ec2-3-14-86-241.us-east-2.compute.amazonaws.com

>>To copy only one file:
scp -i /Users/stevens/Downloads/LHub.pem /Users/stevens/aiLearninghub.github.io/app.py ec2-user@ec2-3-14-86-241.us-east-2.compute.amazonaws.com

>>To Connect at EC2:
ssh -i /Users/stevens/Downloads/LHub.pem ec2-user@ec2-3-14-86-241.us-east-2.compute.amazonaws.com

cd aiLearninghub.github.io

>> To see the body of app.py to ensure it is the correct vection:
cat app.py

>> To modify:
vi app.py
press 'i' to enter insert mode and edit
edit
Press 'Esc' to leave insert mode
type ':wq' and press 'Enter' to write changes and quit

python3 --version
sudo yum install python3-pip -y
python3 -m venv myenv
source myenv/bin/activate
pip install flask
python app.py


>> To look at the users.db file:
sudo yum install sqlite
sqlite3 users.db

.tables
.schema users
SELECT * FROM users;
.exit



