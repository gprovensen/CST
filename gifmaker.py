def gifmake():
    chs = pickAFile()
    vid = (VideoFileClip(chs))
    for f in vid:
        subclip((0, 3.5), (0, 4))
        resize(0.5)
        crop(x1=150, x2=400)
        print f
    clip.write_gif("project.gif")
