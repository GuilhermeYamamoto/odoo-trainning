import sys
import json
import logging

from odoo import http, tools
from odoo.http import content_disposition, dispatch_rpc, request, serialize_exception as _serialize_exception, Response

_logger = logging.getLogger(__name__)

class apiBitrix(http.Controller):
    def _log(self, line_data, status, message, line=None):
        
        log = {'line_id': line_data['id_processamento'], 'status': status, 'message': message}

        if line:
            log['dados_enviados'] = line

        return log

    ###################
    ### METODOS GET ###
    ###################
    @http.route('/api/bitrix', type='http', methods=['GET'], auth='public', csrf=False)
    def get_bitrix(self, **kwargs):
        try:
            # countries = request.env['res.partner'].search([])

            # if request.httprequest.data:
            #    domain = json.loads(request.httprequest.data)

            # data = []
            #for line in countries:
            line_data = {
                'id': line.id,
                'name': line.name,
            }
            #    data.append(line_data)

            json_data = {'result': line_data}

            return Response(json.dumps(json_data), content_type='application/json;charset=utf-8', status=200)

        except Exception as e:
            # vmsg = f'Error line: {sys.exc_info()[2].tb_lineno} \nError Message: \n{e}'
            _logger.info({e})
            return False
