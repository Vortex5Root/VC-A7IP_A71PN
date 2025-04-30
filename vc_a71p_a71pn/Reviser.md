
<h1 align="center">VC-A71P_A71PN</h1>

<p align="center">
    <a href="https://github.com/Vortex5Root/VC-A71P_A71PN/releases"><img alt="Dynamic TOML Badge" src="https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FVortex5Root%2FVC-A71P_A71PN%2Fmain%2Fpyproject.toml&query=%24.tool.poetry.version&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAAtFBMVEVHcEyWYTihdkuXYzrBjlqhbkHepWuzglG8hFGWYjmzglHepmz3z5iygVCWYjmWYjmxgVDsvorMlmDepmybaD2oe02ufU2leUzdpWqzglGfdUrgqnH616j%2F4LKWYjmvf1C3hVPepmyWYjmWZDuWYjmzglGWYjmwfk7fp22aZjz93a7VoGmpfFKdbEe4hlTFkFzwxZH30aDpuYO%2BnICUbUbGkl3jrnbjr3eSYjuuiWzNq4fjvI5PAatoAAAAJXRSTlMA4v34FBH4Jwwn4l8IXFG6%2FrWcv2PCZqdJxeX291Ci4uVQ5eQoZPLoqAAAAIxJREFUCNdFzscCgjAQBNA1JIAGVMDeW0iEAPb6%2F%2F9lCuqc9s1eBkDHpxTDN8E8mroJ9S1G0Sw7noSbrAMAHLvidshMERPwVlUuxF0Vb7ltgtdi5VUV%2BetcNAwZKyv%2BeP7J%2BD6VRaq5rKmiOUGoW3OzAzxEF2npLIgaGPbN1%2Bm07S4SjvkPOnjQI%2Bb4AGCaEYNClUKKAAAAAElFTkSuQmCC&label=Package%20Version"></a>
</p>

-------

<p align="center">
    <a href="https://github.com/Vortex5Root/VC-A71P_A71PN/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Vortex5Root/VC-A71P_A71PN.svg" alt="License">
    <a href="https://github.com/Vortex5Root/VC-A71P_A71PN/releases"><img src="https://img.shields.io/github/downloads/Vortex5Root/VC-A71P_A71PN/total.svg" alt="GitHub all releases"></a><br>
    <a href="https://github.com/Vortex5Root/VC-A71P_A71PN/network"><img src="https://img.shields.io/github/forks/Vortex5Root/VC-A71P_A71PN.svg" alt="GitHub forks"></a>
    <a href="https://github.com/Vortex5Root/VC-A71P_A71PN/stargazers"><img src="https://img.shields.io/github/stars/Vortex5Root/VC-A71P_A71PN.svg" alt="GitHub stars"></a>
    <a href="https://github.com/Vortex5Root/VC-A71P_A71PN/watchers"><img src="https://img.shields.io/github/watchers/Vortex5Root/VC-A71P_A71PN.svg" alt="GitHub watchers"></a><br>
    <a href="https://github.com/Vortex5Root/VC-A71P_A71PN/issues"><img src="https://img.shields.io/github/issues/Vortex5Root/VC-A71P_A71PN.svg" alt="GitHub issues"></a>
    <a href="https://github.com/Vortex5Root/VC-A71P_A71PN/pulls"><img src="https://img.shields.io/github/issues-pr/Vortex5Root/VC-A71P_A71PN.svg" alt="GitHub pull requests"></a>
    <a href="https://github.com/Vortex5Root/VC-A71P_A71PN/commits/master"><img src="https://img.shields.io/github/last-commit/Vortex5Root/VC-A71P_A71PN.svg" alt="GitHub last commit"></a><br>
</p>

<h2 align="center">Introduction</h2>

> This library is a Python package that provides the capability to interact with the VC-A71P and A71PN devices. It is designed to be simple and easy to use, making it accessible for developers of all skill levels. The library is built on top of the requests library, which allows for easy HTTP requests and responses.
> The library is designed to be easy to use and easy to understand. It is also designed to be easy to use with other libraries and frameworks. The library is built on top of the requests library, which allows for easy HTTP requests and responses.

