import time
import random
import logging
import requests

functions = {
    "login": {
        "url_suffix": "cgi-bin/lums_login.cgi",
        "method": "POST",
        "kargs": {
            "cmd": "loginauth",
            "username": "",
            "password": "",
            "uuid": ""
        }
    },
    "action_cam": {
        "url_suffix": "cgi-bin/lums_configuration.cgi",
        "method": "POST",
        "kargs": {
            "cmd": "campowerModeAction",
            "powermode": "",
            "uuid": ""
        }
    },
    "get_status": {
        "url_suffix": "power",
        "method": "POST",
        "kargs": {
            "cmd": "caminqpowermode",
            "uuid": ""
        }
    },
}

class VC_A7IP_A71PN:
    
    ip : str
    url : str
    
    def __init__(self, ip_cam : str, proxy : tuple=None):
        self.ip = ip_cam
        self.url = f"http://{ip_cam}/"
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Content-Type': 'application/json'
        }
        if proxy is not None:
            self.session.proxies = {
                'http': f'socks5://{proxy[0]}:{proxy[1]}',
                'https': f'socks5://{proxy[0]}:{proxy[1]}'
            }            
    
    def start_logger(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.logger.info("Logger started.")

    def gen_uuid(self):
        d = int(time.time() * 1000)
        uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'
        def replace_char(c):
            nonlocal d
            r = int((d + random.random() * 16)) % 16
            d = d // 16
            v = r if c == 'x' else (r & 0x3 | 0x8)
            return format(v, 'x')
        return ''.join(replace_char(c) if c in 'xy' else c for c in uuid)

    def login(self, username, password):
        url = self.url + functions["login"]["url_suffix"]
        data = {
            "cmd": "loginauth",
            'username': username,
            'password': password,
            'uuid': self.gen_uuid()
        }
        response = self.session.request(functions["login"]["method"], url, json=data)
        if response.status_code == 200:
            if "ERRCODE" in response.json():
                raise ValueError(f"Fail to login. Error code: {response.json()}")
            response = response.json()
            self.uuid = data["uuid"]
            cookies = {
                "langAge": "en",
                "userName": username,
                "passWord": password,
                "uuid": data["uuid"],
                "authority": "0",
                "vmsversion": response["vmsversion"],
                "vmsversionsub" : None
            }
            self.session.cookies.update(cookies)
            return response
        else:
            raise ValueError(f"Fail to login. Status code: {response.status_code}, response: {response.text}")
        
    def action_cam(self,
        action : str = "start",
    ):
        actions = {
            "start": "1",
            "stop": "0"
        }
        
        if action not in actions:
            raise ValueError(f"Invalid action: {action}")
        else:
            action = actions[action]
        
        url = self.url + "cgi-bin/lums_configuration.cgi"
        data = {
            "cmd": "campowerModeAction",
            "powermode": action,
            "uuid": self.uuid
        }
        print(f"Request URL: {url}")
        print(f"Request Data: {data}")
        #print(f"Cookies: {self.cookies}")
        response = self.session.post(url, json=data)
        print(response.status_code)
        print(response.text)
        return response.json()
    
    def move(self, direction) -> None:
        endpoint = self.url + "cgi-bin/lums_setpantilt.cgi"
        motion = {
            "home": "PT_HOME",
            "up": "PT_MOTOR_UP",
            "up_left": "PT_UP_LEFT",
            "up_right": "PT_UP_RIGHT",
            "down": "PT_MOTOR_DOWN",
            "down_left": "PT_DOWN_LEFT",
            "down_right": "PT_DOWN_RIGHT",
            "left": "PT_MOTOR_LEFT",
            "right": "PT_MOTOR_RIGHT",
            "stop": "PT_MOTOR_STOP",
        }
        if direction not in motion:
            raise ValueError(f"Invalid direction: {list(motion.keys())}")
        data = {
            "cmd": motion[direction],
            "uuid": self.uuid
        }
        if direction == "home":
            data["holding"] = "1"
        else:
            data["holding"] = "0"
        response = self.session.post(endpoint, json=data)
        print(response.status_code)
        print(response.text)
        return response.json()
    
    def zoom(self, zoom_value) -> None:
        self.endpoint = self.url + "cgi-bin/lums_setlens.cgi"
        response = self.session.post(self.endpoint, json={
            "cmd": "zoomdirect",
            "uuid": self.uuid,
            "value": zoom_value*766,
            "zoomUIVar": zoom_value
        })
        print(response.status_code)
        print(response.text)
        return response.json()
    
    def logout(self):
        url = self.url + "logout"
        response = requests.post(url)
        return response.json()

if __name__ == "__main__":
    cam = VC_A7IP_A71PN("192.168.100.100",("127.0.0.1", 6060))
    print(cam.login("admin", "admin"))
    cam.move("home")
    time.sleep(1)
    cam.move("stop")

    #cam.move("home")
    #cam.move("stop")
    #cam.zoom(1)
    #cam.zoom(10)
    #cam.zoom(1)

    for i in range(10):
        print(i, "up")
        cam.move("right")
        time.sleep(0.1)
        cam.move("stop")
        time.sleep(0.5)


    for i in range(2):
        print(i, "left")
        cam.move("left")
        time.sleep(0.1)
        cam.move("stop")
        time.sleep(1.5)
    #print(cam.action_cam("start"))
