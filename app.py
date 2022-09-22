from distutils.debug import DEBUG
from flask import Flask, after_this_request,render_template,request,send_file
from pytube import YouTube
import os

app=Flask(__name__)

@app.route('/',methods=("GET","POST"))
def index():
    if request.method=="POST":
        yurl=request.form['yurl']
#        try:
        global yt
        yt=YouTube(str(yurl))
 """    except:
            return render_template('index.html',er=1)"""
        
        title=yt.title
        thumb=yt.thumbnail_url
        desc=yt.description
        res=[]
        ftypes=[]
        for i in yt.streams:
            r=str(i.resolution)
            f=str(i.type)
            if r not in res and r!='None':
                res.append(r)
            if f not in ftypes:
                ftypes.append(f)
        return render_template('index.html',resol=res,ftypes=ftypes,title=title,thumb=thumb,desc=desc[:100]+"...")
    return render_template('index.html')

@app.route('/downl',methods=['POST'])
def downl():
    try:
        form_r=request.form['resolution']
        form_f=request.form['format']
        if form_f=='video':
            download_path=yt.streams.filter(resolution=form_r)[0].download('/temp')
            
        else:
            download_path=yt.streams.filter(only_audio=True)[0].download()

        fname = download_path.split("//")[-1]
        
    except:
        return "Video Download Failed"

        
    return send_file(fname, as_attachment=True)    

if __name__=="__main__":
    app.run(debug=True)

#set FLASK_DEBUG=1-->To start in debug mode
