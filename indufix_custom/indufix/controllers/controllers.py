import sys
import json
import logging

from odoo import http
from odoo.http import request as Response

_logger = logging.getLogger(__name__)

class apiBitrix(http.Controller):
    """
    def _log(self, line_data, status, message, line=None):
        
        log = {'line_id': line_data['id_processamento'], 'status': status, 'message': message}

        if line:
            log['dados_enviados'] = line

        return log
    """
    
    ###################
    ### METODOS GET ###
    ###################
    @http.route('/api/bitrix/', type='http', methods=['GET'], auth='public')
    def get_bitrix(self, **kwargs):
        try:
            _logger.info('Iniciando o método get_bitrix')
            # countries = request.env['res.partner'].sudo().search([])
            countries = ''
            # Restante do seu código...

            json_data = {'result': countries}

            return Response(json.dumps(json_data), content_type='application/json;charset=utf-8', status=200)

        except Exception as e:
            _logger.error(str(e))
            vmsg = f'Error line: {sys.exc_info()[2].tb_lineno} \nError Message: \n{e}'
            _logger.error(vmsg)
            return Response(f'Bad Request - {vmsg}', content_type='text/html;charset=utf-8', status=400)

