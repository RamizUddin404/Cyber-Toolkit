import os
import time
import subprocess

class PhoneFullControl:
    def __init__(self):
        self.adb_path = self.find_adb()

    def find_adb(self):
        # Adjust the path as per your ADB installation
        adb_path = 'adb'
        return adb_path if self.check_adb(adb_path) else None

    def check_adb(self, adb_path):
        try:
            subprocess.run([adb_path, 'version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except Exception as e:
            print(f'ADB not found: {e}')
            return False

    def connect_device(self, device_ip):
        os.system(f'{self.adb_path} connect {device_ip}') 

    def disconnect_device(self, device_ip):
        os.system(f'{self.adb_path} disconnect {device_ip}') 

    def list_connected_devices(self):
        return subprocess.check_output([self.adb_path, 'devices']).decode().strip()

    def install_app(self, apk_path):
        os.system(f'{self.adb_path} install {apk_path} \n')

    def uninstall_app(self, package_name):
        os.system(f'{self.adb_path} uninstall {package_name}')

    def take_screenshot(self, output_path):
        os.system(f'{self.adb_path} exec-out screencap -p > {output_path}')

    def record_screen(self, output_path, duration):
        os.system(f'{self.adb_path} screenrecord {output_path} --time-limit {duration}')

    def send_sms(self, number, message):
        os.system(f'{self.adb_path} shell am start -a android.intent.action.SENDTO -d sms:{number} --es sms_body "{message}" --ez exit_on_sent true')

    def list_files(self, remote_path):
        return subprocess.check_output([self.adb_path, 'shell', 'ls', remote_path]).decode().strip()

    def pull_file(self, remote_path, local_path):
        os.system(f'{self.adb_path} pull {remote_path} {local_path}')

    def push_file(self, local_path, remote_path):
        os.system(f'{self.adb_path} push {local_path} {remote_path}')\n\nif __name__ == '__main__':
    phone_control = PhoneFullControl()
    phone_control.connect_device('192.168.1.1')  # Replace with the actual device IP
    # Add further functionality as required
