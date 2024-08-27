python
def GenerateConfig(context):
    resources = [{
        'name': 'my-vm-instance',
        'type': 'compute.v1.instance',
        'properties': {
            'zone': context.properties['zone'],
            'machineType': ''.join(['zones/', context.properties['zone'],
                                    '/machineTypes/', context.properties['machineType']]),
            'disks': [{
                'deviceName': 'boot',
                'type': 'PERSISTENT',
                'boot': True,
                'initializeParams': {
                    'sourceImage': context.properties['sourceImage']
                }
            }],
            'networkInterfaces': [{
                'network': 'global/networks/default'
            }]
        }
    }]
    return {'resources': resources}