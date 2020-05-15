#!/bin/bash

xfce4-session -V | cut -d " " -f 2 | head -n 1
