# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:24:57 2024

@author: sherrins
"""

from shiny import App, ui, render

# Define UI layout
app_ui = ui.page_fluid(
    ui.h2("Hello, ShinyLive Dashboard!"),
    ui.input_slider("slider", "Slide me!", min=0, max=100, value=50),
    ui.output_text_verbatim("slider_value")
)

# Define server logic
def server(input, output, session):
    @output
    @render.text
    def slider_value():
        return f"Slider value: {input.slider()}"

# Create app
app = App(app_ui, server)

# Serve the app
app.run()