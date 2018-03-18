from typing import Union, Dict

import requests

from .abc import PoolInterfaceAbstract


class BTCComPool(PoolInterfaceAbstract):
    command = 'BTC.com'

    def __init__(self, access_key, puid):
        self.access_key = access_key
        self.puid = puid

    def getBalance(self) -> Union[None, Dict[str, str]]:
        resp = requests.get("https://eu.pool.btc.com/v1/realtime/hashrate?access_key=%s&puid=%s" % (
            self.access_key, self.puid,
        ))

        resp_json = resp.json()

        if resp_json['err_no'] != 0:
            return {
                "Error": resp_json['err_msg']
            }
        else:
            return {
                "*Hashrate*": "",
                "15 min": "%s%s" % (resp_json['data']['shares_15m'], resp_json['data']['shares_15m_unit']),
                "1 day": "%s%s" % (resp_json['data']['shares_1d'], resp_json['data']['shares_1d_unit']),
            }
