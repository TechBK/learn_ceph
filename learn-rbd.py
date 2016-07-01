import rbd

import rados
import os

try:
    cluster = rados.Rados(conffile=os.path.abspath('ceph.conf'))
except TypeError as e:
    print 'Argument validation error: ', e
    raise e

# print "Created cluster handle."

try:
    cluster.connect()
except Exception as e:
    print "connection error: ", e
    raise e
# finally:
    # print "Connected to the cluster."


if not cluster.pool_exists('pool1'):
    # print "create data pool"
    # cluster.create_pool('data')
    raise RuntimeError('No data pool exists')


ioctx = cluster.open_ioctx('pool1')

diffs = []
def interate_cd(offset, length, exists):
    # print "-------------------------"
    # print "offset: ", offset
    # print "length: ", length
    # print "exists: ", exists
    diffs.append({'offset': offset, 'length':length, 'exists': exists})



with rbd.Image(ioctx, 'binh') as image:
    with rbd.Image(ioctx, 'binh_dr') as image1:
        # print image.size()
        # print image1.size()
        snaps = image.list_snaps()
        # for snap in snaps:
        #     print snap
        # print image.size()
        image.diff_iterate(0, image.size(), 'snap1', interate_cd)
        # print diffs

        with open('test-diff', 'w') as file:
            for diff in diffs:
                # print type(image.read(diff['offset'], diff['length']))
                image1.write(image.read(diff['offset'], diff['length']), diff['offset'])

        image.close()
        image1.close()
ioctx.close()
cluster.shutdown()