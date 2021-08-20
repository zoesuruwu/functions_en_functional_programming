# Block 1
from Resolve import Resolver

resolve = Resolver()
resolve.has_host("pluralsight.com")
# Block 2
resolve("pluralsight.com")
resolve.has_host("pluralsight.com")
# Block 3
resolve.clear()
resolve.has_host("pluralsight.com")
