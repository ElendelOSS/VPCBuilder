import json
import os
import logging
import traceback

import builder
import customerror

from typing import Union


def handler(event: dict, context: object) -> Union[dict, Exception]:
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logger = logging.getLogger('Builder')
    logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
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
            print(response['Resources'][k]['Type'])
            if response['Resources'][k]['Type'] == 'ElendelOSS::Network::VPC':
                if 'Properties' in response['Resources'][k]:
                    _builder = builder.builder(k, response['Resources'][k]['Properties'], parameters)

                    _builder.build_all()
                    _template = _builder.get_template()
                    resources = {**resources, **_template.get('Resources')}
                    outputs = {**outputs, **_template.get('Outputs')}

        response['Resources'] = resources
        response['Outputs'] = outputs
    except customerror.requiredfielderror as e:
        logger.error(e)
        macro_response['status'] = 'failure'
        macro_response['errorMessage'] = str(e)
    except AssertionError as e:
        print(e)
        print(traceback.print_exc())
    except Exception as e:
        print(e)
        print(traceback.print_exc())
        macro_response['status'] = 'failure'
        macro_response['errorMessage'] = str(e)
    else:
        logger.info(json.dumps(macro_response, default=str))
        macro_response['fragment'] = response
    finally:
        print(macro_response)
        return macro_response
