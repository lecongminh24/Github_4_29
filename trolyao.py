#truy cập, xử lí file hệ thống
import os
from unittest import result
#Chuyển văn bản thành âm thanh
from gtts import gTTS
#Mở âm thanh
import playsound
#Chuyển âm thanh thành văn bản
import speech_recognition
#Xử lí thởi gian
from time import strftime
import time
import datetime
#Chọn ngẫu nhiên
import random
#Truy cập web, trình duyệt
import re
import webbrowser
#Lấy thông tin từ web
import requests
import json
#Truy cập web, trình duyệt, hỗ trợ tìm kiếm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from youtube_search import YoutubeSearch
#Thư viện Tkinter hỗ trợ giao diện
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as mbox
#Thư viện wikipedia
import wikipedia


path=ChromeDriverManager().install()
root = Tk()
text_area = Text(root, height=26, width=45)
scroll = Scrollbar(root, command=text_area.yview)

def speak(text):
    print("Jarvis:  {}".format(text))
    text_area.insert(INSERT,"Jarvis: "+text+"\n")
    tts = gTTS(text=text, lang='vi', slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")

def get_audio():
    playsound.playsound("Ping.mp3", False)
    time.sleep(1)
    print("\nJarvis:  Đang nghe ...")
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("You: ")
        audio = r.listen(source, phrase_time_limit=6)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text.lower()
        except:
            print("\n")
            return

def hello():
    image1 = Image.open("image\\hacker1.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    day_time = int(strftime('%H'))
    if day_time < 11:
        speak("Chào buổi sáng tốt lành.Jarvis có thể giúp gì được cho bạn.")
    elif 11 <= day_time < 13:
        speak("Chào buổi trưa, bạn gọi Jarvis có việc gì không ạ")
    elif 13 <= day_time < 18:
        speak("Chào buổi chiều, Jarvis có thể giúp gì được cho bạn.")
    else:
        speak("Chào buổi tối tốt lành.Jarvis có thể giúp gì được cho bạn.")
    root.update()
    time.sleep(5)

def get_time(text):
    image1 = Image.open("image\\thoigian.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    now = datetime.datetime.now()
    now1 = datetime.datetime.now().strftime("%w")
    now2 = int(now1)
    now3 = "Chủ Nhật"
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút %d giây' % (now.hour, now.minute, now.second))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" % (now.day, now.month, now.year))
    elif "thứ" in text and now2!=0:
        speak('Hôm nay là thứ %s' % (now2+1))
    elif "thứ" in text and now2==0:
        speak('Hôm nay là %s' % (now3))
    else:
        speak("Tôi chưa hiểu ý của bạn. Bạn nói lại được không?")
        time.sleep(6)
    root.update()
    time.sleep(5)

def open_application(text):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    if "google" in text:
        speak("Mở Google Chrome")
        os.startfile(
            'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    elif "word" in text:
        speak("Mở Microsoft Word")
        os.startfile(
            'C:\Program Files\Microsoft Office\\root\Office16\\WINWORD.EXE')
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        os.startfile(
            'C:\Program Files\Microsoft Office\\root\Office16\EXCEL.EXE')
    elif "facebook" in text:
        webbrowser.open('https://www.facebook.com/',new=2)
        speak("Jarvis đã mở Facebook thành công!")
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
    root.update()
    time.sleep(6)

def open_website(text):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    reg_ex = re.search('mở website (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
    else:
        webbrowser.open("https://www.google.com/")
        speak("Trang web của bạn được mở.")
    root.update()
    time.sleep(5)

def open_google_and_search(text):
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    search_for = text.split("kiếm", 1)[1]
    speak('Jarvis đang tìm kiếm giúp bạn')
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element("xpath","//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
    root.update()
    time.sleep(5)

def weather(text):
    temp="Trời quang mây tạnh"
    if "moderate rain" in text:
        temp="Trời hôm nay có mưa vừa, bạn ra ngoài nhớ mang theo áo mưa" 
    elif "heavy intensity rain" in text or "thunderstorm with light rain" in text or "very heavy rain" in text:
        temp="Trời hôm nay có mưa rất lớn kèm theo giông sét, bạn nhớ đem ô dù khi ra ngoài" 
    elif "light rain" in text:
        temp="Trời hôm nay mưa nhẹ, rải rác một số nơi" 
    elif "heavy intensity shower rain" in text:
        temp="Trời hôm nay có mưa rào với cường độ lớn"
    elif "broken clouds" in text or "few clouds" in text:
        temp="Trời hôm nay có mây rải rác, không mưa"
    elif "overcast clouds" in text:
        temp="Trời hôm nay nhiều mây, u ám, dễ có mưa"
    elif "scattered clouds" in text:
        temp="Trời hôm nay có nắng, có mây rải rác"  
    if "rain" in text:
        image1 = Image.open("image\\thoitiet2.jpg")
        image_1 = ImageTk.PhotoImage(image1)    
        label1 = Label(image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)
    else :
        image1 = Image.open("image\\thoitiet1.jpg")
        image_1 = ImageTk.PhotoImage(image1)    
        label1 = Label(image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)
    return temp

def temperature(text):
    temp="mát mẻ"
    if text<15:
        temp="lạnh buốt giá"
    elif text<20:
        temp="khá lạnh"
    elif text<30:
        temp="mát mẻ"
    elif text<33:
        temp="khá nóng"
    else:
        temp="nóng bức"

    return temp

def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu vậy.")
    root.update()
    time.sleep(3)
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_audio()
    text_area.insert(INSERT,"You: "+city+"\n")
    if city=="":
        current_weather()
    else:
        api_key = "fe8d8c65cf345889139d8e545f57819a"
        call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
        response = requests.get(call_url)
        data = response.json()
        if data["cod"] != "404":
            city_res = data["main"]
            current_humidity = city_res["humidity"]
            current_temperature = city_res["temp"]
            temperature1=temperature(current_temperature)
            suntime = data["sys"]
            sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
            sunset = datetime.datetime.fromtimestamp(suntime["sunset"])

            weather_description = data["weather"][0]["description"]
            weather1=weather(weather_description)
            content = """
    -Thời tiết hôm nay {temperature} có nhiệt độ trung bình là {temp} độ C 
    -Độ ẩm là {humidity}%
    -{weather}
    -Mặt trời mọc vào {hourrise} giờ {minrise} phút
    -Mặt trời lặn vào {hourset} giờ {minset} phút.""".format(hourrise = sunrise.hour, minrise = sunrise.minute,
                                                            weather=weather1,temperature=temperature1,
                                                            hourset = sunset.hour, minset = sunset.minute, 
                                                            temp = current_temperature, humidity = current_humidity)
            speak(content)
            root.update()
            time.sleep(21)
        else:
            speak("Không tìm thấy địa chỉ của bạn")
            root.update()
            time.sleep(2)
            current_weather()
        
def sleep_time(x):
    if x==1:
        time.sleep(13)
    elif x==2:
        time.sleep(10)
    elif x==3:
        time.sleep(7)
    elif x==4:
        time.sleep(13)
    elif x==5:
        time.sleep(11)
    elif x==6:
        time.sleep(11)
    else :
        time.sleep(21)

def get_math():
    speak("Bạn nói phép tính đi, Jarvis sẽ giúp bạn.")
    root.update()
    time.sleep(4)
    text1=get_audio()
    text_area.insert(INSERT,"You: "+text1+"\n")
    root.update()
    image_1 = ImageTk.PhotoImage(Image.open("image\\math.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    if "+" in text1:
        text2=text1.replace("+", "-")
        try:
            math_a = re.search('(.+) -', text2)
            a = math_a.group(1)
            math_b = re.search('- (.+)', text2)
            b = math_b.group(1)
            c = float(a)+float(b)
            speak("Kết quả phép tính "+a+" cộng "+b+" là: "+str(c))
            root.update()
        except:
            speak("Phép tính không hợp lệ")
            root.update()
    elif "/" in text1 or "chia" in text1:
        text2=text1.replace("chia", "/")
        try:
            math_a = re.search('(.+) /', text2)
            a = math_a.group(1)
            math_b = re.search('/ (.+)', text2)
            b = math_b.group(1)
            c = float(a)/float(b)
            speak("Kết quả phép tính "+a+" chia "+b+" là: "+str(c))
            root.update()
            time.sleep(3)
        except:
            speak("Phép tính không hợp lệ")
            root.update()
    elif "x" in text1 or "nhân" in text1:
        text2=text1.replace("nhân", "x")
        try:
            math_a = re.search('(.+) x', text2)
            a = math_a.group(1)
            math_b = re.search('x (.+)', text2)
            b = math_b.group(1)
            c = float(a)*float(b)
            speak("Kết quả phép tính "+a+" nhân "+b+" là: "+str(c))
            time.sleep(2)
            root.update()
        except:
            speak("Phép tính không hợp lệ")
            root.update()
    elif "-" in text1:
        try:
            math_a = re.search('(.+) - ', text1)
            a = math_a.group(1)
            math_b = re.search(' - (.+)', text1)
            b = math_b.group(1)
            c = float(a)-float(b)
            speak("Kết quả phép tính "+a+" trừ "+b+" là: "+str(c))
            root.update()
        except:
            speak("Phép tính không hợp lệ")
            root.update()
    else:
        speak("Phép tính không hợp lệ")
        root.update()
    
    time.sleep(6)

def youtube_search():
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)

    speak('Xin mời bạn chọn tên để tìm kiếm trên youtube')
    root.update()
    time.sleep(3.5)
    text = get_audio()
    text_area.insert(INSERT,"You: "+text+"\n")
    root.update()
    if text == "":
        speak("Lỗi tìm kiếm. Do bạn chưa nói tên tìm kiếm.")
        root.update()
        time.sleep(4)
    else:
        result = YoutubeSearch(text, max_results = 10).to_dict()
        url = 'https://www.youtube.com' + result[0]['url_suffix']
        print(url)
        webbrowser.open(url)
        if "bài hát" in text:
            speak("Bài hát bạn yêu cầu đã được mở.")
        elif "phim" in text:
            speak("Bộ phim bạn yêu cầu đã được mở.")
        else:
            speak("Yêu cầu của bạn đã hoàn thành.")
        time.sleep(7)  

def func():
    image1 = Image.open("image\\trolyao.jpg")
    image_1 = ImageTk.PhotoImage(image1)    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    content="""
    Tôi có những chức năng sau đây:
    1.Chào hỏi
    2.Thông báo thời gian 
    3.Dự báo thời tiết 
    4.Thực hiện phép tính đơn giản 
    5.Mở ứng dụng,mở website 
    6.Tìm kiếm thông tin trên google 
    7.Mở nhạc,phim trên youtube 
    8.Tắt máy
    9.Khởi động lại máy
    10.Tạm biệt"""
    speak(content)
    root.update()
    time.sleep(23)


def color():
    mylist = ["#009999","black","green","grey","blue","orange","#cc0099","#00ff00","brown"]
    aa=random.choice(mylist)
    text_area.tag_add("here", "1.0", "100000.0")
    text_area.tag_config("here", background = aa)
    root.update()

def color1():
    mylist1 = ["yellow","#0000ff","white","#00ff00","black"]
    bb=random.choice(mylist1)
    text_area.tag_add("here", "1.0", "100000.0")
    text_area.tag_config("here",foreground = bb)
    root.update()

def info():
    mbox.showinfo("Giới thiệu", "-Nhấn Micro để bắt đầu thực hiện nói với AI.\n-Nhấn Làm mới để xóa toàn bộ cuộc trò chuyện.\n-Bạn có thể thay đổi màu nền hoặc màu chữ ngẫu nhiên.\n-Tiếng Pip xuất hiện là lúc AI đang nghe bạn nói.\n-Nói 'dừng lại' để tạm hoãn cuộc trò chuyện. \n-Nhấn Thoát để tắt chương trình.")

def r_set():
    image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
    label1 = Label(image=image_1)
    label1.image = image_1
    label1.place(x=7, y=43)
    text_area.delete("1.0", "1000000000.0")


def ham_main():
    r = speech_recognition.Recognizer()
    you=""
    ai_brain=""
    while True:
        with speech_recognition.Microphone() as source:
            playsound.playsound("Ping.mp3", False)
            time.sleep(1)
            print("Jarvis:  Dang nghe ...")
            audio = r.listen(source, phrase_time_limit=6)
            print("Jarvis:  ...")
        try:
            you = r.recognize_google(audio, language="vi-VN")
            print("\nYou: "+ you)	
            you = you.lower()
        except:
            ai_brain = "Tôi nghe không rõ. Bạn nói lại được không"
            print("\nJarvis: " + ai_brain)

        text_area.insert(INSERT,"You: "+you+"\n")
        root.update()

        if "xin chào" in you or "hello" in you:
            hello()
        elif "thời tiết" in you:
            current_weather()
        elif "ngày mấy" in you or "mấy giờ" in you or "thứ mấy" in you:
            get_time(you)
        elif "phép tính"in you or "tính " in you:
            get_math()
        elif "mở ứng dụng" in you or "mở phần mềm" in you:
            open_application(you)
        elif "mở website" in you:
            open_website(you)
        elif "mở google và tìm kiếm" in you:
            open_google_and_search(you)
        elif "nhạc" in you or "phim" in you or "mở youtube" in you or "bài hát" in you:
            youtube_search()
        elif "bạn có" in you and "chức năng" in you:
            func()
        elif "đổi màu nền" in you:
            color()
        elif "đổi màu chữ" in you:
            color1()
        elif "shut down" in you or "tắt máy" in you:
            os.system("shutdown -s")
        elif "restart" in you or "khởi động lại máy" in you:
            os.system("shutdown -r")
        elif "dừng lại" in you or "tạm dừng" in you :
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            break
        
        elif "hẹn gặp lại" in you or "tạm biệt" in you or "cảm ơn" in you:
            ai_brain="Rất vui khi giúp đỡ bạn. Hẹn gặp lại bạn sau."
            speak(ai_brain)
            root.update()
            time.sleep(4)
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            playsound.playsound("Ping.mp3", False)
            time.sleep(0.5)
            playsound.playsound("Ping.mp3", False)
            time.sleep(1)
            exit()

        else:
            ai_brain = "Tôi không nghe rõ gì cả !!!"
            speak(ai_brain)
            root.update()
            time.sleep(4)

        text_area.insert(INSERT,"_____________________________________________")
        you=""

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent) 
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Trợ Lý Jarvis")
        self.style = Style()
        self.style.theme_use("default")
        
        scroll.pack(side=RIGHT, fill=Y)
        text_area.configure(yscrollcommand=scroll.set)
        text_area.pack(side=RIGHT)

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        image3 = Image.open("image\\micro.png")
        image_3 = ImageTk.PhotoImage(image3)  
        label = Label(image=image_3)
        label.image = image_3
        label.place(x=430, y=477)

        closeButton = Button(self, text="Thoát",command = exit,width=10,fg="white", bg="#009999",bd=3)
        closeButton.pack(side=RIGHT, padx=11, pady=10)
        okButton = Button(self, text="Micro",command = ham_main,width=10,fg="white", bg="#009999",bd=3)
        okButton.pack(side=RIGHT, padx=11, pady=10)
        doimau = Button(self,text="Đổi màu nền",command = color,width=10,fg="white", bg="#009999",bd=3)
        doimau.pack(side=RIGHT,padx=11, pady=10)
        doimau = Button(self,text="Đổi màu chữ",command = color1,width=10,fg="white", bg="#009999",bd=3)
        doimau.pack(side=RIGHT,padx=11, pady=10)
        thongtin = Button(self,text="Giới thiệu",command = info,width=10,fg="white", bg="#009999",bd=3)
        thongtin.pack(side=RIGHT,padx=11, pady=10)
        lammoi = Button(self,text="Làm mới",command = r_set,width=10,fg="white", bg="#009999",bd=3)
        lammoi.pack(side=RIGHT,padx=11, pady=10)

        # self.pack(fill=BOTH, expand=1)   
        # Style().configure("TFrame", background="#333")
    
        image_1 = ImageTk.PhotoImage(Image.open("image\\trolyao.jpg"))    
        label1 = Label(self, image=image_1)
        label1.image = image_1
        label1.place(x=7, y=43)

        l = Label(root, text='Lịch sử trò chuyện', fg='White', bg='blue')
        l.place(x = 750, y = 10, width=120, height=25)
        l1 = Label(root, text='Hình ảnh minh họa', fg='yellow', bg='black')
        l1.place(x = 250, y = 11, width=120, height=25)

root.geometry("1000x510+250+50")
root.resizable(False, False)
app = Example(root)
root.mainloop()






