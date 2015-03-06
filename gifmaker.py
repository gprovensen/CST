def gifmaker():
    from moviepy.editor import *
    vid = (VideoFileClip()
        .subclip((1,22.65),(1,23.2))
        .resize(0.5))
        .crop(x1=150,x2=400)) 
    clip.write_gif("project.gif")
