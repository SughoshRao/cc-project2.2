from flask import Flask, request, jsonify
import sys
import io

app = Flask(__name__, static_url_path='/')

@app.route("/py/eval", methods=['GET', 'POST'])
def handle():
    if request.method == 'POST':

        # Implementation goes here.
        #
        # Both stdout and stderr should be captured.
        # {"stdout": "<output_from_stdout>", "stderr": "<output_from_stderr>"}

        ### BEGIN STUDENT CODE ###
        code_out = io.StringIO()
        code_err = io.StringIO()

        # capture output and errors
        sys.stdout = code_out
        sys.stderr = code_err

        input_json = request.get_json(force=True)
        # print("request from client: ", input_json)
        code = input_json['code']
        error = ""
        try:
            exec(code)
        except Exception as e:
            print("Error occurred")
            sys.stderr.write(str(e))
        # restore stdout and stderr
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        jsonToReturn = {"stdout":code_out.getvalue(),"stderr":code_err.getvalue()}

        code_out.close()
        code_err.close()

        return jsonify(jsonToReturn)
        ### END STUDENT CODE ###

if __name__ == '__main__':
    app.run(threaded=True, debug=True, host="0.0.0.0", port=6000)
