import sys

latest_values = {"humidity": "", "temperature": ""}
first_update = True  

def clear_lines(num_lines=2):
    if not first_update:  
        sys.stdout.write('\x1b[{}A\x1b[2K'.format(num_lines))
    else:
        sys.stdout.write('\n' * num_lines)  

def process_data(data):
    global latest_values, first_update

    if data.startswith('$HUMDITY'):
        value = data.split(',')[1]
        latest_values["humidity"] = value.strip()
    elif data.startswith('$TEMP'):
        value = data.split(',')[1]
        latest_values["temperature"] = value.strip()

    first_update = False  # 将 first_update 设置为 False，以便在下一次更新时清除行
    output_values()  

def output_values():
    clear_lines()  # 在每次输出之前清除之前的输出
    print(f"TEMP: {latest_values['temperature']}")
    print(f"HUMDITY: {latest_values['humidity']}")
