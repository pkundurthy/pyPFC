
import inspect, os

#print inspect.getfile(inspect.currentframe()) # script filename (usually with path)
modulePath = os.path.dirname( os.path.abspath(__file__ ) )
picklePath = modulePath+'/pickledData/'
