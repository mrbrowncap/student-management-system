from PyQt6.QtWidgets import QApplication, QVBoxLayout, QComboBox, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Calculator")
        grid = QGridLayout()

        # Create Widgets
        distance_label = QLabel("Distance:")
        self.distance_textbox = QLineEdit()

        self.combobox1 = QComboBox()
        self.combobox1.addItems(["Imperial (miles)", "Metric(km)"])

        time_label = QLabel("Time (hours):")
        self.time_textbox = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("here")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_textbox, 0, 1)
        grid.addWidget(self.combobox1, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_textbox, 1, 1)
        grid.addWidget(calculate_button, 2, 0)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_textbox.text())
        time = float(self.time_textbox.text())
        if self.combobox1.currentText() == "Imperial (miles)":
            speed = distance / time
            self.output_label.setText(f"Average Speed: {speed: .2f} mph")
        else:
            get_miles = distance / 1.609344
            speed = get_miles / time
            self.output_label.setText(f"Average Speed: {speed: .2f} mph")


app = QApplication(sys.argv)
speed_calc = SpeedCalculator()
speed_calc.show()
sys.exit(app.exec())
