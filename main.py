from flask import Flask, render_template, request
import csv
app = Flask(__name__)

list = []
list1 = []

with open('Movie_Id_Titles.csv','r', errors='ignore') as cs:
    creader = csv.reader(cs)
    next(creader)
    for line in creader:
        list1.append(line[1])


@app.route('/')
def index():
    return render_template("movies.html")

@app.route('/', methods=['POST'])
def getval():
    list = []
    movieName = request.form['search-bar']
    i=0
    for n in list1:
        if(movieName.lower() in n.lower()):
            list.append(list1[i])
            i=i+1
        else:
            i=i+1

    return render_template("movies.html", list = list)

if __name__ == "__main__":
    app.run()