import os
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.pdfgen import canvas
from PIL import Image

# 処理前フォルダのパスを設定する
input_folder = '処理前'

# 処理後フォルダのパスを設定する
output_folder = '処理後'

# 処理後フォルダが存在しない場合は作成する
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# 処理前フォルダにあるすべてのPDFファイルに対して処理を行う
for filename in os.listdir(input_folder):
    if filename.endswith('.pdf'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        cvs = canvas.Canvas(output_path)
        pdf = PdfReader(input_path, decompress=False).pages
        page = pagexobj(pdf[0])
        cvs.doForm(makerl(cvs, page))
        img = Image.open('./temp.png')
        cvs.drawInlineImage(img, 400, 519, 200, 190)
        cvs.showPage()
        cvs.save()
        os.remove(input_path)
