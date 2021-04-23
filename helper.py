def save_image(image_url: str):
    filename = "temp/image.png"
    r = requests.get(image_url, stream = True)
    r.raw.decode_content = True

    with open(filename, "wb") as f:
        shutil.copyfileobj(r.raw, f)

    return filename

def get_file(file_name):
    with open(file_name, "rb") as f:
        return f
        
def parse_time(time: str):
    suffix = time[-1]
    time_number = int(time[:-1])

    if suffix == "s":
        return time_number
    elif suffix == "m":
        return time_number * 60
    elif suffix == "h":
        return time_number * 60 * 60
    else:
        return int(time)