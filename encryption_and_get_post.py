from Crypto.Cipher import AES
import requests
import json
import hashlib
import datetime
import random
import string

code = "2020-04-22T13:55:03.808Z+09003b7a7c06-4e1c-46be-9845-6ab943baa15985643649115555558794402584531164025503click"

def Af_Data():
	url = "http://app.adjust.com/sdk_click"
	method = "POST"
	headers = {
			'Accept-Encoding': 'gzip',
			'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi K20 Pro MIUI/V10.3.3.0.PFKINXM)',
			'Content-Length': '1150',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Client-SDK': 'android4.14.0',
			'Authorization': 'Signature secret_id='+"114"+
			'signature='+str(hashlib.sha256(code.encode()).hexdigest())+
			'algorithm='+"sha256"+
			'headers='+"created_at gps_adid app_secret activity_kind"
		}
	params = {
			'android_uuid':	'b52024b9-b1d7-4fad-823a-e7e364e21a1c',
			'api_level':	'28',
			'app_token':	's4qpu9zf8f98',
			'app_version':	'8.19.0',
			'attribution_deeplink':	'1',
			'click_time':	'2020-04-22T13:53:19.000Z+0900',
			'connectivity_type':'1',
			'country':'	IN',
			'cpu_type':'arm64-v8a',
			'created_at':	'2020-04-22T13:55:03.808Z+0900',
			'device_manufacturer':	'Xiaomi',
			'device_name':	'Redmi K20 Pro',
			'device_type':	'phone',
			'display_height':	'2210',
			'display_width':	'1080',
			'environment':	'production',
			'event_buffering_enabled':	'0',
			'fb_id':	'2038c8ab-d0d0-42ad-8243-930af10acfed',
			'gps_adid':	'3b7a7c06-4e1c-46be-9845-6ab943baa159',
			'hardware_name':	'PKQ1.181121.001',
			'install_begin_time':	'2020-04-22T13:53:23.000Z+0900',
			'installed_at':	'2020-04-22T13:53:27.463Z+0900',
			'language'	:'en',
			'mcc':'	404',
			'mnc':	'11',
			'needs_response_details':	'1',
			'network_type'	:'10',
			'os_build':'PKQ1.181121.001',
			'os_name':'android',
			'os_version	':'9',
			'package_name':'com.zalora.android',
			'referrer':'utm_source=(not%20set)&utm_medium=(not%20set)',
			'screen_density':'high',
			'screen_format':'long',
			'screen_size':'normal',
			'sent_at':'2020-04-22T13:55:04.377Z+0900',
			'session_count':'1',
			'session_length':'0',
			'source':'install_referrer',
			'subsession_count':'1',
			'time_spent':	'0',
			'tracking_enabled':'1',
			'updated_at':'	2020-04-22T13:53:27.463Z+0900',
			'vm_isa':	'arm64'
		}
	
    #	some code to make reques
        response=requests.post(url,data=json.dumps({"data":[]}),headers=headers,params=params)

        # json.dumps(data,indent=2, sort_keys=True, default=str)

Af_Data()