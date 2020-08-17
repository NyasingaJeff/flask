from flask import Flask# this imports the flask classs
#instatbtiate the flask class, __name__ is a special variable that py will use to get the name of the script
app =Flask(__name__) #when run py will assighn the name var to main
@app.route('/') #route # hr keeps calling this dude a decorAtor
def home():#function
    return "website content goes here"#what to return
#if the script was to be imported from another file then the name var will conatin the name of the file but... if the script runs itself then the main value will be given

if __name__ == "__main__":#This iis ass soon as the script runs py will give the name var "Main"
    app.run(debug=True)