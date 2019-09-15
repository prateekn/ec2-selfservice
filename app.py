from flask import Flask, render_template, request, flash,redirect
from helpers import *


app = Flask(__name__)
app.config.from_object("config")

@app.route('/')
def index():
    getstatus = get_status(aws_access_key_id,aws_secret_access_key,aws_session_token,location)
    return render_template("index.html",ec2s=getstatus)

@app.route('/action', methods=['GET', 'POST'])
def action():
    instanceid = request.form.get("EC_select")
    action = request.form.get("EC_action_select")
    action2 = request.form.get("EC_action2_select")
    inst_count = request.form.get("count_select")
    output = "None"
    op = "None"

  
    if str(action) == 'None' and str(action2)  != 'None' and int(inst_count) != 0:
        inst_id = start_instance(aws_access_key_id,aws_secret_access_key,aws_session_token,location,image_id,instance_type)
        output = "Instance",inst_id
        op = "Launch"
        return render_template("action.html",operation=op,output2=output)
    elif str(action2) == 'None' and str(action)  != 'None':
        del_instance = [instanceid]
        delete_instance(aws_access_key_id,aws_secret_access_key,aws_session_token,location,del_instance)
        output = "Instance ",del_instance," terminated"
        op = "Terminate"
        return render_template("action.html",operation=op,output2=output)
    elif str(action2) != 'None' and str(action)  != 'None':
        output = "Invalid Option Selected"
        op = "Error"
        return render_template("action.html",operation=op,output2=output)
    else:
        output = "Bad Request...No Action Item Selected"
        return render_template("action.html",operation=op,output2=output)
     
if __name__ == '__main__':
    app.run(debug=True)
