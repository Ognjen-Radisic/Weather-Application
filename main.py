import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

def on_entry_click(event):
    if city_entry.get() == 'Type name of the desired city..':
        city_entry.delete(0, 'end')
        city_entry.insert(0, '')
        city_entry.config(fg='black')


def on_entry_click_away(event):
    if city_entry.get() == '':
        city_entry.insert(0, 'Type name of the desired city..')
        city_entry.config(fg='grey')


def format_output(result):
    try:
        city_name = result['name']
        country = result['sys']['country']
        temp = result['main']['temp']
        weather_description = result['weather'][0]['description']
        final_string = '%s, %s\nTemperature: %s °C\n%s' % (city_name, country, temp, weather_description)
    except:
        final_string = "Something went wrong,\ntry typing name of the city again."
    return final_string


def get_weather_func(city):
    print(city)
    weather_api_key = 'copy_paste_your_api_key_here'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parameters = {'APPID': weather_api_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=parameters)
    result = response.json()
    label_result['text'] = format_output(result)


root = tk.Tk()
root.title('City weather forecast')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#32a852')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.2)
frame_top = tk.Frame(root, bg='#044014')
frame_top.place(relwidth=1, relheight=0.2)
frame_left = tk.Frame(root, bg='#07591d')
frame_left.place(relwidth=0.1, relheight=0.8, relx=0, rely=0.2)
frame_right = tk.Frame(root, bg='#07591d')
frame_right.place(relwidth=0.1, relheight=0.8, relx=0.9, rely=0.2)

label_top = tk.Label(frame_top, text='Your official weather forecast', font = ('Cooper black', 20))
label_top.place(relx=0.5, rely=0.25, relwidth=0.7, relheight=0.5, anchor='n')

city_entry = tk.Entry(frame, font = 40, fg='#AEACAC', bd=5)
city_entry.insert(0, 'Type name of the desired city..')
city_entry.bind('<FocusIn>', on_entry_click)
city_entry.bind('<FocusOut>', on_entry_click_away)
city_entry.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

search_button = tk.Button(frame, text='SEARCH WEATHER', font=50, command=lambda: get_weather_func(city_entry.get()))
search_button.place(relwidth=0.4, relheight=0.1, relx=0.3, rely=0.22)

label_result = tk.Label(frame, font=('Britanic Bold', 17), anchor = 'nw', justify = 'left')
label_result.place(relx=0.5, anchor='n', rely=0.42, relwidth=0.8, relheight=0.5)

# image on left frame
background_image = tk.PhotoImage(file='forest.png')
background_label = tk.Label(frame_left, image=background_image)
background_label.place(relwidth=1, relheight=1)
# image on right frame
background_image2 = tk.PhotoImage(file='forest.png')
background_label2 = tk.Label(frame_right, image=background_image2)
background_label2.place(relwidth=1, relheight=1)

root.mainloop()