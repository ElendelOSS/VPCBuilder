import json
import os
import logging

import builder
import customerror

from typing import Union

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger('Builder')
logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))


def handler(event: dict, context: object) -> Union[dict, Error]:
    macro_response: dict = {
        'requestId': event.get('requestId'),
        'status': 'success'
    }
    resources: dict = {}
    outputs: dict = {}
    response: dict = event['fragment']
    parameters: dict = event.get('templateParameterValues', {})
    try:
        for k in list(response['Resources'].keys()):
            if response['Resources'][k]['Type'] == 'ElendelOSS::Network::VPC"':
                if 'Properties' in response['Resources'][k]:
                    _builder = builder.builder(k, response['Resources'][k]['Properties'], parameters)

                    _builder.build_all()
                    template = _builder.template.to_dict()
                    resources = {**resources, **template.get('Resources')}
                    outputs = {**outputs, **template.get('Outputs')}

        logger.debug('Resources:')
        logger.debug(json.dumps(resources, default=str))

        response['Resources'] = resources
        response['Outputs'] = outputs
    except customerror.requiredfielderror as e:
        logger.error(e)
        macro_response['status'] = 'failure'
        macro_response['errorMessage'] = str(e)
    except Exception as e:
        logger.error(e)
        macro_response['status'] = 'failure'
        macro_response['errorMessage'] = str(e)
    else:
        logger.info(json.dumps(macro_response, default=str))
        macro_response['fragment'] = response
    finally:
        return macro_response
