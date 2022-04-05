def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_leds("""
            # . . . .
                        . # . . .
                        . . # . .
                        . . . # .
                        . . . . #
        """)
    basic.clear_screen()
    if input.button_is_pressed(Button.B):
        basic.show_leds("""
            . . . . #
                        . . . # .
                        . . # . .
                        . # . . .
                        # . . . .
        """)
basic.forever(on_forever)
