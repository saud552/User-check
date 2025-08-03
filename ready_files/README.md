# 🤖 تطبيق البوتات المدمج - Telegram Bots Application

هذا المستودع يحتوي على بوتين تليجرام يعملان معاً:

## 🔧 البوتات المتضمنة

### 1. بوت إضافة الحسابات (`add.py`)
- إضافة وإدارة حسابات التليجرام
- تشفير بيانات الجلسات
- إدارة الفئات والتصنيفات
- فحص حالة الحسابات

### 2. بوت فحص اليوزرات (`User_check.py`)
- فحص وصيد اليوزرات المتاحة
- إنشاء قنوات لاختبار اليوزرات
- إدارة عمليات الصيد بشكل متزامن
- دعم أنماط مختلفة من اليوزرات

## 🚀 النشر على Render

### الطريقة الأولى: استخدام render.yaml (مُوصى بها)

1. **ادفع الكود إلى GitHub:**
   ```bash
   git add .
   git commit -m "إعداد المستودع للنشر على Render"
   git push origin main
   ```

2. **اذهب إلى [Render Dashboard](https://dashboard.render.com)**

3. **اضغط على "New +" ثم "Blueprint"**

4. **اختر المستودع من GitHub**

5. **سيتم قراءة ملف `render.yaml` تلقائياً وإعداد جميع متغيرات البيئة**

### الطريقة الثانية: الإعداد اليدوي

1. **إنشاء خدمة جديدة:**
   - اذهب إلى Render Dashboard
   - اضغط "New +" → "Web Service"
   - اربط مستودعك من GitHub

2. **إعدادات الخدمة:**
   - **Name:** `telegram-bots`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main.py`

3. **إضافة متغيرات البيئة:**

## 🔐 متغيرات البيئة المطلوبة

يجب إضافة المتغيرات التالية في إعدادات Render:

### متغيرات أساسية:
```
TG_API_ID=26924046
TG_API_HASH=4c6ef4cee5e129b7a674de156e2bcc15
BOT_TOKEN=7618405088:AAEikRuG-UXaLYqcrqGjgxf5k4V23U9kcAA
CHECK_BOT_TOKEN=7941972743:AAFMmZgx2gRBgOaiY4obfhawleO9p1_TYn8
ADMIN_IDS=985612253
```

### متغيرات التشفير:
```
ENCRYPTION_SALT=render_deployment_salt_2024
ENCRYPTION_PASSPHRASE=secure_passphrase_for_encryption
```

### متغيرات اختيارية:
```
DB_PATH=accounts.db
LOG_LEVEL=INFO
MAX_CONCURRENT_TASKS=10
SESSION_TIMEOUT=60
```

## 📁 هيكل المشروع

```
├── main.py                 # نقطة الدخول الرئيسية
├── add.py                  # بوت إضافة الحسابات
├── User_check.py           # بوت فحص اليوزرات
├── encryption.py           # وظائف التشفير المشتركة
├── accounts.db             # قاعدة البيانات (يتم إنشاؤها تلقائياً)
├── requirements.txt        # التبعيات المطلوبة
├── render.yaml            # إعدادات Render التلقائية
├── Dockerfile             # ملف Docker للبناء
└── README.md              # هذا الملف
```

## 🛠️ التطوير المحلي

### 1. تثبيت التبعيات:
```bash
pip install -r requirements.txt
```

### 2. إعداد متغيرات البيئة:
```bash
export TG_API_ID="26924046"
export TG_API_HASH="4c6ef4cee5e129b7a674de156e2bcc15"
export BOT_TOKEN="7618405088:AAEikRuG-UXaLYqcrqGjgxf5k4V23U9kcAA"
export CHECK_BOT_TOKEN="7941972743:AAFMmZgx2gRBgOaiY4obfhawleO9p1_TYn8"
export ADMIN_IDS="985612253"
```

### 3. تشغيل التطبيق:
```bash
python main.py
```

## 🔍 فحص الصحة

التطبيق يوفر endpoint للتحقق من حالة الخدمة:
- **URL:** `https://your-app.onrender.com/health`
- **استجابة صحيحة:** HTTP 200 مع `{"status": "healthy"}`

## 📝 الميزات

### بوت إضافة الحسابات:
- ✅ إضافة حسابات برقم الهاتف أو الجلسة
- ✅ تشفير بيانات الجلسات
- ✅ إدارة الفئات والتصنيفات
- ✅ فحص حالة الحسابات
- ✅ حذف وتحديث الحسابات

### بوت فحص اليوزرات:
- ✅ فحص اليوزرات المتاحة
- ✅ دعم أنماط مختلفة من اليوزرات
- ✅ إنشاء قنوات اختبار تلقائياً
- ✅ إدارة متزامنة للعمليات
- ✅ إيقاف مؤقت واستئناف العمليات

## ⚠️ ملاحظات مهمة

1. **الأمان:** جميع الجلسات مشفرة باستخدام مكتبة `cryptography`
2. **قاعدة البيانات:** يتم استخدام SQLite مع وضع WAL للأداء المحسن
3. **التزامن:** كلا البوتين يعملان بشكل متزامن دون تداخل
4. **المراقبة:** النظام يوفر تسجيل مفصل لجميع العمليات

## 🐛 استكشاف الأخطاء

### مشاكل شائعة:

1. **فشل في الاتصال بالتليجرام:**
   - تأكد من صحة `TG_API_ID` و `TG_API_HASH`
   - تحقق من اتصال الإنترنت

2. **خطأ في التوكن:**
   - تأكد من صحة `BOT_TOKEN` و `CHECK_BOT_TOKEN`
   - تحقق من أن البوتات نشطة في @BotFather

3. **مشاكل الأذونات:**
   - تأكد من أن `ADMIN_IDS` صحيح
   - تحقق من أن المستخدم مُدرج في قائمة الأدمن

## 📞 الدعم

في حالة وجود أي مشاكل أو استفسارات، يمكنك:
- فتح issue في GitHub
- مراجعة ملفات الـ logs للتشخيص
- التحقق من حالة الخدمة عبر `/health` endpoint

---

**تم تطوير هذا المشروع ليعمل بكفاءة على منصة Render مع دعم كامل للنشر التلقائي ومتغيرات البيئة.**