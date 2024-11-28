import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.main_window import Ui_MainWindow  # Import the converted UI file
from PySide6.QtCore import QDateTime, QThread, Signal

from utils import webserver
from fastapi.responses import HTMLResponse

import datetime
import uvicorn
import multiprocessing
import webbrowser
import os

# Redirect stdout and stderr to files if they are None
if not sys.stdout:
    sys.stdout = open(os.devnull, 'w')  # Suppress standard output
if not sys.stderr:
    sys.stderr = open("error.log", 'w')  # Log errors to a file

class WebServerProcess(multiprocessing.Process):
    def __init__(self, webserver_signal_queue, host="0.0.0.0", port=5000):
        super().__init__()
        self.webserver_signal_queue = webserver_signal_queue  # Queue to send signal to main process
        self.host = host
        self.port = port

    def run(self):
        @webserver.app.get("/",response_class=HTMLResponse)
        def dashboard():
            with open("dashboard.html") as html:
               html_content  = html.read()
            return HTMLResponse(content=html_content)
        @webserver.app.get("/cancel-shutdown")
        def cancel_shutdown():
            self.webserver_signal_queue.put("reset_timer")
        @webserver.app.get("/shutdown-now")
        def shutdown_now():
            os.system("shutdown /s /t 0") 

        # Start the web server using Uvicorn
        uvicorn.run(webserver.app, host=self.host, port=self.port)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setFixedSize(self.width(),self.height())
        
        self.button_arr = [self.ui.set_new_schedule_button,self.ui.predefined_hours_button,self.ui.predefined_minute_button,self.ui.predefined_days_button]

        # Set schedule time input to now
        self.ui.time_input_schedule.setDateTime(datetime.datetime.now())

        # Set schedule button
        self.ui.set_new_schedule_button.clicked.connect(self.schedule_new_shutdown_time)

        # Cancel Shutdown Time
        self.ui.cancel_shutdown_button.clicked.connect(self.reset_timer)

        # Create a queue for communication with the subprocess
        self.webserver_signal_queue = multiprocessing.Queue()

        # Start webserver in a separate process
        self.start_web_server()

        # Listen for the reset signal from the webserver
        self.listen_for_signal()
        
        # Define Preset Times
        self.ui.predefined_minute_button.clicked.connect(lambda:self.set_predefined_shutdown("M"))
        self.ui.predefined_hours_button.clicked.connect(lambda:self.set_predefined_shutdown("H"))
        self.ui.predefined_days_button.clicked.connect(lambda:self.set_predefined_shutdown("D"))
        
        # API server link
        self.ui.api_server_link_button.clicked.connect(lambda:webbrowser.open("http://127.0.0.1:5000"))

    def schedule_new_shutdown_time(self,preset_time = 0):
        """_summary_

        Args:
            preset_time (int, optional): Time in minutes . Defaults to 0.
        """
        if not preset_time:
            scheduler_datetime_input = self.ui.time_input_schedule
            scheduler_main_label = self.ui.scheduled_label_main
            if scheduler_datetime_input.dateTime().toPython() > datetime.datetime.now():
                scheduler_main_label.setText(scheduler_datetime_input.text())
                self.start_schedule_timer()
            else:
                QMessageBox.warning(self, "Cannot schedule", "Cannot schedule in past, I am not a time traveller! 😉")
        else:
            scheduler_main_label = self.ui.scheduled_label_main
            scheduled_shutdown_time = datetime.datetime.now() + datetime.timedelta(minutes=preset_time)
            scheduler_main_label.setText(str(scheduled_shutdown_time))
            self.start_schedule_timer(scheduled_shutdown_time)

    def start_schedule_timer(self,preset_time = None):
        if not preset_time:
            scheduler_datetime_input = self.ui.time_input_schedule
            self.countdown_thread = CountdownThread(scheduler_datetime_input.dateTime())
        else:
            scheduler_datetime_input = preset_time
            self.countdown_thread = CountdownThread(QDateTime.fromSecsSinceEpoch(int(scheduler_datetime_input.timestamp())))

        self.countdown_thread.time_left_updated.connect(self.update_time_display)
        
        # Disable all schedule buttons
        for button in self.button_arr: button.setDisabled(True)
        
        self.countdown_thread.start()

    def update_time_display(self, time_left):
        full_time = time_left.split(":")
        time_HH, time_MM, time_SS = full_time[0], full_time[1], full_time[2]
        self.ui.HH_timer_label.display(time_HH)
        self.ui.MM_timer_label.display(time_MM)
        self.ui.SS_timer_label.display(time_SS)

    def reset_timer(self):
        scheduler_main_label = self.ui.scheduled_label_main
        self.ui.HH_timer_label.display("0")
        self.ui.MM_timer_label.display("0")
        self.ui.SS_timer_label.display("0")
        scheduler_main_label.setText("NO SHUTDOWN SCHEDULED")
        for button in self.button_arr: button.setDisabled(False)
        self.countdown_thread.terminate()

    def listen_for_signal(self):
        # Listen for the reset signal from the subprocess
        def listen():
            while True:
                try:
                    signal = self.webserver_signal_queue.get()
                    if signal == "reset_timer":
                        self.reset_timer()
                except:
                    print("Could not reset the timer")

        import threading
        listener_thread = threading.Thread(target=listen)
        listener_thread.daemon = True
        listener_thread.start()

    def start_web_server(self):
        web_server_process = WebServerProcess(self.webserver_signal_queue)
        web_server_process.daemon = True 
        web_server_process.start()
        
    def set_predefined_shutdown(self,preset=str):
        if preset == "M":
            preset_data = self.ui.predefined_minute_combo.currentText()
            minutes = int(preset_data.split("m")[0])
            self.schedule_new_shutdown_time(minutes)
        if preset == "H":
            preset_data = self.ui.predefined_hours_combo.currentText()
            hours = int(preset_data.split("h")[0])
            self.schedule_new_shutdown_time(hours*60)
        if preset == "D":
            preset_data = self.ui.predefined_days_combo.currentText()
            days = int(preset_data.split("d")[0])
            self.schedule_new_shutdown_time(days*24*60)
            
        


class CountdownThread(QThread):
    time_left_updated = Signal(str)

    def __init__(self, end_time):
        super().__init__()
        self.end_time = end_time

    def run(self):
        while True:
            current_time = QDateTime.currentDateTime()
            time_left = self.end_time.toSecsSinceEpoch() - current_time.toSecsSinceEpoch()

            if time_left <= 0:
                self.time_left_updated.emit("00:00:00")
                os.system("shutdown /s /t 0") 
                break 

            hours = time_left // 3600
            minutes = (time_left % 3600) // 60
            seconds = time_left % 60

            self.time_left_updated.emit(f"{hours:02}:{minutes:02}:{seconds:02}")

            self.sleep(1)

if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    multiprocessing.set_start_method('spawn')
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())