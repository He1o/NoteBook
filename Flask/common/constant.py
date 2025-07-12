"""Define some constants."""
import logging
K_PRODUCTION = "PRODUCTION"
K_PRE = "PRE"
K_DEV = "DEV"
# thread pool
K_THREAD_POOL_MAX_WORKER = 5

# logging
K_LOGGING_SAVE_LOCAL = True
K_LOGGING_DIR = "/Users/didi/Code/logs"
K_LOGGING_LEVEL = logging.DEBUG
K_LOGGING_FORMAT = ("[%(levelname)s][%(asctime)s]"
                    "[%(filename)s:%(lineno)d:%(funcName)s]%(message)s")
K_HTTP_HANDLER = True  # True
K_HTTP_HANDLER_HOST = {
    K_PRODUCTION: '100.69.239.97:30919',
    K_PRE: '100.69.239.97:30571',
    K_DEV: '10.182.103.91:8888'
}
K_HTTP_HANDLER_URL = "/log/msgs"
K_HTTP_HANDLER_METHOD = "POST"
K_LOGGING_USE_PUBLIC = True

# public key
K_PUBLIC_KEY_SPEED = "prior_map_cloud_speed"
K_PUBLIC_KEY_SPEED_EVAL = "prior_map_cloud_speed_eval"
K_PUBLIC_KEY_MERGE_UPLOAD = "prior_map_cloud_merge_and_upload"
K_PUBLIC_KEY_TRAFFIC_NUM = "prior_map_cloud_traffic_num"
K_PUBLIC_KEY_TRAFFIC_NUM_EVAL = "prior_map_cloud_traffic_num_eval"

# Redis
K_REDIS_STARTUP_NODE = {
    K_PRODUCTION: {
        "host": "10.88.129.193",
        "port": 3100
    },
    K_DEV: {
        "host": "10.88.151.70",
        "port": 4200
    }
}
K_REDIS_MAX_ATTEMPTS = 1
K_REDIS_RETRY_PAUSE = 0  # second

EX_REDIS_SPEED = 24 * 60 * 60

K_IS_TO_MONGODB = True
K_IS_MINI_TO_MONGODB = True
K_TEST_CURRENT_TID = '20220802102'

K_HOST_ENV = {
    'hnb-prior-map-prod-pre-sf-e559b-1.docker.ys': K_PRODUCTION,
    'hnb-prior-map-prod-pre-sf-e559b-2.docker.ys': K_PRODUCTION,
    'hnb-prior-map-prod-pre-sf-e559b-4.docker.ys': K_PRODUCTION,
    'hna-prior-map-prod-online-sf-b10f6-0.docker.gz01': K_PRE,
    'hna-prior-map-prod-online-sf-b10f6-1.docker.gz01': K_PRE,
    'hna-prior-map-prod-online-sf-b10f6-2.docker.gz01': K_PRE
}

# threshold
# congest prob threshold. if congest prob > threshold, it's congested.
THRESHOLD_4_CONGEST = {
    'beijing_yizhuang': 0.080984,
    'guangzhou': 0.826964
}
# speed threshold. if speed < threshold, it's congested.
THRESHOLD_4_SPEED = 2.5
# zone threshold. if zone start coordinate
# of s-t > threshold, we think it works
THRESHOLD_4_ZONE = 25
