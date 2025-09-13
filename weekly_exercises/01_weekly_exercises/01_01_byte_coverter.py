def converter_bytes():
    bytes_input = int(input("Give your input in bytes: "))

    kilobyte = 1024
    megabyte  = 1024 * 1024
    gigabyte  = 1024 * 1024 * 1024


    kb = bytes_input / kilobyte
    mb = bytes_input / megabyte
    gb = bytes_input / gigabyte


    print(f"bytes \t\t {bytes_input} B")
    print(f"Kilobytes\t {kb:.6f} KB")
    print(f"Megabytes\t {mb:.6f} MB")
    print(f"Gigabytes\t {gb:.6f} GB")

    
converter_bytes()
