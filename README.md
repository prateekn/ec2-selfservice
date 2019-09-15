# ec2-selfservice portal

Self Service Portal to manage EC2 instance
- Check status of Current running Ec2 instances.
- Terminate Ec2 instance.
- Launch new Ec2 instance.
(note: Max number of vm's that can be spawned limited by variable "fixed_count" under config.py)

![Demo Panel](/static/demo-pic.png)


## Installation
- pip install -r requirements.txt
- gunicorn  -b localhost:8000  app:app
