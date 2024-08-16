from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MenuProject):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_order.clicked.connect(lambda: self.order_screen())
        self.button_back.clicked.connect(lambda: self.main_screen())
        self.button_placeorder.clicked.connect(lambda: self.place_order())
        self.button_calculate.clicked.connect(lambda: self.calculate_total())

    # Navigation
    def main_screen(self):
        self.hide_order_screen()
        self.hide_bill_screen()
        self.label_title.setHidden(False)
        self.button_order.setHidden(False)
        self.line_main_screen.setHidden(False)
        self.label_welcome.setHidden(False)
        self.label_total_cost.clear()
        self.radio_10.setChecked(True)

    def hide_main_screen(self):
        self.label_title.setHidden(True)
        self.button_order.setHidden(True)
        self.line_main_screen.setHidden(True)
        self.label_welcome.setHidden(True)

    def order_screen(self):
        self.hide_main_screen()
        self.hide_bill_screen()
        self.label_title.setHidden(False)
        self.button_back.setHidden(False)
        self.label_steak.setHidden(False)
        self.label_spaghetti.setHidden(False)
        self.label_steakcost.setHidden(False)
        self.label_salad.setHidden(False)
        self.label_soda.setHidden(False)
        self.label_water.setHidden(False)
        self.label_icecream.setHidden(False)
        self.label_spagcost.setHidden(False)
        self.label_saladcost.setHidden(False)
        self.label_sodacost.setHidden(False)
        self.label_watercost.setHidden(False)
        self.label_icecreamcost.setHidden(False)
        self.button_placeorder.setHidden(False)
        self.input_steak.setHidden(False)
        self.input_spag.setHidden(False)
        self.input_salad.setHidden(False)
        self.input_soda.setHidden(False)
        self.input_water.setHidden(False)
        self.input_icecream.setHidden(False)
        self.label_item.setHidden(False)
        self.label_price.setHidden(False)
        self.label_amountordered.setHidden(False)
        self.line_order_screen.setHidden(False)

    def hide_order_screen(self):
        self.label_title.setHidden(True)
        self.button_back.setHidden(True)
        self.label_steak.setHidden(True)
        self.label_spaghetti.setHidden(True)
        self.label_steakcost.setHidden(True)
        self.label_salad.setHidden(True)
        self.label_soda.setHidden(True)
        self.label_water.setHidden(True)
        self.label_icecream.setHidden(True)
        self.label_spagcost.setHidden(True)
        self.label_saladcost.setHidden(True)
        self.label_sodacost.setHidden(True)
        self.label_watercost.setHidden(True)
        self.label_icecreamcost.setHidden(True)
        self.button_placeorder.setHidden(True)
        self.input_steak.setHidden(True)
        self.input_spag.setHidden(True)
        self.input_salad.setHidden(True)
        self.input_soda.setHidden(True)
        self.input_water.setHidden(True)
        self.input_icecream.setHidden(True)
        self.label_item.setHidden(True)
        self.label_price.setHidden(True)
        self.label_amountordered.setHidden(True)
        self.line_order_screen.setHidden(True)
        self.label_ordered_error.setHidden(True)

    def bill_screen(self):
        self.hide_bill_screen()
        self.hide_main_screen()
        self.label_title.setHidden(False)
        self.label_bill.setHidden(False)
        self.label_item_bill.setHidden(False)
        self.label_steak_bill.setHidden(False)
        self.label_spaghetti_bill.setHidden(False)
        self.label_salad_bill.setHidden(False)
        self.label_soda_bill.setHidden(False)
        self.label_water_bill.setHidden(False)
        self.label_icecream_bill.setHidden(False)
        self.label_amountordered_bill.setHidden(False)
        self.label_tax.setHidden(False)
        self.label_tip.setHidden(False)
        self.label_total_bill.setHidden(False)
        self.label_total.setHidden(False)
        self.line_bill.setHidden(False)
        self.label_steak_ordered.setHidden(False)
        self.label_spag_ordered.setHidden(False)
        self.label_salad_ordered.setHidden(False)
        self.label_soda_ordered.setHidden(False)
        self.label_water_ordered.setHidden(False)
        self.label_icecream_ordered.setHidden(False)
        self.label_steak_total.setHidden(False)
        self.label_spag_total.setHidden(False)
        self.label_salad_total.setHidden(False)
        self.label_soda_total.setHidden(False)
        self.label_water_total.setHidden(False)
        self.label_icecream_total.setHidden(False)
        self.label_tax_total.setHidden(False)
        self.label_total_cost.setHidden(False)
        self.radio_10.setHidden(False)
        self.radio_15.setHidden(False)
        self.radio_20.setHidden(False)
        self.radio_25.setHidden(False)
        self.line.setHidden(False)
        self.button_back.setHidden(False)
        self.button_calculate.setHidden(False)

    def hide_bill_screen(self):
        self.label_bill.setHidden(True)
        self.label_item_bill.setHidden(True)
        self.label_steak_bill.setHidden(True)
        self.label_spaghetti_bill.setHidden(True)
        self.label_salad_bill.setHidden(True)
        self.label_soda_bill.setHidden(True)
        self.label_water_bill.setHidden(True)
        self.label_icecream_bill.setHidden(True)
        self.label_amountordered_bill.setHidden(True)
        self.label_tax.setHidden(True)
        self.label_tip.setHidden(True)
        self.label_total_bill.setHidden(True)
        self.label_total.setHidden(True)
        self.line_bill.setHidden(True)
        self.label_steak_ordered.setHidden(True)
        self.label_spag_ordered.setHidden(True)
        self.label_salad_ordered.setHidden(True)
        self.label_soda_ordered.setHidden(True)
        self.label_water_ordered.setHidden(True)
        self.label_icecream_ordered.setHidden(True)
        self.label_steak_total.setHidden(True)
        self.label_spag_total.setHidden(True)
        self.label_salad_total.setHidden(True)
        self.label_soda_total.setHidden(True)
        self.label_water_total.setHidden(True)
        self.label_icecream_total.setHidden(True)
        self.label_tax_total.setHidden(True)
        self.label_total_cost.setHidden(True)
        self.radio_10.setHidden(True)
        self.radio_15.setHidden(True)
        self.radio_20.setHidden(True)
        self.radio_25.setHidden(True)
        self.line.setHidden(True)
        self.button_back.setHidden(True)
        self.button_calculate.setHidden(True)

    def place_order(self):

        steak = self.input_steak.text()
        spag = self.input_spag.text()
        salad = self.input_salad.text()
        water = self.input_water.text()
        soda = self.input_soda.text()
        ice_cream = self.input_icecream.text()

        try:
            steak = float(steak)
            spag = float(spag)
            salad = float(salad)
            water = float(water)
            soda = float(soda)
            ice_cream = float(ice_cream)

            if steak < 0:
                self.label_ordered_error.setHidden(False)
            elif spag < 0:
                self.label_ordered_error.setHidden(False)
            elif salad < 0:
                self.label_ordered_error.setHidden(False)
            elif water < 0:
                self.label_ordered_error.setHidden(False)
            elif soda < 0:
                self.label_ordered_error.setHidden(False)
            elif ice_cream < 0:
                self.label_ordered_error.setHidden(False)
            else:
                self.label_ordered_error.setHidden(True)
                self.hide_order_screen()
                self.bill_screen()

                self.label_steak_ordered.setText(f'{steak:.0f}')
                self.label_spag_ordered.setText(f'{spag:.0f}')
                self.label_salad_ordered.setText(f'{salad:.0f}')
                self.label_water_ordered.setText(f'{water:.0f}')
                self.label_soda_ordered.setText(f'{soda:.0f}')
                self.label_icecream_ordered.setText(f'{ice_cream:.0f}')

                steak_cost = steak * 15.50
                self.label_steak_total.setText(f'${steak_cost:.2f}')
                spag_cost = spag * 12.75
                self.label_spag_total.setText(f'${spag_cost:.2f}')
                salad_cost = salad * 8.00
                self.label_salad_total.setText(f'${salad_cost:.2f}')
                soda_cost = soda * 5.00
                self.label_soda_total.setText(f'${soda_cost:.2f}')
                water_cost = water * 1.50
                self.label_water_total.setText(f'${water_cost:.2f}')
                icecream_cost = ice_cream * 6.50
                self.label_icecream_total.setText(f'${icecream_cost:.2f}')

                tax = (steak_cost + spag_cost + salad_cost + soda_cost + water_cost + icecream_cost) * 0.10
                self.label_tax_total.setText(f'${tax:.2f}')

                self.total = steak_cost + spag_cost + salad_cost + soda_cost + water_cost + icecream_cost + tax

                steak = self.input_steak.clear()
                spag = self.input_spag.clear()
                salad = self.input_salad.clear()
                water = self.input_water.clear()
                soda = self.input_soda.clear()
                ice_cream = self.input_icecream.clear()

        except ValueError:
            self.label_ordered_error.setHidden(False)


    def calculate_total(self):
        tip = 0.10
        if self.radio_15.isChecked():
            tip = 0.15
        elif self.radio_20.isChecked():
            tip = 0.20
        elif self.radio_25.isChecked():
            tip = 0.25

        final_tip = self.total * tip
        final_total = self.total + final_tip

        self.label_total_cost.setText(f'${final_total:.2f}')