from flask import Flask,render_template,redirect
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects/')
def projects():
    base_dir = os.getcwd() + '/projects' #projects folder
    sub_folders = os.listdir(base_dir) #list of subfolders
    index_dirs = [sub_folder + '/index.html' for sub_folder in sub_folders]
    return render_template('new_project.html', files= index_dirs)

@app.route('/projects/<string:folder_name>/')
def showcase(folder_name):
    folder_name = folder_name.split("%20")
    folder = " ".join(folder_name)
    return redirect("/projects/"+folder+"/index.html",code=302)
if __name__ == "__main__":
    app.run(debug=True)