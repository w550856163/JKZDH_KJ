import os
import configparser
current_path =os.path.dirname(__file__)#获取config当前文件路径
config_file_path = os.path.join(current_path,'..','conf','localconfig.ini')#获取配置文件的路径

class ConfigUtils: #类封装、驼峰式命名法
    def __init__(self,cfg_path=config_file_path):
        self.cfg =configparser.ConfigParser()#创建一个配置文件对象
        self.cfg.read(cfg_path) #创建好后去读取cfg_path

    @property #这个如果不写requests.utils就获取不到
    def HOSTS(self):
        hosts_value = self.cfg.get('default','hosts') #获取节和key
        return hosts_value  #@property的属性名这里必须有下划线，不然会报错
#
local_config = ConfigUtils() #创建对象，测试代码
if __name__=='__main__':
    print(local_config.HOSTS)

