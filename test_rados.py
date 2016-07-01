import rados

cluster = rados.Rados(conffile='ceph.conf')
cluster.connect()

cluster_stats = cluster.get_cluster_stats()

for key, value in cluster_stats.iteritems():
	print key, value
