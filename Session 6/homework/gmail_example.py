
from gmail import GMail, Message
from random import choice
import datetime
gmail = GMail('nguyen.giang100491@gmail.com','Thugiang123')

html_content = """
<p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
<p style="text-align: left;">Em ch&agrave;o thầy</p>
<p style="text-align: left;">T&ecirc;n em l&agrave; Tuấn Anh</p>
<p style="text-align: left;">H&ocirc;m nay em {{sickness}} em xin ph&eacute;p thầy cho em nghỉ 1 buổi học.&nbsp;</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">Tuấn Anh</p>
"""
# dùng choice để random
# place holder
sickness = ["chán đời", "mệt mỏi", "thiếu tiền"]
reason = choice(sickness) # lấy ngẫu nhiên ra 1 lí do
html_content_to_send = html_content.replace("{{sickness}}", reason)

current = datetime.datetime.now()
time = current.hour

msg = Message('Test Message',to='20130075@student.hust.edu.vn',html=html_content_to_send)

gmail.send(msg)

if time>7:
    gmail.send(msg)




