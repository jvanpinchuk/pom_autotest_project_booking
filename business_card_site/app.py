import subprocess
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route("/run_ui")
def run_ui():
    """Run UX/UI Tests"""
    cmd = ["../scripts/run_test_ui_booking.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/run_api")
def run_api():
    """Run API Tests"""
    cmd = ["../scripts/run_test_api_booking.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)



@app.route("/run-allure")
def run_allure():
    """Run Allure Report"""
    cmd = ["../scripts/runallure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/error")
def error():
    """Error page"""
    return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True)