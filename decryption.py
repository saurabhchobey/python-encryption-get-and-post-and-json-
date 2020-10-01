from Crypto.Cipher import AES

key =b'24305c3a354951afe96d1800ad9299bf'

iv =b'heF9BATUfWuISyO8'
ciphered_data ='connection_type=wifi&app_name=MLB9Innings17&app_version=21&app_version_name=2.0.2&country_code=in&device_brand=Videocon&device_carrier=Jio+4G&device_cpu_type=armv8l&device_model=V502430&google_aid=b2753f4e-8aad-44dd-b7b6-823923eb5d67&google_ad_tracking_disabled=0&insdate=1495711043&installer=com.android.vending&install_referrer=utm_source%3D%28not+set%29%26utm_medium%3D%28not+set%29&language=en&mat_id=cc92c5ce-b617-4b6a-b1ce-596da5077425&mobile_country_code=405&mobile_network_code=872&os_version=6.0&screen_density=2.0&screen_layout_size=1280x720&sdk_version=3.11.4&conversion_user_agent=Dalvik%2F2.1.0+%28Linux%3B+U%3B+Android+6.0%3B+V502430+Build%2FMRA58K%29&currency_code=USD&revenue=0.0&system_date=1495711261  '
#ciphered_data=ciphered_data.encode()
cipher = AES.new(key, AES.MODE_CBC, iv)
original_data = cipher.encrypt(ciphered_data)
print(original_data.encode('hex'))
