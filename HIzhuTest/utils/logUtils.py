#coding:utf-8
import logging
import datetime
timer = datetime.datetime.now().strftime('%Y-%m-%d')
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',datefmt = '%a ,%d %b %Y %H:%M:%S',filename="./logs/"+timer+"ApiRunlog.log",filemod='w')
logger = logging.getLogger(__name__)