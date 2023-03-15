# LOGIN = '9cocbg'
# PASSWORD = 'QJN879'

LOGIN_CANADA = 'kfbJ0z'
PASSWORD_CANADA = 'sZKrVv'

LOGIN_USA = 'HdENyd'
PASSWORD_USA = 'H40Nb6'

LOGIN_RUSSIA_SHRD = 'htRbXQ'
PASSWORD_RUSSIA_SHRD = '2b2Aew'

# proxy_russia = {
#     'https': f'http://{LOGIN}:{PASSWORD}@195.216.132.9:8000'
# }

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
