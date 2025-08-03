# 🔧 متغيرات البيئة المطلوبة للبوتات

## ✅ تم إدراج جميع المتغيرات تلقائياً!

جميع متغيرات البيئة الموجودة في الملفات التالية:

### 📁 الملفات المحتوية على المتغيرات:
- `config.py` - الإعدادات الأساسية مع القيم الافتراضية
- `.env` - متغيرات البيئة للنشر
- `render.yaml` - إعدادات Render

---

## 🚀 المتغيرات المستخرجة من البوتين:

### 📱 متغيرات Telegram API:
```bash
TG_API_ID=26924046
TG_API_HASH=4c6ef4cee5e129b7a674de156e2bcc15
```

### 🤖 توكنز البوتات:
```bash
# بوت إضافة الحسابات (add.py)
BOT_TOKEN=7618405088:AAEikRuG-UXaLYqcrqGjgxf5k4V23U9kcAA

# بوت فحص اليوزرات (User_check.py)
CHECK_BOT_TOKEN=7941972743:AAFMmZgx2gRBgOaiY4obfhawleO9p1_TYn8
```

### 👤 إعدادات المدراء:
```bash
ADMIN_IDS=985612253
```

### 💾 إعدادات قاعدة البيانات:
```bash
DB_PATH=accounts.db
```

### 🔐 إعدادات التشفير:
```bash
ENCRYPTION_SALT=render_deployment_salt_2024
ENCRYPTION_PASSPHRASE=secure_passphrase_for_encryption
```

### ⚡ إعدادات الأداء:
```bash
MAX_CONCURRENT_TASKS=10
SESSION_TIMEOUT=60
VIEW_PAGE_SIZE=50
DEFAULT_PAGE_SIZE=5
```

### 📊 إعدادات التسجيل:
```bash
LOG_LEVEL=INFO
LOG_FILE=username_checker.log
```

### 🌐 إعدادات الخادم:
```bash
PORT=8080
```

### 📂 ملفات النظام:
```bash
CLAIMED_FILE=claimed_usernames.txt
FRAGMENT_FILE=fragment_usernames.txt
```

### 🔧 إعدادات متقدمة:
```bash
MIN_WAIT_TIME=0.5
MAX_WAIT_TIME=3.0
MAX_COOLDOWN_TIME=3600
EMERGENCY_THRESHOLD=300
ACCOUNT_CHECK_RATIO=0.3
```

---

## 📋 كيفية عمل النظام:

### 🔄 ترتيب أولوية تحميل المتغيرات:

1. **ملف `.env`** - يتم تحميله أولاً
2. **متغيرات البيئة من Render** - تُحدث القيم الموجودة
3. **القيم الافتراضية في `config.py`** - تُستخدم إذا لم تُعرّف المتغيرات

### 🎯 النتيجة:

- ✅ **لا حاجة لإعداد متغيرات يدوياً في Render**
- ✅ **البوتات ستعمل فوراً بالقيم المحددة**
- ✅ **إمكانية تخصيص القيم عبر متغيرات Render إذا أردت**
- ✅ **نظام fallback محكم للقيم الافتراضية**

---

## 🚀 للنشر على Render:

**الطريقة الأولى: نشر تلقائي (موصى بها)**
- فقط اربط المستودع بـ Render
- سيتم قراءة جميع الإعدادات تلقائياً

**الطريقة الثانية: تخصيص المتغيرات**
- أضف المتغيرات أعلاه في إعدادات Render
- ستُحدث القيم الافتراضية

---

**🎉 البوتات جاهزة للعمل فوراً دون أي إعداد إضافي!**