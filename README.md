# One-Liner-SSH-To-Raspberry-Pi

SSH into your Raspberry Pi from anywhere with just one command

Adapted from http://docs.weaved.com/docs/userlogin and http://docs.weaved.com/docs/deviceconnect

## Pre-requisites & Usage:

You must have a Weaved account and your Pi's SSH port connected and up with Weaved.

You will need httplib2:

`sudo pip install httplib2`

Clone this repo and cd into it:

```
git clone https://github.com/Ritiek/One-Liner-SSH-To-Raspberry-Pi
cd One-Liner-SSH-To-Raspberry-Pi
```

Now just add your weaved email, pass and your pi's UID in `sshpi.py`.

You can find your UID by logging into Weaved and opening your SSH service, you will find a URL like https://developer.weaved.com/portal/members/viewerPage.php?id=00:00:00:01:00:00:A1:1A&type=00:1C:00:00:00:01:00:00:01:10:00:11:00:00:00:00&name=U1NIIFRlcm1pbmGd appear.

Here `00:00:00:01:00:00:A1:1A` is your UID

Now just run the Python script:

`sudo python sshpi.py`

It will automatically SSH into your Pi after fetching for Weaved's forwarded SSH port.

## How it Works?

It just makes use of the Weaved API to generate a token and fetch for their forwarded SSH Port.

More info on their API here http://docs.weaved.com/
