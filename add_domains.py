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

if __name__ == "__main__":
    domain_id_list = list()

    raw, jsonData, err = sdk.post("Web.Domain.add.batch", postData={
        "domain": ["ohoey.cn", "*.ohoey.cn", "tvdgi.cn", "*.tvdgi.cn"]
    })
    print(jsonData)
    print(err) if err else print("No Error.")

    if 16011 == jsonData.get('status').get('code'):
        print(jsonData.get('data').get('existDomains'))
        domains_str_list = ",".join(jsonData.get('data').get('existDomains'))

        raw, jsonData, err = sdk.get("web.domain.list.short", query={
           # "per_page": 1000,
           # "page": 2,
           "domains	": domains_str_list
        })
        print(jsonData)
        print(err) if err else print("No Error.")
        domain_id_list = [dd.get('id') for dd in jsonData.get('data').get('list')]
    else:
        domain_id_list = list(jsonData.get('data').get('list').keys())
    print(domain_id_list)
