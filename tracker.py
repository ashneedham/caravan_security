from modules.Gps import Gps
from modules.GoogleMaps import GoogleMaps
import sys
import requests
import time
import json

print('Booting GPS...')
gpsObj = Gps()
latLong = gpsObj.get_current_location()
mapObj = GoogleMaps(latLong['lat'], latLong['long'])
print('Uploading location data to server...')
postData = {
    'lat': latLong['lat'],
    'long': latLong['long'],
    'date': time.strftime("%Y-%m-%d %H:%M:%S")
}
postHeaders = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImY4NjFkZDNhYjA2MGU2N2IxOGFiZjc5ODgwYTBjN2E0NjQ4NzY5ZTk2MDNiZTBmZmRiYzA3MzYzZmQ5YTNmNjIyZDA5MjQ1Y2M4MWViN2Q3In0.eyJhdWQiOiI0IiwianRpIjoiZjg2MWRkM2FiMDYwZTY3YjE4YWJmNzk4ODBhMGM3YTQ2NDg3NjllOTYwM2JlMGZmZGJjMDczNjNmZDlhM2Y2MjJkMDkyNDVjYzgxZWI3ZDciLCJpYXQiOjE0ODc0Mjg4NTcsIm5iZiI6MTQ4NzQyODg1NywiZXhwIjoxNTE4OTY0ODU3LCJzdWIiOiIyIiwic2NvcGVzIjpbXX0.UaaTnNRzwWIxH9N6sAcEh1JSfBrwGMUA4ZmmE64GQAZ5vRxBiglTYpTkuHuYMblRMtu5l5WyuzAoUGgjoGlO04p_Qvdnck_A2300YFM6bWu8INoPqp6hOc3Us4_UsJ9pVvDFuzSzL-0iIV4p35XDQXv1lFI8XdsmUIjUnSM3EDrQTEvIM-jQBFTKHcP2PXdFdruCdigyy4HWKQVIHKb0PiwncCp0cSsWcSk07cSDb0S4dxqNyxABPw-pv07c3VDgCo_MutuKg3Y8YBzBdW1zq9SBOrVGC1-Rzg_SwccMA-PtG265r_kzgLsZ0dwA1rlbeARZSYfjxD80ISXIANL4LIBoKQ9kwynmCPbVT8Xe7zIWn1lcPZ4m1MMWaGPwQFsibRFvei0WTFUv2HYKQXdHP8f0K_agGXzje3CvyVf6nGGmqvHUo5eeNLRXpPu8SWOeBRAZASs1i-eeY9huX_OnrByeoSTnofBTs61up5ACnUQguYfY4Zxcb8pJHOLRqzEOD2d1E8qStLaa_93ncVz1Z3-IazQpIBcUwaNr7hTQqjbk4V_vXlt0Yglo2WznzkXW-0_DVIFXUB4EB00RvQY1KAJdZ4ZGG7rQVs5Fiux6T2hc4ZRiZaT2fOTUUagY0vsaYiEOiEx41K11bl9V6_sqsHs1Uo5e9OH8eDELoH5vlTg'
}
req = requests.post('http://gps.ashneedham.co.uk/api/v1/location', data=json.dumps(postData), headers=postHeaders)
print(req)
del gpsObj
del mapObj
del req
sys.exit()
