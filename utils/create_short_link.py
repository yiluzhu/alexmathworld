# This script creates a short link for our app at: https://ui-4imylu4s7a-ew.a.run.app

import requests


# Get web api key from: https://console.firebase.google.com/u/0/project/alex-maths-world/settings/general/
web_api_key = 'AIzaSyAaOYqWi-CvSqQ3GtcCi4qdTyGb1a3xIlg'

# Get web address from deployment of build.
# To build: gcloud builds submit --tag gcr.io/alex-maths-world/ui
# To deploy: gcloud beta run deploy --image gcr.io/alex-maths-world/ui --platform managed
web_address = 'https://ui-4imylu4s7a-ew.a.run.app/'
url = f'https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key={web_api_key}'

# domainUriPrefix can be created manually from firebase dynamic links:
# https://console.firebase.google.com/u/0/project/alex-maths-world/durablelinks/links/https:~2F~2Falexzhu.page.link
data = {
    "dynamicLinkInfo": {
        "domainUriPrefix": "https://alexzhu.page.link",
        "link": web_address,
    }
}
r = requests.post(url, json=data)

print(r.json())


# {'shortLink': 'https://alexzhu.page.link/y6N7', 'warning': [{'warningCode': 'UNRECOGNIZED_PARAM', 'warningMessage': 'There is no configuration to prevent phishing on this domain https://alexzhu.page.link. Setup URL patterns to whitelist in the Firebase Dynamic Links console. [https://support.google.com/firebase/answer/9021429]'}], 'previewLink': 'https://alexzhu.page.link/y6N7?d=1'}
