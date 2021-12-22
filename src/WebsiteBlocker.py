def WebsiteBlocker():
    from ProofOS import ProofOS
    from CreateFile import CreateFile
    from WebsiteUnblocker import WebsiteUnblocker
    import pymsgbox
    ProofOS()
    CreateFile()
    Sites = open("SitesToBlock.txt", "r").readlines()
    with open(ProofOS.Host, "r+") as HostFile:
        Hosts = HostFile.read()
        for Site in Sites:
            if Site not in Hosts:
                HostFile.write("127.0.0.1 " + Site + ProofOS.nl)
                pymsgbox.alert("Successfully blocked site " + Site, title="WebsiteBlocker")
            else:
                pymsgbox.alert("ERROR : site " + Site + " is already blocked!", title="ERROR")
