import base64
import uuid

import helper.constant_helper as constant_helper
import helper.collection_helper as collection_helper

import wrapper.request_wrapper as request_wrapper
import wrapper.security_wrapper as security_wrapper


class BaseSDKService(object):
    '''

    '''

    def __init__(self, name):
        self.name = name

    def create(self, payload, action="create"):
        apimapopts = constant_helper.ConstantHelper.get_setting_constant().API_MAP.get(self.name)

        url = collection_helper.CollectioHelper.process_key_join(value=[constant_helper.ConstantHelper.get_setting_constant(
        ).API_BASE_URL, apimapopts.get(action).get("prefix"), apimapopts.get(action).get("endpoint")], separator="")
        headers = constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER
        params = {}
        attributes = payload

        token = "%(name)s:%(pass)s" % {
            "name": request_wrapper.request_wrapper.get_wrapper().key, "pass": request_wrapper.request_wrapper.get_wrapper().secret}
        headers.update({"authorization": "Basic " +
                        base64.b64encode(token.encode("utf-8")).decode('ascii')})

        headers.update(
            {"x-apikey": request_wrapper.request_wrapper.get_wrapper().key})

        if apimapopts.get(action).get("has_signature") is True:
            headers.update({"x-signature": security_wrapper.sucurity_wrapper.get_wrapper().process_hmac_signature(
                value=collection_helper.CollectioHelper.process_serialize_data(attributes), password=request_wrapper.request_wrapper.get_wrapper().secret)})

        return request_wrapper.request_wrapper.get_wrapper().process_axios_post(
            url=url, headers=headers, params=params, data=attributes)

    def get(self, id, action="get"):
        apimapopts = constant_helper.ConstantHelper.get_setting_constant().API_MAP.get(self.name)

        url = collection_helper.CollectioHelper.process_key_join(value=[constant_helper.ConstantHelper.get_setting_constant(
        ).API_BASE_URL, apimapopts.get(action).get("prefix"), apimapopts.get(action).get("endpoint")], separator="").replace("{id}", id)
        headers = constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER

        token = "%(name)s:%(pass)s" % {
            "name": request_wrapper.request_wrapper.get_wrapper().key, "pass": request_wrapper.request_wrapper.get_wrapper().secret}
        headers.update({"authorization": "Basic " +
                        base64.b64encode(token.encode("utf-8")).decode('ascii')})

        headers.update(
            {"x-apikey": request_wrapper.request_wrapper.get_wrapper().key})

        return request_wrapper.request_wrapper.get_wrapper().process_axios_get(
            url=url, headers=headers, params={})

    def get_by(self, by_key, by_value, swap_id=None, action="get"):
        apimapopts = constant_helper.ConstantHelper.get_setting_constant().API_MAP.get(self.name)

        url = collection_helper.CollectioHelper.process_key_join(value=[constant_helper.ConstantHelper.get_setting_constant(
        ).API_BASE_URL, apimapopts.get(action).get("prefix"), apimapopts.get(action).get("endpoint")], separator="").replace("{id}", str(uuid.uuid4()))
        headers = constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER
        params = {}

        params.update({by_key: by_value})
        if swap_id is not None:
            params.update({ "swap_id": swap_id })

        token = "%(name)s:%(pass)s" % {
            "name": request_wrapper.request_wrapper.get_wrapper().key, "pass": request_wrapper.request_wrapper.get_wrapper().secret}
        headers.update({"authorization": "Basic " +
                        base64.b64encode(token.encode("utf-8")).decode('ascii')})

        headers.update(
            {"x-apikey": request_wrapper.request_wrapper.get_wrapper().key})

        headers.update(
            {"content-type": "application/x-www-form-urlencoded"})

        return request_wrapper.request_wrapper.get_wrapper().process_axios_get(
            url=url, headers=headers, params=params)

    def save(self, id, payload, action="save"):
        apimapopts = constant_helper.ConstantHelper.get_setting_constant().API_MAP.get(self.name)

        url = collection_helper.CollectioHelper.process_key_join(value=[constant_helper.ConstantHelper.get_setting_constant(
        ).API_BASE_URL, apimapopts.get(action).get("prefix"), apimapopts.get(action).get("endpoint")], separator="").replace("{id}", id)
        headers = constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER
        attributes = payload

        token = "%(name)s:%(pass)s" % {
            "name": request_wrapper.request_wrapper.get_wrapper().key, "pass": request_wrapper.request_wrapper.get_wrapper().secret}
        headers.update({"authorization": "Basic " +
                        base64.b64encode(token.encode("utf-8")).decode('ascii')})

        headers.update(
            {"x-apikey": request_wrapper.request_wrapper.get_wrapper().key})

        if apimapopts.get(action).get("has_signature") is True:
            headers.update({"x-signature": security_wrapper.sucurity_wrapper.get_wrapper().process_hmac_signature(
                value=collection_helper.CollectioHelper.process_serialize_data(attributes), password=request_wrapper.request_wrapper.get_wrapper().secret)})

        return request_wrapper.request_wrapper.get_wrapper().process_axios_put(
            url=url, headers=headers, params={}, data=attributes)

    def delete(self, id, action="get"):
        apimapopts = constant_helper.ConstantHelper.get_setting_constant().API_MAP.get(self.name)

        url = collection_helper.CollectioHelper.process_key_join(value=[constant_helper.ConstantHelper.get_setting_constant(
        ).API_BASE_URL, apimapopts.get(action).get("prefix"), apimapopts.get(action).get("endpoint")], separator="").replace("{id}", id)
        headers = constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER
       
        token = "%(name)s:%(pass)s" % {
            "name": request_wrapper.request_wrapper.get_wrapper().key, "pass": request_wrapper.request_wrapper.get_wrapper().secret}
        headers.update({"authorization": "Basic " +
                        base64.b64encode(token.encode("utf-8")).decode('ascii')})

        headers.update(
            {"x-apikey": request_wrapper.request_wrapper.get_wrapper().key})

        return request_wrapper.request_wrapper.get_wrapper().process_axios_delete(
            url=url, headers=headers, params={})

    def fetch(self, filter={}, paging={"page": 1, "limit": 20}, action="fetch"):
        
        apimapopts = constant_helper.ConstantHelper.get_setting_constant().API_MAP.get(self.name)

        url = collection_helper.CollectioHelper.process_key_join(value=[constant_helper.ConstantHelper.get_setting_constant(
        ).API_BASE_URL, apimapopts.get(action).get("prefix"), apimapopts.get(action).get("endpoint")], separator="")
        headers = constant_helper.ConstantHelper.get_setting_constant().API_BASE_HEADER
        params = {**filter, **paging}

        token = "%(name)s:%(pass)s" % {
            "name": request_wrapper.request_wrapper.get_wrapper().key, "pass": request_wrapper.request_wrapper.get_wrapper().secret}
        headers.update({"authorization": "Basic " +
                        base64.b64encode(token.encode("utf-8")).decode('ascii')})

        headers.update(
            {"x-apikey": request_wrapper.request_wrapper.get_wrapper().key})

        return request_wrapper.request_wrapper.get_wrapper().process_axios_get(
            url=url, headers=headers, params=params)
