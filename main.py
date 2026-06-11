import json
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

# 📱 Pure black theme aur automatic responsive screen setup
Window.clearcolor = get_color_from_hex('#000000')

class CopyAIApp(App):
    def build(self):
        self.title = "Copy AI"
        
        # 🔑 2026 Verified Config (Gemini 3.5 Flash)
        self.api_key = "AQ.Ab8RN6LniGrnAzffAK2kd5Yei12jcmT0pNfLc1IwSFy1k3DP8w"
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={self.api_key}"

        # Main Layout Setup
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # App Header Layout
        header = Label(
            text="[b]Copy AI[/b] 💬", 
            markup=True,
            font_size='26sp', 
            size_hint_y=None, 
            height=50,
            color=get_color_from_hex('#FFFFFF'),
            halign='left',
            valign='middle'
        )
        header.bind(size=header.setter('text_size'))
        main_layout.add_widget(header)

        # Scroll Window for Chat
        self.scroll_view = ScrollView(size_hint=(1, 0.75))
        self.chat_box = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        self.chat_box.bind(minimum_height=self.chat_box.setter('height'))
        
        # UI Welcome Screen Text
        welcome_text = Label(
            text="[color=888888]Hi User,[/color]\n[b]How can Copy AI help you today?[/b]",
            markup=True,
            font_size='22sp',
            size_hint_y=None,
            height=120,
            halign='center',
            valign='middle'
        )
        welcome_text.bind(size=welcome_text.setter('text_size'))
        self.chat_box.add_widget(welcome_text)
        
        self.scroll_view.add_widget(self.chat_box)
        main_layout.add_widget(self.scroll_view)

        # Chat Input Row
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, spacing=10)
        
        self.user_input = TextInput(
            hint_text="Ask Copy AI...",
            hint_text_color=get_color_from_hex('#666666'),
            background_color=get_color_from_hex('#1E1E1E'),
            foreground_color=get_color_from_hex('#FFFFFF'),
            multiline=False,
            font_size='16sp',
            padding=[15, 15, 15, 15],
            cursor_color=get_color_from_hex('#FFFFFF')
        )
        self.user_input.bind(on_text_validate=self.send_message)
        
        send_btn = Button(
            text="⚡",
            font_size='20sp',
            size_hint_x=None,
            width=60,
            background_color=get_color_from_hex('#333333'),
            color=get_color_from_hex('#FFFFFF')
        )
        send_btn.bind(on_press=self.send_message)

        input_layout.add_widget(self.user_input)
        input_layout.add_widget(send_btn)
        main_layout.add_widget(input_layout)

        return main_layout

    def send_message(self, instance):
        query = self.user_input.text.strip()
        if not query:
            return
            
        # Display user input in UI
        user_label = Label(
            text=f"[b]You:[/b] {query}",
            markup=True,
            font_size='16sp',
            size_hint_y=None,
            height=40,
            color=get_color_from_hex('#00FFCC'),
            halign='left'
        )
        user_label.bind(size=user_label.setter('text_size'))
        self.chat_box.add_widget(user_label)
        
        self.user_input.text = ""
        
        # Endpoint Integration
        payload = {"contents": [{"parts": [{"text": query}]}]}
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(self.url, headers=headers, data=json.dumps(payload))
            if response.status_code == 200:
                data = response.json()
                reply = data['candidates'][0]['content']['parts'][0]['text']
            else:
                reply = f"Error: Status {response.status_code}"
        except Exception as e:
            reply = f"Failed to connect: {str(e)}"
            
        # Display bot response
        bot_label = Label(
            text=f"[b]Copy AI:[/b] {reply}",
            markup=True,
            font_size='16sp',
            size_hint_y=None,
            color=get_color_from_hex('#FFFFFF'),
            halign='left'
        )
        bot_label.bind(size=bot_label.setter('text_size'))
        bot_label.height = max(60, len(reply) * 0.5)
        
        self.chat_box.add_widget(bot_label)
        self.scroll_view.scroll_to(bot_label)

if __name__ == '__main__':
    CopyAIApp().run()
      