<h2 align="center">Index</h2>

| Topic | sub-topic |
| --- | --- |
| [Dependencies](#dependencies) | |
| [Installation](#installation) | |
| [Documentation](#documentation) |  |
| [Acknowledgements](#acknowledgements) | |


<h2 align="center">Dependencies</h2>

| Name | Version | Description |
| --- | --- | --- |
| [![Linux](https://img.shields.io/badge/Linux-A81D33?style=for-the-badge&logo=linux&logoColor=ffffff)](https://www.linux.org/) | 5.14.0 | Linux is a family of open-source Unix-like operating systems based on the Linux kernel. |
| [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/) | >=3.11 | Python is an interpreted high-level general-purpose programming language. |
| [![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json?style=for-the-badge)](https://python-poetry.org/) | 1.1.8 | Poetry is a tool for dependency management and packaging in Python. |

<h2 align="center">Installation</h2>

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
```bash
poetry add git+https://github.com/Vortex5Root/VC-A71P_A71PN.git
```

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
```bash
pip install git+https://github.com/Vortex5Root/VC-A71P_A71PN.git#egg=VC-A71P_A71PN
```

<h2 align="center">Security Research</h2>

<h3 align="center">Login</h2>

<h4 align="center"> Web Requests Overview </h4>

```json
{
    "end_point": "http://192.168.100.100/cgi-bin/lums_login.cgi",
    "payload": {
        "cmd": "loginauth",
        "username": "admin",
        "password": "123",
        "uuid": "b943d2ba-5af8-409d-8877-2884091beedb"
    }
}
```

<h3 align="center"> Event Trigger </h3>

The login process is initiated through a `startLogin()` function that handles:
- User input validation
- Language selection
- UUID generation
- AJAX request to login endpoint
- Error handling and responses

<h3 align="center"> Connected Functions </h3>

```javascript
function generateUUID() {
    var d = new Date().getTime();
    if (typeof performance !== 'undefined' && typeof performance.now === 'function') {
        d += performance.now();
    }
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = (d + Math.random() * 16) % 16 | 0;
        d = Math.floor(d / 16);
        return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
    });
}
```

<h3 align="center">Live Interaction</h3>

<h4 align="center"> Motion Control </h4>

```json
{
    "end_point": "/cgi-bin/lums_setpantilt.cgi",
    "params": {
        "cmd": ["PT_MOTOR_LEFT", "PT_MOTOR_RIGHT", "PT_MOTOR_STOP", "PT_MOTOR_DOWN", "PT_MOTOR_UP", "PT_DOWN_RIGHT", "PT_DOWN_LEFT", "PT_UP_RIGHT", "PT_UP_LEFT"],
        "uuid": ""
    }
}
```

<h3 align="center"> Zoom Control </h3>

```json
{
    "end_point": "/cgi-bin/lums_setlens.cgi",
    "payload": {
        "cmd": "zoomdirect",
        "uuid": "ef69e0fc-5818-44ae-b1d5-fbe0ebde4b7b",
        "value": 766,
        "zoomUIVar": 2
    }
}
```

<h2 align="center">Acknowledgements</h2>

<p align="center">
    <br>[Coder]<br>
    <a href="https://github.com/Vortex5Root"><img src=https://avatars.githubusercontent.com/u/102427260?s=200&v=4 width=50 style="border-radius: 50%;"><br>Vortex5Root <br><b>        {Full-Stack Software Engineer}</b></a><br>
    <br>[Lab]<br>
    <a href="https://github.com/lunarring"><img src=https://avatars.githubusercontent.com/u/78172771?s=200&v=4 width=50 style="border-radius: 50%;"><br>LunarRing <br><b>        {MLCore in Champalimaud Foundation}</b></a><br><br>
</p>
