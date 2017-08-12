# one-liner-SSH-to-Raspberry-Pi

SSH into your Weaved connected Raspberry Pi with one command.

Adapted from [userlogin](http://docs.weaved.com/docs/userlogin) and [deviceconnect](http://docs.weaved.com/docs/deviceconnect).

## Screenshots

<img src="http://i.imgur.com/Jeqsyti.png" width="700">

## Installation

You must have a Weaved account and your Pi's SSH port connected and up with Weaved.

Clone this repo and cd into it:

```
git clone https://github.com/ritiek/one-liner-SSH-to-Raspberry-Pi
cd one-liner-SSH-to-Raspberry-Pi
```

Now just add your weaved email, pass and your pi's UID in `sshpi.py` or `sshpi.sh` depending upon your preferred language.

You can find your UID by logging into Weaved and opening your SSH service, you will find a URL like https://developer.weaved.com/portal/members/viewerPage.php?id=00:00:00:01:00:00:A1:1A&type=00:1C:00:00:00:01:00:00:01:10:00:11:00:00:00:00&name=U1NIIFRlcm1pbmGd appear.

Here `00:00:00:01:00:00:A1:1A` is your UID

## Usage

Simply pass the bash script with `-p` option as hostname:

```
ssh pi@$(bash sshpi.sh -p)
```

It can also be used in other tools that require use of SSH like [sshuttle](https://github.com/apenwarr/sshuttle) that do not use the `-p` option.

```
sshuttle -r pi@$(bash sshpi.sh) 0.0.0.0/0
```

## Options

The tool takes `-p` as optional parameter to generate the address by passing the port number to `-p` option:

```
$ sshpi -p
proxyaddress -p proxyport
```

without `-p` option:

```
$ sshpi
proxyaddress:proxyport
```

This option may be useful to you depending on how you want to pass the SSH address as different tools use one of it as a preference.

## Add to PATH

You can copy this script to PATH, if you want a command named `sshpi`:

```
sudo cp sshpi.sh /usr/bin/sshpi
sudo chmod +x /usr/bin/sshpi
```

Then you can just do:

```
ssh pi@$(sshpi -p)
```

or

```
sshuttle -r pi@$(sshpi) 0.0.0.0/0
```

It will automatically SSH into your Pi after generating a token and fetching Weaved's forwarded SSH port.

## How it works?

It just makes use of the Weaved API.

More info on their API here http://docs.weaved.com/
