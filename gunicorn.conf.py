import multiprocessing, netifaces                                                                                                                                                                                         

info = netifaces.ifaddresses('eth0')

bind = info[2][0]['addr']

workers = multiprocessing.cpu_count() * 2 + 1                                                                                                                                                                  

wsgi_app = 'run:app'

reload = True
