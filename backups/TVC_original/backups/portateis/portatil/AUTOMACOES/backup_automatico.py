#!/usr/bin/env python3
import os
print("\n📦 Backups disponíveis:")
if os.path.exists(os.path.expanduser("~/TVC4/BACKUPS")):
    for b in os.listdir(os.path.expanduser("~/TVC4/BACKUPS")):
        print(f"   {b}")
