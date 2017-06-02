# __init__.py - Starting of our application 
  
from flask import Flask
from flask_ask import Ask, statement, question
from vsphereapi import get_cluster, get_vcenter_health_status, vm_count

app = Flask(__name__)
ask = Ask(app, "/control_center")

@app.route('/')
def homepage():
    return "VMware Control Center Alexa Skill"

@ask.launch
def start_skill():
    welcome_message = 'vSphere Control Center is online'
    return question(welcome_message)

@ask.intent("VMCountIntent")
def share_count():
    counting = vm_count()
    count_msg = 'The total number of virtual machines in this vcenter is {}'.format(counting)
    return question(count_msg)

@ask.intent("HealthIntent")
def share_vcenter_health():
    health = get_vcenter_health_status()
    health_msg = 'The current health of the vCenter appliance is {}'.format(health)
    return question(health_msg)

@ask.intent("HostClustersIntent")
def share_hosts_in_clusters():
    hosts = get_cluster()
    host_msg = 'Current hosts in clusters are {}'.format(hosts)

if __name__ == '__main__':
    app.run(debug=True)