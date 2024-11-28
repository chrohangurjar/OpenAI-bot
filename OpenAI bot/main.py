import sys
import openai
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QTextEdit, QPushButton, QLabel

# Set up OpenAI API key
openai.api_key = "xxxxxxxxxxxxx"

class ChatGPTApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ChatGPT Desktop App")
        self.setGeometry(200, 200, 600, 400)

        # Layout
        layout = QVBoxLayout()

        # Chat Display
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display)

        # Input Text Area
        self.input_text = QTextEdit()
        layout.addWidget(self.input_text)

        # Submit Button
        self.submit_button = QPushButton("Ask ChatGPT")
        self.submit_button.clicked.connect(self.ask_chatgpt)
        layout.addWidget(self.submit_button)

        # Status Label
        self.status_label = QLabel("")
        layout.addWidget(self.status_label)

        # Set Layout
        self.setLayout(layout)

    def ask_chatgpt(self):
        user_input = self.input_text.toPlainText().strip()
        if not user_input:
            self.status_label.setText("Please enter a question!")
            return

        self.status_label.setText("Waiting for response...")
        QApplication.processEvents()  # Update UI immediately

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            reply = response['choices'][0]['message']['content']
            self.chat_display.append(f"**You:** {user_input}\n**ChatGPT:** {reply}\n")
            self.input_text.clear()
        except Exception as e:
            self.chat_display.append(f"Error: {str(e)}\n")
        finally:
            self.status_label.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat_app = ChatGPTApp()
    chat_app.show()
    sys.exit(app.exec_())
