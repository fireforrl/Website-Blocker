def CreateFile():
    import os
    if not os.path.isfile("SitesToBlock.txt"):
        CreateFile.CreateFile = open("SitesToBlock.txt", "w")