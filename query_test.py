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

# req_api = "web.domain.list.short"
# query_data = {
#    # "per_page": 1000,
#    # "page": 2,
#    "domain": "770110.cc"
# }
# raw, jsonData, err = sdk.get(req_api, query = query_data)

req_api = "Web.Domain.add.batch"
post_data = {
    "domain": [
        "fdupay.com", "*.fdupay.com",
        "fdupayment.com", "*.fdupayment.com"
    ]
}
raw, jsonData, err = sdk.post(req_api, postData = post_data)

# req_api = "web.domain.set.get"
# query_data = {
#     "domain_id": "438459",
#     "group": ",".join([
#         "back_source_host",
#         "slice",
#         "cdn_advance_cache",
#         "page_gzip",
#         "WebP",
#         "page_optimization",
#         "ajax_load",
#         "all_view_optimization",
#         "mobile_jump",
#         "https",
#         "domain_proxy_conf",
#         "back_source_sni",
#         "browser_cache",
#         "upload_file",
#         "search_engine_optimization",
#         "hsts",
#         "websocket",
#         "resp_headers",
#         "customized_req_headers",
#         "diy_page_500",
#         "diy_page_502_or_504",
#         "diy_page_404",
#         "cloud_waf",
#         "waf_block_diy_page",
#         "anti_cc",
#         "source_site_protect",
#         "guest_auth"
#     ])
# }
# raw, jsonData, err = sdk.get(req_api, query = query_data)

print(jsonData)
print(err)


# new_domain_list = list(jsonData.get('data').get('list').keys())
# print(new_domain_list)
