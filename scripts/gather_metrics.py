import subprocess

def get_metrics():
    commands = {
        'disk_usage': 'df -h',
        'memory_usage': 'free -m',
        'cpu_load': 'uptime',
        'processes': 'ps aux'
    }
    metrics = {}
    for key, cmd in commands.items():
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        metrics[key] = result.stdout
    return metrics

if __name__ == '__main__':
    metrics = get_metrics()
    with open('/home/ubuntu/ec2_metrics_python.txt', 'w') as f:
        for k, v in metrics.items():
            f.write(f"{k}:\n{v}\n")
