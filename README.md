# ipmsg-sender-simple
A simple [IPMessanger](https://ipmsg.org/) sender for python3.

[IPMessanger](https://ipmsg.org/) is lightweight messanger for LAN.

## Dependency
Nothing.

## Example
It is very simple.

    from IPMessageSender import IPMessageSender
    ipmsg = IPMessageSender('kikei', 'localhost', '192.168.0.10')
    ipmsg.send_message('192.168.0.11', 'Hello, ipmsg!!')
