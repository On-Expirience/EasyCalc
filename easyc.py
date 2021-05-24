
import os
import time

def lessgo():
    print("Easyc beta 0.1 RUN\n")
    print("Building Python-code\n-------")
    time.sleep(1.5)
    app_file = open("app.py", "w+")
    app_file.write("from flask import Flask, render_template, request\n\napp = Flask(__name__)\n@app.route('/')\ndef main():\n    return render_template('app.html')\n@app.route('/calculate', methods=['POST'])\ndef calculate():\n    num1 = request.form['num1']\n    num2 = request.form['num2']\n    operation = request.form['operation']\n    if operation == 'add':\n        result = float(num1) + float(num2)\n        return render_template('app.html', result=result)\n    elif operation == 'subtract':\n        result = float(num1) - float(num2)\n        return render_template('app.html', result=result)\n    elif operation == 'multiply':\n        result = float(num1) * float(num2)\n        return render_template('app.html', result=result)\n    elif operation == 'divide':\n        result = float(num1) / float(num2)\n        return render_template('app.html', result=result)\n\n    else:\n        return render_template('app.html')\nif __name__ == '__main__':\n    app.run()")
    app_file.close()
    print("Python-code DONE!\nBuilding HTML-structure\n-------")
    time.sleep(1.8)
    os.mkdir("templates")
    app_hatml = open("templates/app.html", "w+")
    app_hatml.write('<!DOCTYPE html>\n<html lang="en">\n<style>\nbody {display: flex;width:100%;justify-content: center;}form {display: flex;flex-direction: column;width:30%;background-color: rgb(109, 109, 253);padding: 1%;box-shadow: 0px 1px 3px 0px rgba(34, 60, 80, 0.2);border-bottom-left-radius: 4px;border-bottom-right-radius: 4px;}input, select {margin-bottom: 2vh;}p {width: 100%;text-align: center;}div {display: flex;flex-direction: row;justify-content: space-between;}div select{width: 32%;}\n</style>\n<head>\n<title>EastC project</title></head>\n<body>\n<form action="/calculate" method="POST">\n<p>Easy Calculate</p>\n<label for="Number One">First</label>\n<input type="text" placeholder="First Number" name="num1" />\n<label for="Number Two">Second</label>\n<input type="text" placeholder="Second Number" name="num2" />\n<label for="Operation">Operation</label>\n<div>\n<select name="operation">\n<option value="add">+</option>\n<option value="subtract">-</option>\n<option value="multiply">*</option>\n<option value="divide">:</option>\n</select>\n<input type="submit" value="calculate" id="calc_btn" class="btn" />\n</div>\n<p>{{ result }}</p>\n</form>\n</body>\n</html>')
    app_hatml.close
    print("HTML-structure DONE!\n")
    what_next = input("Enter anything to run app.py... ")
    if len(what_next) > 0:
        os.system("app.py")