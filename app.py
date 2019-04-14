from flask import Flask, request, send_file
from flask import render_template
from predict_2 import *

app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('home.html')
global file_name
@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/articles')
# def articles():
#     return render_template('articles.html',text=texts)

@app.route('/')
def upload():
    return render_template('home.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    global file_name
    if request.method == 'POST':
        f = request.files['file']
        predicted = main(f)
    return '<h1>The predicted value is ' + str(predicted) + '</h1>'
#     #   file_name = f.filename
#     #   f.save('data/' + secure_filename(f.filename))
#     #   if '.pdf' in f.filename:
#     #      pdf_to_text(f.filename)
#     #   elif '.png' in f.filename or '.gif' in f.filename:
#     #      img_to_txt(f.filename)
#         pass
        
#     else:
#         return 'invalid file type'


# @app.route('/downloader')
# def downloader():
#    return send_file('C:/Users/Himanshu Prajapati/Downloads/Sampleproject/converted/'+ file_name[:-4]+'.txt')



if __name__ == '__main__':
    app.run(debug=True)