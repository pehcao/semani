from flask import Flask
from flask_cors import CORS
import os
import csv
import locale
locale.setlocale(locale.LC_ALL, 'en_US')

port = int(os.getenv("PORT"))

app = Flask(__name__)
CORS(app)
def getRouteLength(num):
    if num == 1 or num == 3 or num == 6 or num == 12 or num == 16:
        return 8
    elif num == 2 or num == 15 or num == 18 or num == 19:
        return 7
    elif num == 14 or num == 4 or num == 11 or num == 17:
        return 6
    elif num == 5 or num == 7 or num== 13 or num == 20:
        return 10
    elif num == 8 or num == 9 or num == 10:
        return 11

@app.route('/all/<flight>')
def getAll(flight):
    filename = "engines.csv"
    result = ""
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['motorid'] == flight:
                result+= str(row)
                result+= ","
        result = result.rstrip(',')
        return result.replace('\'', '\"')

@app.route('/flights/<flight>')
def getFlights(flight):
    filename = "engines.csv"
    result = "[["
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['motorid'] == flight:
                tot = int(row['totalflights']) - int(row['currentflight'])
                result+= row['currentflight']+"],["
                result+= str(tot)
        if len(result) < 3:
            return "Repair"
        else:
            result = result.rstrip(',')
            result += "]]"
            return result.replace('\'', '\"')

@app.route('/engines')
def getEngines():
    filename = "engines.csv"
    result = "["
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result += "{" + "\"key\""
            result += ":" + row['motorid']
            result += ", \"val\" :" + row['motorid']
            result += "},"
        result = result.rstrip(',')
        result += "]"
        return result.replace('\'', '\"')

@app.route('/costs/<flight>')
def getCosts(flight):
    filename = "engines.csv"
    result = "{"
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['motorid'] == flight:
                repi = float(row['repairearnings'])
                repo = row['optimumcost']
                print repo
                rep = repi - int(repo)
                norep = float(row['norepairearnings']) - 834222 - 621500
                result+="\"optimal\":\"" + str(locale.format("%d", rep, grouping=True)) +  "\", \"subopt\":\"" + str(locale.format("%d", norep, grouping=True)) + "\"}"
        return result.replace('\'', '\"')

@app.route('/')
def parse_json():
    filename = "engines.csv"
    result = "{\"engines\":["
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cycles = (int(row['totalflights']) - int(row['currentflight']))
            if cycles > 0:
                cycles /= getRouteLength(int(row['route']))
            result+= "{"
            result += "\"motorid\"" + ":" + str(row['motorid'])
            result += ","
            result += "\"cyclesleft\"" + ":" + str(cycles)
            result += ","
            result += "\"repair\"" + ":" + "\"" + row['airport'] + "\""
            result += "},"
        result = result.rstrip(',')
        result += "]}"
        return result.replace('\'', '\"')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port= port)