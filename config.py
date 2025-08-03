#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ملف إعدادات المتغيرات لتطبيق البوتات
يحتوي على جميع المتغيرات المطلوبة لتشغيل البوتين
"""

import os
from pathlib import Path

# تحميل ملف .env إذا كان موجوداً
def load_dotenv():
    """تحميل متغيرات البيئة من ملف .env"""
    env_path = Path('.env')
    if env_path.exists():
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ.setdefault(key.strip(), value.strip())

# تحميل متغيرات البيئة
load_dotenv()

# === متغيرات Telegram API ===
TG_API_ID = int(os.getenv('TG_API_ID', '26924046'))
TG_API_HASH = os.getenv('TG_API_HASH', '4c6ef4cee5e129b7a674de156e2bcc15')

# === توكنز البوتات ===
BOT_TOKEN = os.getenv('BOT_TOKEN', '7618405088:AAEikRuG-UXaLYqcrqGjgxf5k4V23U9kcAA')
CHECK_BOT_TOKEN = os.getenv('CHECK_BOT_TOKEN', '7941972743:AAFMmZgx2gRBgOaiY4obfhawleO9p1_TYn8')

# === معرفات المدراء ===
ADMIN_IDS = [int(x) for x in os.getenv('ADMIN_IDS', '985612253').split(',') if x]

# === إعدادات قاعدة البيانات ===
DB_PATH = os.getenv('DB_PATH', 'accounts.db')

# === إعدادات التشفير ===
ENCRYPTION_SALT = os.getenv('ENCRYPTION_SALT', 'render_deployment_salt_2024')
ENCRYPTION_PASSPHRASE = os.getenv('ENCRYPTION_PASSPHRASE', 'secure_passphrase_for_encryption')

# === إعدادات الأداء ===
MAX_CONCURRENT_TASKS = int(os.getenv('MAX_CONCURRENT_TASKS', '10'))
SESSION_TIMEOUT = int(os.getenv('SESSION_TIMEOUT', '60'))
VIEW_PAGE_SIZE = int(os.getenv('VIEW_PAGE_SIZE', '50'))
DEFAULT_PAGE_SIZE = int(os.getenv('DEFAULT_PAGE_SIZE', '5'))

# === إعدادات التسجيل ===
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', 'username_checker.log')

# === إعدادات الخادم ===
PORT = int(os.getenv('PORT', '8080'))

# === ملفات النظام ===
CLAIMED_FILE = os.getenv('CLAIMED_FILE', 'claimed_usernames.txt')
FRAGMENT_FILE = os.getenv('FRAGMENT_FILE', 'fragment_usernames.txt')

# === إعدادات متقدمة ===
MIN_WAIT_TIME = float(os.getenv('MIN_WAIT_TIME', '0.5'))
MAX_WAIT_TIME = float(os.getenv('MAX_WAIT_TIME', '3.0'))
MAX_COOLDOWN_TIME = int(os.getenv('MAX_COOLDOWN_TIME', '3600'))
EMERGENCY_THRESHOLD = int(os.getenv('EMERGENCY_THRESHOLD', '300'))
ACCOUNT_CHECK_RATIO = float(os.getenv('ACCOUNT_CHECK_RATIO', '0.3'))

# === التحقق من المتغيرات المطلوبة ===
def validate_config():
    """التحقق من وجود جميع المتغيرات المطلوبة"""
    required_vars = {
        'TG_API_ID': TG_API_ID,
        'TG_API_HASH': TG_API_HASH,
        'BOT_TOKEN': BOT_TOKEN,
        'CHECK_BOT_TOKEN': CHECK_BOT_TOKEN,
        'ADMIN_IDS': ADMIN_IDS
    }
    
    missing_vars = []
    for var_name, var_value in required_vars.items():
        if not var_value or (isinstance(var_value, list) and len(var_value) == 0):
            missing_vars.append(var_name)
    
    if missing_vars:
        return False, missing_vars
    
    return True, []

# === قائمة جلسات البوتات (من User_check.py) ===
BOT_SESSIONS = [
    "1BJWap1sAUISyr-XZ8_ESa_LuEMv4gvrI1ZP0MQKTveHCCvRh7ZLHaLJPVlBExY6RHpc0yHu52TCK8Cqu3FoxKrOiGl2LdCHA6n1cVlFyan8N5_UWOAlYmRaagjODxJxlVF4XorGVI_Ml2RKcXvz71ZaBey9Y-K_Uofv-pHkN2nxG7cOdw45Dh-8Yr06Gg9b81wyUmfN0I8ZVlDsKlT68yup7zFU00VZbei6j7Ic2f8Y8So_rWCM2o8wKPwERR-mJ8A_ZOMjVinX8eFrkqbIxoYX52Si-K0z-c5jpHE2VLRsnqAhiR5iwnTc6iXbJTSUIwRzfrWbjuqVoyCZnwTUFfPfztgt-LcU=",
    "1BJWap1sAUFEHNUQuiQU71l3PH-MoiqWpoXpdbwR90edR9k8Y7PLGdi8nTU36WdsUP7JZAxL0T8Wo688OjYmE_5VTtGKYPIsavnQ7mOedpGFdADG_hmTp3d4CnEsc-yWZbgYc4_hN8xadUbCD6yrUoLvb_kcTN1S6GvL_hxckkMYwd14hyDj_SjxLTQe_lKd-wdkn9haFOwXBHNJ7XiSMSIXfig3tdmaJ8PWnGtUDM4XM-d_x2q0b8SYsGi702bAGX-ohwnYtnQKJW6lZ_VPxje23auSX67QR5y2p3bKIygXP6QMa4jBNT0G7EZSJmITSWNZlo32FfYHDlb9mw2SuMscnWLKNEG0=",
    "1BJWap1sAUH7UfXGeNoTKG4TR1Vkw89xwWzFOBwrv_n8Trlnf-klEMGJT-3ed3SoGVpZlNO9ImrGQrqGtViNbaM00PEu6soA-SGf8RU5LwXme9iw5mlTInX-sMJAqENbrIQc9JDtmkPLvPxIAY2jpGJ7JoxNtbVBbGHoo6QSkXJPBplBilqNpSL89RAH2kHjjoBe3z9xoRG1yjvh-zmgarPmoud0AJRa0neE1ssuRfOOE6J4rt0DMa127OogFFnKL6NgpjRH15KpRU_DboQUvhpVGt6mWmRJG4pW7UmbBqAf5BnMBMyEI3zcZGhf-a3Jjo4OdkVMJoEnKQDRsEF1w5nmfAXexud8=",
    "1BJWap1sAUFCCcN-1lqCyxL3PxZeUgH0LQFipkNsiQ9DyPOEHgsixt4VOA3GKSAqTFdC1BcyTi51GJlpEsuskJfdl7cnuZLPlQgMXQOKeJh8B_tylOv9EozMDGur4H8PhcNyHh3oC4pT6UQ_lDrXNtIk-_0z3m-QWyXjlor1kCBaBJCoqW4EhkEO52agErVzN1nfffAVC6YmKXS9B8laXFnXs72pPQii52na2Bx7oymX2UhKIUeolZWt7_iesJHZO7RedSGE-UoKt75vNghn6y-fq041R97hKzu60Ts9ZKCj8GGBo9chc29pNat3NSSO3KXBBBv6atSa3yM76dqfaROrdjzMtwb8=",
    "1BJWap1sAUDq3Pq6nlCgPC4dxOGGjwmI6MOfu9wK8I2yPuXbXyFRXhXKebBtrsBwZ0H_ilG3ab0F_50ePxjjuIiCjjy8gL8AOBFaHO0DMcZl81eWkhG9ogz28i_EvMPQslBKynrdyepq6k5o1j5HJ-zdiXth-fnEW8JS7Hm_Kik_5Jc082AzDiGbgFYGwWs8Qx3p8jQX8cegVitXSwH0lU--CvYWuz7psIeY8uWlFveYJRZ_fdJEfUWO0J1UEpYpo-WODAiVI6-1VdTzOJ6OMX5DHxi0yGPTQp8ruZ3NFEraSj4tFt3I3GgbeU96wjTG7XUQWZJDZInuiMKW-EWHX7SDgnuRpeAM=",
    "1BJWap1sAUJJ1_qUKh1Lg8zy4nenSyHEfZpa68GNtNEM-77644Dd7f_lRcJ0rpsJWoajhZQConiZ8cZgoq4briC-DBsnnRFyaBFz8BDuvriFdQRKrYA9WsDivQZafojHzsgeNoUpopylvtefTajmdss2tK_q6oaBCisn24_cI9SmwfgdDw2CMYCFI6j_kSgAGHLO71577eRXJfjAqnHz1nssi5Oph8-cWhJ3Csl6KEs_7rKYX5tWH5ZVD_XYpnV8nUr5jbSgBQxs1IgeAeQsT3SSn0ykxtWcVMbOOTLzqBlLu97xZqDBDnr8zkcc5MfNHBpjgLan_W4DbcGqRSLllMxeAtBLVOUU=",
    "1BJWap1sAUI-a0iDjLFzKjsvoNOpaOhlNt2ygPyLfU98C4Ob9R4kEVLSzprsuvpCbBwAswIKcQLMItqNLOMu4CElDbALBqPDl-o4694xoyXhc88r7DwlZPaqAjxngrg1i8SqdfgSdFpI3-0v_0sb_bjV2r12R5wSTl1jAWFQsWtg8uBhnj0u8F8pNoCMiR5NxpOlv4u8n9MHCfN4Ust0ZutClnZ9UZTilbmqZGJJRgoRhQwrfDNIjrSJgXxhuzBlJ82HD3B4WP7ZRBVI0PDBefzF0w81RMWxOTh0fQ_eVaWVlKSVXTv93JLZiaDStHYIsAojPksqc43RpF-x9EyK9DLzKMt2xnD0=",
    "1BJWap1sAUKA7tcITef_VI_xUQzrdk4ggX1sNfY4Z-qkmHiM51Asf86OHmVyerOiRs0mHWrjdWhraPxIrZd-6LBQLQn7DOqIoBiW_flH75QjgXbAE7wwaxMykQ6WKlO7rPdnSxJV-zeX9UGiaRtAxrP0_kLEZRe80y5pK0vmIns7_P18XeiX0YwjmnjDmT1qung65grtR9T0LtgSSOitit0x7_CayNYYOJ_WCnWr2ahF87kP1koss93qN9FzmrECaYffSRRYsvw0XeINqtu2V23FDUiPyNvSIshJDU0Omv2TGDsEttOKu9rgZjWZAiXV44W6j8WVtOLD6b3k2r3dKc1-KnGaBJWk="
]

# === إعدادات أجهزة Android (من add.py) ===
DEVICES = [
    {'device_model': 'Google Pixel 9 Pro', 'system_version': 'Android 15 (SDK 35)', 'app_version': 'Telegram Android 10.9.0', 'lang_code': 'en', 'lang_pack': 'android'}
]

# === قوالب اليوزرات (من User_check.py) ===
TEMPLATE_TYPES = {
    '١': ('char', 'fixed', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),    
    '٢': ('char', 'full', 'abcdefghijklmnopqrstuvwxyz'),     
    '٣': ('digit', 'fixed', '0123456789'),            
    '٤': ('digit', 'full', '0123456789'),             
    '_': ('literal', '_', ['_'])                      
}