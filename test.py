import psutil

def get_available_disk_space(path):
    """Возвращает доступное место на диске в байтах."""
    stats = psutil.disk_usage(path)
    return stats.free

val = get_available_disk_space('/')
print(val)