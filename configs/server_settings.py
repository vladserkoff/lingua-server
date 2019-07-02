# pylint: skip-file
import multiprocessing

bind = ":8000"

# multiprocess workers
worker_class = 'sync'
workers = multiprocessing.cpu_count() + 1

# approx number of requests serverd before restart
max_requests = 100000
max_requests_jitter = 100
graceful_timeout = 600

# max request execution time
timeout = 3600

# Do not limit the size of requests
limit_request_line = 0
limit_request_field_size = 0

# write access log to stdout
accesslog = '-'
