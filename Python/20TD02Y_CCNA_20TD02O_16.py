python
    from ncclient import manager

    with manager.connect(host='192.168.1.1', port=830, username='admin', password='password', hostkey_verify=False) as m:
        netconf_reply = m.get_config(source='running')
        print(netconf_reply)