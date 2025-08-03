#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
نقطة الدخول الرئيسية لتشغيل البوتين معاً على Render
يتضمن البوت الأول (add.py) والبوت الثاني (User_check.py)
"""

import os
import sys
import asyncio
import logging
import signal
import time
from threading import Thread
from datetime import datetime

# إعداد المسار لاستيراد الملفات
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# إعداد التسجيل
logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'INFO'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

# متغيرات عامة لحالة التطبيق
app_running = True
health_status = True

class BotManager:
    """مدير البوتات للتحكم في تشغيل البوتين معاً"""
    
    def __init__(self):
        self.add_bot_task = None
        self.check_bot_task = None
        self.health_server_task = None
        
    async def start_add_bot(self):
        """تشغيل بوت إضافة الحسابات"""
        try:
            logger.info("🚀 بدء تشغيل بوت إضافة الحسابات...")
            
            # التحقق من التوكن قبل الاستيراد
            try:
                from config import BOT_TOKEN as ADD_BOT_TOKEN
                logger.info(f"🔑 بوت الإضافة - التوكن: {ADD_BOT_TOKEN[:20]}...")
                if not ADD_BOT_TOKEN or len(ADD_BOT_TOKEN) < 20:
                    raise ValueError("توكن بوت الإضافة غير صحيح")
            except:
                logger.error("❌ لم يتم العثور على توكن بوت الإضافة")
                return
            
            # استيراد بوت الإضافة
            import add
            
            # تشغيل البوت مع معالجة تضارب البوتات
            await add.main()
            
        except Exception as e:
            if "Conflict" in str(e):
                logger.error("⚠️ تضارب في بوت الإضافة - ربما يعمل بوت آخر بنفس التوكن")
                logger.info("💡 سيتم إيقاف بوت الإضافة مؤقتاً...")
                await asyncio.sleep(30)
            else:
                logger.error(f"❌ خطأ في بوت إضافة الحسابات: {e}")
                global health_status
                health_status = False
            
    async def start_check_bot(self):
        """تشغيل بوت فحص اليوزرات"""
        try:
            logger.info("🚀 بدء تشغيل بوت فحص اليوزرات...")
            
            # التحقق من التوكن قبل الاستيراد
            try:
                from config import CHECK_BOT_TOKEN
                logger.info(f"🔑 بوت الفحص - التوكن: {CHECK_BOT_TOKEN[:20]}...")
                if not CHECK_BOT_TOKEN or len(CHECK_BOT_TOKEN) < 20:
                    raise ValueError("توكن بوت الفحص غير صحيح")
            except:
                logger.error("❌ لم يتم العثور على توكن بوت الفحص")
                return
            
            # استيراد بوت الفحص
            import User_check
            
            # تشغيل البوت مع معالجة تضارب البوتات
            await User_check.main()
            
        except Exception as e:
            if "Conflict" in str(e):
                logger.error("⚠️ تضارب في بوت الفحص - ربما يعمل بوت آخر بنفس التوكن")
                logger.info("💡 سيتم إيقاف بوت الفحص مؤقتاً...")
                await asyncio.sleep(30)
            else:
                logger.error(f"❌ خطأ في بوت فحص اليوزرات: {e}")
                global health_status
                health_status = False
    
    async def health_check_server(self):
        """خادم فحص الصحة لـ Render"""
        from http.server import HTTPServer, BaseHTTPRequestHandler
        import threading
        
        class HealthHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/health':
                    if health_status:
                        self.send_response(200)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        response = {
                            "status": "healthy",
                            "timestamp": datetime.now().isoformat(),
                            "uptime": time.time() - start_time
                        }
                        self.wfile.write(str(response).encode())
                    else:
                        self.send_response(503)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        response = {"status": "unhealthy"}
                        self.wfile.write(str(response).encode())
                else:
                    self.send_response(404)
                    self.end_headers()
                    
            def log_message(self, format, *args):
                # إخفاء رسائل التسجيل للطلبات
                pass
        
        def run_server():
            port = int(os.getenv('PORT', 8080))
            server = HTTPServer(('0.0.0.0', port), HealthHandler)
            logger.info(f"🏥 خادم فحص الصحة يعمل على المنفذ {port}")
            server.serve_forever()
        
        # تشغيل الخادم في خيط منفصل
        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        
        # الحفاظ على المهمة نشطة
        while app_running:
            await asyncio.sleep(1)
    
    async def run_all_bots(self):
        """تشغيل جميع البوتات والخدمات"""
        try:
            logger.info("🌟 بدء تشغيل جميع الخدمات...")
            
            # بدء خادم فحص الصحة أولاً
            health_task = asyncio.create_task(self.health_check_server(), name="health_server")
            
            # انتظار قليل قبل بدء البوتات
            await asyncio.sleep(2)
            
            # تشغيل البوتات بشكل متتالي مع فترات انتظار
            logger.info("🤖 بدء تشغيل بوت الإضافة...")
            add_task = asyncio.create_task(self.start_add_bot(), name="add_bot")
            
            # انتظار 5 ثوانٍ قبل بدء البوت الثاني
            await asyncio.sleep(5)
            
            logger.info("🔍 بدء تشغيل بوت الفحص...")
            check_task = asyncio.create_task(self.start_check_bot(), name="check_bot")
            
            # انتظار جميع المهام
            tasks = [add_task, check_task, health_task]
            await asyncio.gather(*tasks, return_exceptions=True)
            
        except Exception as e:
            logger.error(f"❌ خطأ في تشغيل الخدمات: {e}")
            global health_status
            health_status = False

def signal_handler(signum, frame):
    """معالج الإشارات لإيقاف التطبيق بشكل صحيح"""
    global app_running
    logger.info(f"📟 تم استلام إشارة {signum}، إيقاف التطبيق...")
    app_running = False

def setup_environment():
    """إعداد متغيرات البيئة والتحقق من المتطلبات"""
    
    # محاولة استيراد الإعدادات من config.py
    try:
        from config import validate_config
        is_valid, missing_vars = validate_config()
        
        if not is_valid:
            logger.error(f"❌ متغيرات الإعداد المفقودة: {missing_vars}")
            logger.info("💡 سيتم استخدام القيم الافتراضية المضمنة في config.py")
        
        logger.info("✅ تم تحميل الإعدادات من config.py بنجاح")
        return True
        
    except ImportError:
        logger.warning("⚠️ لم يتم العثور على config.py، سيتم استخدام متغيرات البيئة")
        
        # التحقق من المتغيرات المطلوبة
        required_vars = [
            'TG_API_ID', 'TG_API_HASH', 'BOT_TOKEN', 
            'CHECK_BOT_TOKEN', 'ADMIN_IDS'
        ]
        
        missing_vars = []
        for var in required_vars:
            if not os.getenv(var):
                missing_vars.append(var)
        
        if missing_vars:
            logger.error(f"❌ متغيرات البيئة المفقودة: {missing_vars}")
            return False
        
        # إعداد المتغيرات الافتراضية
        os.environ.setdefault('DB_PATH', 'accounts.db')
        os.environ.setdefault('MAX_CONCURRENT_TASKS', '10')
        os.environ.setdefault('SESSION_TIMEOUT', '60')
        os.environ.setdefault('ENCRYPTION_SALT', 'default_salt')
        os.environ.setdefault('ENCRYPTION_PASSPHRASE', 'default_pass')
        
        logger.info("✅ تم إعداد متغيرات البيئة بنجاح")
        return True

async def main():
    """الدالة الرئيسية"""
    global start_time
    start_time = time.time()
    
    logger.info("🎯 بدء تشغيل تطبيق البوتات...")
    
    # إعداد معالجات الإشارات
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # إعداد البيئة
    if not setup_environment():
        logger.error("❌ فشل في إعداد البيئة")
        sys.exit(1)
    
    # إنشاء مدير البوتات
    bot_manager = BotManager()
    
    try:
        # تشغيل جميع الخدمات
        await bot_manager.run_all_bots()
        
    except KeyboardInterrupt:
        logger.info("⏹️  تم إيقاف التطبيق بواسطة المستخدم")
    except Exception as e:
        logger.error(f"❌ خطأ عام في التطبيق: {e}")
    finally:
        logger.info("🔚 تم إيقاف التطبيق")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("⏹️  تم إيقاف التطبيق")
    except Exception as e:
        logger.error(f"❌ خطأ في تشغيل التطبيق: {e}")
        sys.exit(1)