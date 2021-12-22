def ProofOS():
    import sys
    if sys.platform == "win32":
        ProofOS.Host = r"C:\Windows\System32\drivers\etc\hosts"
        ProofOS.nl = "\r\n"
    elif sys.platform == "linux" or sys.platform == "darwin":
        ProofOS.Host = "/etc/hosts"
        ProofOS.nl = "\n"
