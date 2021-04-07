from flask import Flask, render_template, request
import csv
import subprocess

#Initiate a Flask server
app = Flask(__name__)


#Route to the home page of the utility.
@app.route('/', methods=['GET','POST'])
def index():
    #If the 'Show Results" button is not clicked, do not show any data.
    if request.method == 'GET':    
        return render_template("index.html")

    #If the "Show Results" button is clicked, open the CSV files generated by Locust, Parse them, and output them in the HTML file as a table
    elif request.method =="POST":
        results_request_stats = []
        results_rt_stats = []        
       # subprocess.Popen("runlocust.bat", shell=True)
        try:
       #Grab only the request statistics
            with open("csv_files/example_stats.csv", "r") as file_in:
                with open("csv_files/request_stats.csv", "w") as file_out:

                    writer = csv.writer(file_out)
                    for row in csv.reader(file_in):
                        writer.writerow(row[1:11])
        except OSError:
            return "Could not find any results."
            sys.exit()

        #Grab the given data and put in variable to pass to HTML document.
        test_data = csv.DictReader(open("csv_files/request_stats.csv"))
        for row in test_data:
            results_request_stats.append(row)
        
        fieldnames_req = [key for key in results_request_stats[0].keys()]


        return render_template('index.html', results_request_stats=results_request_stats, fieldnames_req=fieldnames_req,len=len)



@app.route('/run')
def run(command):
   out = os.popen(command).read()
   return (out)

if __name__ == "__main__":
    app.run(debug=True)