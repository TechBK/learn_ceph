import rados
import os

try:
    cluster = rados.Rados(conffile=os.path.abspath('ceph.conf'))
except TypeError as e:
    print 'Argument validation error: ', e
    raise e

print "Created cluster handle."

try:
    cluster.connect()
except Exception as e:
    print "connection error: ", e
    raise e
finally:
    print "Connected to the cluster."


print "\n\nI/O Context and Object Operations"
print "================================="

print "\nCreating a context for the 'data' pool"
if not cluster.pool_exists('data'):
    print "create data pool"
    cluster.create_pool('data')
    # raise RuntimeError('No data pool exists')
ioctx = cluster.open_ioctx('data')
#
# print "\nWriting object 'hw' with contents 'Hello World!' to pool 'data'."
# ioctx.write("hw", "Hello World!")
# print "Writing XATTR 'lang' with value 'en_US' to object 'hw'"
# ioctx.set_xattr("hw", "lang", "en_US")
#
#
# print "\nWriting object 'bm' with contents 'Bonjour tout le monde!' to pool 'data'."
# ioctx.write("bm", "Bonjour tout le monde!")
# print "Writing XATTR 'lang' with value 'fr_FR' to object 'bm'"
# ioctx.set_xattr("bm", "lang", "fr_FR")
#
# print "\nContents of object 'hw'\n------------------------"
# print ioctx.read("hw")
#
# print "\n\nGetting XATTR 'lang' from object 'hw'"
# print ioctx.get_xattr("hw", "lang")
#
# print "\nContents of object 'bm'\n------------------------"
# print ioctx.read("bm")
#
# print "Getting XATTR 'lang' from object 'bm'"
# print ioctx.get_xattr("bm", "lang")
#
#
# # print "\nRemoving object 'hw'"
# # ioctx.remove_object("hw")
# #
# # print "Removing object 'bm'"
# # ioctx.remove_object("bm")

print "Stats:"
print ioctx.get_stats()

# print "list object"
# print ioctx.list_objects()


# object_iterator = ioctx.list_objects()
# while True :
#
#     try :
#         rados_object = object_iterator.next()
#         print "Object contents = " + rados_object.read()
#
#     except StopIteration :
#         break

print "\nClosing the connection."
ioctx.close()

print "Shutting down the handle."
cluster.shutdown()
