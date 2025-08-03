#!/bin/bash

# تصدير متغيرات البيئة من ملف .env
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# تشغيل التطبيق
python main.py