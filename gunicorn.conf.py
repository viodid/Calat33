import multiprocessing


workers = multiprocessing.cpu_count() * 2 + 1                                                                                                                                                                  

wsgi_app = 'run:app'

reload = True
