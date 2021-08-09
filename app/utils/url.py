
def create_url(protocol: str, address: str, version: int, path: str):
    return protocol + "://" + address + f"/v{version}" + path