# -*- coding: utf-8 -*-
"""

@author: Robert Dosa
"""

import dearpygui.core as dpg
from dearpygui.simple import menu_bar, menu
from caesar_lang_gen import encrypt, decrypt

# MAIN WINDOW SETTINGS

dpg.set_main_window_size(700, 900)
dpg.set_main_window_pos(500, 100)
dpg.set_main_window_title("Caesar Language-like Encryption")

# CALLBACK FUNCTIONS

text = ""
key = 0


def retrieve_callback_encrypt(sender, callback):
    global text
    global key
    text = dpg.get_value("encrypt")
    key = dpg.get_value("Key##key1")
    dpg.set_value("output_encrypt", encrypt(text, key))


def retrieve_callback_decrypt(sender, callback):
    global text
    global key
    text = dpg.get_value("decrypt")
    key = dpg.get_value("Key##key2")
    dpg.set_value("output_decrypt", decrypt(text, key))


def print_me(sender, data):
    dpg.log_debug(f"Menu Item: {sender}")


def file_picker_for_encryption(sender, data):
    dpg.open_file_dialog(callback=apply_selected_file_for_encryption, extensions=".*,.txt")


def file_picker_for_decryption(sender, data):
    dpg.open_file_dialog(callback=apply_selected_file_for_decryption, extensions=".*,.txt")


def apply_selected_file_for_encryption(sender, data):
    global text
    global key
    directory = data[0]
    file = data[1]
    file_path = f"{directory}\\{file}"
    with open(file_path) as file:
        text = file.read()
        key = dpg.get_value("Key##key1")
        dpg.set_value("output_encrypt", encrypt(text, key))
    # TODO implement creating new file with timestamp


def apply_selected_file_for_decryption(sender, data):
    global text
    global key
    directory = data[0]
    file = data[1]
    file_path = f"{directory}\\{file}"
    key = dpg.get_value("Key##key1")
    with open(file_path) as file:
        text = file.read()
        key = dpg.get_value("Key##key1")
        dpg.set_value("output_decrypt", decrypt(text, key))
    # dpg.set_value("output_encrypt", encrypt(text, key))
    # TODO implement creating new file with timestamp


def quit_program():
    pass


# WIDGETS AND SPACINGS


with menu_bar("Main Menu Bar"):
    with menu("File"):
        dpg.add_menu_item("Encrypt file", callback=file_picker_for_encryption)
        dpg.add_menu_item("Decrypt file", callback=file_picker_for_decryption)
        dpg.add_menu_item("Quit", callback=quit_program)

    dpg.add_menu_item("Help", callback=print_me)

dpg.add_spacing(count=4)

dpg.add_same_line(spacing=180)

dpg.add_text("***ENCRYPTION***")

dpg.add_spacing(count=4)

dpg.add_input_text("encrypt", multiline=True, label="Text to encrypt")

dpg.add_spacing(count=4)

dpg.add_slider_int("Key##key1", min_value=1, max_value=9, default_value=1)

dpg.add_spacing(count=8)

dpg.add_same_line(spacing=205)
dpg.add_button("Encrypt", callback=retrieve_callback_encrypt)

dpg.add_spacing(count=4)

dpg.add_input_text("output_encrypt", multiline=True, label="Encrypted text")

dpg.add_spacing(count=8)
dpg.add_separator()
dpg.add_spacing(count=8)

dpg.add_same_line(spacing=180)

dpg.add_text("***DECRYPTION***")

dpg.add_spacing(count=4)

dpg.add_input_text("decrypt", multiline=True, label="Text to decrypt")

dpg.add_spacing(count=4)

dpg.add_slider_int("Key##key2", min_value=1, max_value=9, default_value=1)

dpg.add_spacing(count=8)

dpg.add_same_line(spacing=205)
dpg.add_button("Decrypt", callback=retrieve_callback_decrypt)

dpg.add_spacing(count=4)

dpg.add_input_text("output_decrypt", multiline=True, label="Decrypted text")

if __name__ == "__main__":
    dpg.start_dearpygui()
