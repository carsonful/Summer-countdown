from dotenv import load_dotenv
import os 

load_dotenv()


sid = os.environ['SID']

csrf = os.environ['CSRF']

user = os.environ['USER']

weatherapikey = os.environ['WEATHERAPIKEY']

weathercity = os.environ['WEATHERCITY']







lst = []
lst.append(os.environ['carson'].split(","))
lst.append(os.environ['maya'].split(","))
lst.append(os.environ['tiffany'].split(","))
lst.append(os.environ['josh'].split(","))
lst.append(os.environ['varsha'].split(","))
lst.append(os.environ['vanessa'].split(","))
lst.append(os.environ['maddie'].split(","))
lst.append(os.environ['antonio'].split(","))
lst.append(os.environ['evren'].split(","))
lst.append(os.environ['micaela'].split(","))
lst.append(os.environ['kaitlin'].split(","))
