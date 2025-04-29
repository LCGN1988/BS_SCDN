#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import logging
from pr2apisdk import Sdk

sdk = Sdk({
    "app_id": "632trw5o7p2Bo3R7KeK0", ## accesskey id
    "app_secert": "TxkeoVt0dt2C7pp908Ku3z732oxis132", ## accesskey secret
    "api_pre": "https://apiv4.lalcsafe.com/V4/", ## 调用地址前缀：https://apiv4.lalcsafe.com/V4/
    "timeout": 30,
})

req_api = "Web.Domain.remove"
post_data = {
    "domains": [
        "fdupay.com", "*.fdupay.com",
        "fdupayment.com", "*.fdupayment.com"
    ]
}
raw, jsonData, err = sdk.delete(req_api, postData = post_data)
print(jsonData)
print(err)
