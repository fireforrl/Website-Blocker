def WebsiteUnblocker():
    from ProofOS import ProofOS
    from CreateFile import CreateFile
    from WebsiteBlocker import WebsiteBlocker
    import pymsgbox
    CreateFile()
    Sites = open("SitesToBlock.txt", "r").readlines()
    with open(ProofOS.Host, "r+") as HostFile:
        Index = HostFile.readlines()
        HostFile.seek(0)
        for Line in Index:
            if not any(Site in Line for Site in Sites):
                HostFile.write(Line)
            HostFile.truncate()
    pymsgbox.alert("Successfully unblocked all sites!", title="WebsiteUnblocker")
