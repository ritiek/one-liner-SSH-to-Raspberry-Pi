# one-liner-SSH-to-Raspberry-Pi

SSH into your Weaved connected Raspberry Pi with one command.

Adapted from [userlogin](http://docs.weaved.com/docs/userlogin) and [deviceconnect](http://docs.weaved.com/docs/deviceconnect).

## Screenshots

<img src="http://i.imgur.com/CnPL0Rr.png" width="290">

## Usage

You must have a Weaved account and your Pi's SSH port connected and up with Weaved.

Clone this repo and cd into it:

```
git clone https://github.com/Ritiek/One-Liner-SSH-To-Raspberry-Pi
cd One-Liner-SSH-To-Raspberry-Pi
```

Now just add your weaved email, pass and your pi's UID in `sshpi.py` or `sshpi.sh` depending upon your preferred language.

You can find your UID by logging into Weaved and opening your SSH service, you will find a URL like https://developer.weaved.com/portal/members/viewerPage.php?id=00:00:00:01:00:00:A1:1A&type=00:1C:00:00:00:01:00:00:01:10:00:11:00:00:00:00&name=U1NIIFRlcm1pbmGd appear.

Here `00:00:00:01:00:00:A1:1A` is your UID


### Bash

Simply run the bash script:

```
bash sshpi.sh
```

You can copy this script to PATH, if you want a command named `sshpi`:

```
sudo cp sshpi.sh /usr/bin/sshpi
sudo chmod +x /usr/bin/sshpi
sshpi
```

### Python

You will need httplib2:

`sudo pip install -r requirements.txt`

Now just run the Python script:

```
python sshpi.py
```


It will automatically SSH into your Pi after generating a token and fetching Weaved's forwarded SSH port.

## How it works?

It just makes use of the Weaved API.

More info on their API here http://docs.weaved.com/
