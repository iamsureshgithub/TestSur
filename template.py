import os
import sys
from pathlib import Path
import logging
import subprocess

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = sys.argv[1]
os.environ['GITHUB_ACCESSTOKEN'] = sys.argv[2]
os.environ['GITHUB_USERNAME'] = 'iamsureshgithub'

def install():
    try:
        print (f" Inside install "+os.getcwd())
        temp = subprocess.Popen(["pip", "install" , "-r", "requirements.txt"], stdout = subprocess.PIPE)
        output = str(temp.communicate())
        print ("Output"+output)
        #subprocess.check_call([sys.executable, "-m", "pip", "install", "-r requirements.txt"])
    except Exception as e:
        print(f"Exception in install function"+""+str(e))
    else:
        print(f"Pip Install Successfull") 

def gitInit():
    try:
        print ("Git Init Executing")
        subprocess.run(["git", "init"])
    except Exception as e:
        print(f"Exception in Git Init function"+""+str(e))
    else:
        print(f"Git Init Successfull")

def dvcInit():
    try:
        print ("dvc Init Executing")
        subprocess.run(["dvc", "init"])
    except Exception as e:
        print(f"Exception in DVC Init function"+""+str(e))
    else:
        print(f"DVC Init Successfull")
    


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    ".gitignore"
]

def createProj():
    try:
        for filepath in list_of_files:
            filepath = Path(filepath)
            filedir, filename = os.path.split(filepath)
            if filedir !="":
                os.makedirs(filedir, exist_ok=True)
                logging.info(f"Creating directory; {filedir} for the file: {filename}")
            if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
                with open(filepath, "w") as f:
                    pass
                    logging.info(f"Creating empty file: {filepath}")
            else:
                logging.info(f"{filename} is already exists")
    except Exception as e:
        print(f"Exception in Create Project function"+""+str(e))
    else:
        print(f"Create Proj Successfull")


def createRepo():
    try:
       from dotenv import load_dotenv
       from github import Github 
       print("hello")
       #proj_name = str(sys.argv[1])
       access_token = os.environ['GITHUB_ACCESSTOKEN']
       #print("Inside create Repo"+proj_name+" "+access_token)
       os.environ['GITHUB_ACCESSTOKEN'] = sys.argv[2]
    #    os.environ['GITHUB_USERNAME'] = 'iamsureshgithub'
       user = Github(access_token).get_user()
       repo = user.create_repo(name=project_name)
       print(f"Succesfully created repository {project_name}")

    except Exception as e:
        print(f"Exception in Create Repo function"+""+str(e))
    else:
        print(f"Create Repo Successfull")

def gitInitPush():
    try:
        print (f" Inside gitInitPush ")
        addTemp = subprocess.Popen(["git", "add" , "."], stdout = subprocess.PIPE)
        addOutput = str(addTemp.communicate())
        print ("Output"+addOutput)
        commTemp = subprocess.Popen(["git", "commit" , "-m" , "Initial Commit"], stdout = subprocess.PIPE)
        commOutput = str(commTemp.communicate())
        print ("Output"+commOutput)
        remoAddTemp = subprocess.Popen(["git", "remote" , "add" , "origin","https://github.com/"+str(os.environ['GITHUB_USERNAME'])+"/"+str(sys.argv[1])], stdout = subprocess.PIPE)
        remAddOutput = str(remoAddTemp.communicate())
        print ("Output"+remAddOutput)
        remoPushTemp = subprocess.Popen(["git", "push" , "-u" , "origin","master"], stdout = subprocess.PIPE)
        remPushOutput = str(remoPushTemp.communicate())
        print ("Output"+remPushOutput)
    except Exception as e:
        print(f"Exception in Git Init Push function"+""+str(e))
    else:
        print(f"Git Init Push Successfull")

# def testTemp():
#     str1="https://github.com/"+str(os.environ['GITHUB_USERNAME'])+"/"+str(sys.argv[1])
#     print("str output"+str1)





if __name__ == '__main__':
    print("Hello World"+os.getcwd())
    #install()
    #gitInit()
    #dvcInit()
    #createProj()
    #createRepo()
    gitInitPush()
    #testTemp()