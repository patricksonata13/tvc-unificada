#!/bin/bash
cd ~/TVC_STUDIOS
python3 PLATAFORMA_WEB/backend/app.py &
sleep 2
open http://localhost:5001
wait
