import subprocess
import re
# www.18k.icu
def get_wifi_profiles():
    try:
        command = r"netsh wlan show profiles"
        networks = subprocess.check_output(command, shell=True).decode('gbk', errors='ignore')
        wifi_names = re.findall(r":\s*(.+)", networks)
        return [name.strip() for name in wifi_names if "组策略配置文件" not in name]
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return []

def get_wifi_password(wifi_name):
    try:
        command = f'netsh wlan show profile name="{wifi_name}" key=clear'
        result = subprocess.check_output(command, shell=True).decode('gbk', errors='ignore')
        password = re.search(r"关键内容\s*:\s*(.*)|Key Content\s*:\s*(.*)", result)
        return password.group(1).strip() if password else None
    except subprocess.CalledProcessError as e:
        print(f"Error executing command for {wifi_name}: {e}")
        return None

def main():
    wifi_profiles = get_wifi_profiles()
    if not wifi_profiles:
        print("No Wi-Fi configurations found.")
        return
    for wifi in wifi_profiles:
        password = get_wifi_password(wifi)
        if password:
            print(f"WI-FI SSID: {wifi}\tPassword: {password}")
        else:
            print(f"Wi-Fi SSID: {wifi}\tPassword: ")

if __name__ == "__main__":
    main()
