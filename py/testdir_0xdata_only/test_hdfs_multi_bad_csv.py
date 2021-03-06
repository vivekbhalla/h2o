import unittest, time, sys, random
sys.path.extend(['.','..','py'])
import h2o, h2o_cmd, h2o_hosts, h2o_browse as h2b, h2o_import as h2i

class Basic(unittest.TestCase):
    def tearDown(self):
        h2o.check_sandbox_for_errors()

    @classmethod
    def setUpClass(cls):
        # assume we're at 0xdata with it's hdfs namenode
        global localhost
        localhost = h2o.decide_if_localhost()
        if (localhost):
            h2o.build_cloud(1, use_hdfs=True, hdfs_version='cdh3', hdfs_name_node='192.168.1.176')
        else:
            h2o_hosts.build_cloud_with_hosts(1, use_hdfs=True, hdfs_version='cdh3', hdfs_name_node='192.168.1.176')

    @classmethod
    def tearDownClass(cls):
        h2o.tear_down_cloud()

    def test_hdfs_multi_bad_csv(self):
        print "\nUse the new regex capabilities for selecting hdfs: try *csv* at /datasets"
        # pop open a browser on the cloud
        ## h2b.browseTheCloud()
        # defaults to /datasets
        # path should default to /datasets

# One .gz in with non .gz seems to cause a stack trace..so don't match to all (*airlines*).
# no..maybe it's just the zero length gz file?. No it doesn't show up in the list of keys?
        parseResult = h2i.import_parse(path='datasets/airline_all.csv', hex_key='airlines_all.hex', timeoutSecs=600)
        print "*csv* regex to hdfs /datasets", 'parse time:', parseResult['response']['time']
        print "parse result:", parseResult['destination_key']
        sys.stdout.flush() 

if __name__ == '__main__':
    h2o.unit_main()
