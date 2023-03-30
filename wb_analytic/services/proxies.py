import os

from dotenv import load_dotenv

load_dotenv()

LOGIN_CANADA = str(os.getenv('LOGIN_CANADA'))
PASSWORD_CANADA = str(os.getenv('PASSWORD_CANADA'))

LOGIN_USA = str(os.getenv('LOGIN_USA'))
PASSWORD_USA = str(os.getenv('PASSWORD_USA'))

LOGIN_RUSSIA_SHRD = str(os.getenv('LOGIN_RUSSIA_SHRD'))
PASSWORD_RUSSIA_SHRD = str(os.getenv('PASSWORD_RUSSIA_SHRD'))

proxy_canada = {
    'https': f'http://{LOGIN_CANADA}:{PASSWORD_CANADA}@168.196.238.128:9567'
}

proxy_usa = {
    'https': f'http://{LOGIN_USA}:{PASSWORD_USA}@95.164.108.118:9924'
}

proxy_russia_shared = {
    'https': f'http://{LOGIN_RUSSIA_SHRD}:{PASSWORD_RUSSIA_SHRD}@91.188.240.10:9089'
}


proxies = [proxy_usa, proxy_russia_shared, proxy_canada]
times_sleeps = [1.23, 2.03, 3.3, 4.21, 5.5]
