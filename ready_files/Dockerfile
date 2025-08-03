# استخدام Python 3.11 الرسمي كصورة أساسية
FROM python:3.11-slim

# تعيين متغير البيئة لتجنب كتابة ملفات .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# تعيين دليل العمل
WORKDIR /app

# تحديث النظام وتثبيت الحزم المطلوبة
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# نسخ ملف المتطلبات وتثبيت التبعيات
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# نسخ الكود المصدري
COPY . .

# إنشاء مستخدم غير جذر للأمان
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

# تعيين المنفذ المطلوب
EXPOSE 8080

# تعيين متغيرات البيئة الافتراضية
ENV PORT=8080
ENV PYTHONPATH=/app

# فحص الصحة باستخدام Python
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')" || exit 1

# تشغيل التطبيق
CMD ["python", "main.py"]