import os, ini, requests

def downloadChar(name):
    mirrors = ["http://s3.wasabisys.com/webao/base/characters/",
            "http://s3.wasabisys.com/aov-webao/base/characters/",
            "http://s3.us-west-1.wasabisys.com/vanilla-assets/base/characters/"]
    
    for mirror in mirrors:
        print("trying "+mirror+name.lower()+"/"+"... ")
        a = requests.get(mirror+name.lower()+"/"+"char.ini")
        if not a.ok:
            print("ERROR")
            continue
        else:
            print("character exists on site")
            if not os.path.exists("base/characters/"+name): os.mkdir("base/characters/"+name)
            if not os.path.exists("base/characters/"+name+"/emotions"): os.mkdir("base/characters/"+name+"/emotions")
            open("base/characters/"+name+"/char.ini", "wb").write(a.content)
            open("ini.ini", "wb").write(a.content)
            
            total_emotes = ini.read_ini_int("ini.ini", "emotions", "number")
            print("%d total emotes" % total_emotes)
            for i in range(total_emotes):
                sound = ini.read_ini("ini.ini", "soundn", str(i+1), "1")
                emote = ini.read_ini("ini.ini", "emotions", str(i+1)).split("#")
                emotepre = emote[1]
                emoteanim = emote[2]

                if sound and sound != "1" and sound != "0" and sound != "-" and not os.path.exists("base/sounds/general/"+sound+".wav"):
                    print("[%d]" % (i+1), "attempting to download sound "+sound+"... ")
                    urlsound = requests.get(mirror+"sounds/general/"+sound.lower()+".wav")
                    if urlsound.ok:
                        print("OK!")
                        open("base/sounds/general/"+sound+".wav", "wb").write(urlsound.content)
                    else:
                        print("ERROR")

                if emotepre != "-":
                    download_missing_emote(mirror,name,"",emotepre,"gif")
                
                download_missing_emote(mirror,name,"(a)",emoteanim,"gif")
                download_missing_emote(mirror,name,"(b)",emoteanim,"gif")

                download_missing_emote(mirror,name,"",emoteanim,"png")

                if not os.path.exists("base/characters/"+name+"/emotions/button%d_off.png" % (i+1)):
                    button_off = requests.get(mirror+name.lower()+"/"+"emotions/button%d_off.png" % (i+1))
                    if button_off.ok:
                        print("[%d]" % (i+1), "downloaded button%d_off.png" % (i+1))
                        open("base/characters/"+name+"/emotions/button%d_off.png" % (i+1), "wb").write(button_off.content)

                if not os.path.exists("base/characters/"+name+"/emotions/button%d_on.png" % (i+1)):
                    button_on = requests.get(mirror+name.lower()+"emotions/button%d_on.png" % (i+1))
                    if button_on.ok:
                        print("[%d]" % (i+1), "downloaded button%d_on.png" % (i+1))
                        open("base/characters/"+name+"/emotions/button%d_on.png" % (i+1), "wb").write(button_on.content)

            char_icon = requests.get(mirror+name.lower()+"char_icon.png")
            if char_icon.ok:
                print("downloaded char_icon.png")
                open("base/characters/"+name+"/char_icon.png", "wb").write(char_icon.content)
            objection = requests.get(mirror+name.lower()+"objection.wav")
            if objection.ok:
                print("downloaded objection.wav")
                open("base/characters/"+name+"/objection.wav", "wb").write(objection.content)
            holdit = requests.get(mirror+name.lower()+"holdit.wav")
            if holdit.ok:
                print("downloaded holdit.wav")
                open("base/characters/"+name+"/holdit.wav", "wb").write(holdit.content)
            takethat = requests.get(mirror+name.lower()+"takethat.wav")
            if takethat.ok:
                print("downloaded takethat.wav")
                open("base/characters/"+name+"/takethat.wav", "wb").write(takethat.content)
            custom_gif = requests.get(mirror+name.lower()+"custom.gif")
            custom_wav = requests.get(mirror+name.lower()+"custom.wav")
            if custom_gif.ok:
                print("downloaded custom.gif")
                open("base/characters/"+name+"/custom.gif", "wb").write(custom_gif.content)
            if custom_wav.ok:
                print("downloaded custom.wav")
                open("base/characters/"+name+"/custom.wav", "wb").write(custom_wav.content)
            print("finished downloading character "+name)
            return

def download_missing_emote(url,charname,modifier,emotename,extension):
    emotepath = charname+"/"+modifier+emotename+"."+extension
    if not os.path.exists("base/"+emotepath):
        print("attempting to download "+emotepath)
        emotedownload = requests.get(url+emotepath.lower())
        if emotedownload.ok:
            print("OK!")
            open("base/characters/"+emotepath, "wb").write(emotedownload.content)
        else:
            print("ERROR")