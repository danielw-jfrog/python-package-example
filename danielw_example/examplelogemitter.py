#!/usr/bin/env python3

### IMPORTS ###
import logging

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ExampleLogEmitter:
    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.info("Example Log Emitter Initialized")

    def emit(self):
        self.logger.info("Example Log Emitter Emission")
