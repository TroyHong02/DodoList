# needed for any cluster connection
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator

# needed to support SQL++ (N1QL) query
from couchbase.cluster import QueryOptions

# get a reference to our cluster
cluster = Cluster('couchbase://localhost', ClusterOptions(
  PasswordAuthenticator('DodoMan', 'p@ssw0rd')))

# get a reference to our bucket
cb = cluster.bucket('users')

# collection
coll = cb.collection('user_data')

# will insert a document into a collection and print the returned CAS value
print("\nUpsert CAS: ")
try:
    key = 'username'
    result = coll.upsert(key, 'user0')
    print(result.cas)
except Exception as e:
    print(e)

print("\nGet Result: ")
try:
    result = coll.get(key)
    print(result.content_as[str])
except Exception as e:
    print(e)