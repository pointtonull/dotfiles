Vim�UnDo� �$��g_����aRj醁�;H�x���]�   '              ,   /          /   /    `8�#    _�       -           ,           ����                                                                                                                                                                                                                                                                                                                                                             `8��     �                 import fastavro5�_�   ,   .           -           ����                                                                                                                                                                                                                                                                                                                                                             `8��     �         %    �         %    5�_�   -   /           .           ����                                                                                                                                                                                                                                                                                                                                                             `8��    �         &    5�_�   .               /           ����                                                                                                                                                                                                                                                                                                                                                             `8�"     �               '   	import os   !from itertools import zip_longest       import fastavro   )from smart_open import open as smart_open           6ENVIRONMENT_NAME = os.environ["MICROCOSM_ENVIRONMENT"]           )def chunker(iterable, n, fillvalue=None):       """   2    Splits ``iterable`` into chunks of size ``n``.   K    If ``fillvalue`` is provided, it'll be used as padding to fill the last   O    chunk, assuring all chunks have the same length. Else, the last chunk might       be shorter.       """       args = [iter(iterable)] * n   4    chunks = zip_longest(*args, fillvalue=fillvalue)       for chunk in chunks:   !        yield filter(None, chunk)           def get_service_url(service):       """   N    Returns a formatted URL for the given service, in the correct environment.       """   F    service_url = f"https://{service}.{ENVIRONMENT_NAME}.globality.io"       return service_url           def iter_avro_file(filepath):       """       Simple s3/avro abstraction       """   )    file_obj = smart_open(filepath, "rb")   &    reader = fastavro.reader(file_obj)       for record in reader:           yield record5��