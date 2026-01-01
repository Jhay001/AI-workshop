#checking for files on Git
ls
#Checking if on venv
python -c "import sys; print('Is virtual env?', sys.prefix != sys.base_prefix)"
# Create a virtual environment manually
python -m venv .venv
# Activate it
source .venv/bin/activate
#Automatic venv activation
echo "source .venv/bin/activate" >> ~/.bashrc
#Check your key is loaded
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('Key exists:', bool(os.getenv('GOOGLE_API_KEY')))"
# 2. Check the AI package is installed
python -c "import google.generativeai; print('AI package version:', google.generativeai.__version__)"